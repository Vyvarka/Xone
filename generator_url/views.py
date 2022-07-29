from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from .models import Url
from .forms import UrlForm
from .logic import url_generator, check_url_owner


def home(request):
    """Главная страница"""
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = UrlForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = UrlForm(data=request.POST)
        if form.is_valid():
            url = Url.objects.filter(original_url__exact=request.POST['original_url'])  # проверяем наличие URL в БД
            user = User.objects.get(id=request.user.id)
            if url:
                url[0].owners.add(user)
            else:
                new_url = form.save(commit=False)  # сохраняем данные из формы, но не в БД
                new_url.short_url = url_generator()  # генерируем уникальный адрес
                new_url.save()  # сохраняем данные в БД
                new_url.owners.add(user)  # добавляем владельца
            return redirect('generator_url:list')
    context = {'form': form}
    return render(request, 'generator_url/home.html', context)


@login_required()
def url_list(request):
    """Страница со всеми URLs авторизированного пользователя"""
    lst = Url.objects.filter(owners=request.user)
    domain = request.META['HTTP_HOST']
    context = {'lst': lst, 'domain': domain}
    return render(request, 'generator_url/list.html', context)


@login_required()
def short(request, short_url):
    """Контроллер перенаправления"""
    url = get_object_or_404(Url, short_url=short_url)
    check_url_owner(request, url)
    return redirect(url.original_url)
