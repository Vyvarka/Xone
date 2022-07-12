from django.forms import ModelForm, TextInput, Textarea

from .models import Url


class UrlForm(ModelForm):
    class Meta:
        model = Url
        fields = ['original_url']
        labels = {'original_url': ''}
        widgets = {
            'name': Textarea(attrs={
                'placeholder': 'Введите URL-адрес, который нужно сократить',
                'autofocus': 'on',
            }, ),
        }
