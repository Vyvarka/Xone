from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Url
from .forms import UrlForm
from .logic import url_generator


# Create your views here.
def home(request):
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = UrlForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = UrlForm(data=request.POST)
        if form.is_valid():
            new_url = form.save(commit=False)  # сохраняем данные из формы, но не в БД
            new_url.short_url = url_generator(url=new_url.original_url)  # сокращаем URL при помощи обработчика
            new_url.owner = request.user  # присваиваем владельца
            new_url.save()  # сохраняем данные в БД
            return redirect('generator_url:list')  # можно убрать перенаправление, если мешает
    context = {'form': form}
    return render(request, 'generator_url/home.html', context)


@login_required()
def url_list(request):
    """Страница со всеми URLs авторизированного пользователя"""
    lst = Url.objects.filter(owner=request.user)
    context = {'lst': lst}
    return render(request, 'generator_url/list.html', context)


