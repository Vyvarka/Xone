from django.forms import ModelForm, Textarea

from .models import Url


class UrlForm(ModelForm):
    class Meta:
        model = Url
        fields = ['original_url']
        labels = {'original_url': ''}
        widgets = {
            'original_url': Textarea(attrs={
                'autofocus': 'on',
            }, ),
        }
