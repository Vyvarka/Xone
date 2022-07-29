from django.db import models
from django.contrib.auth.models import User
from django.core import validators


class Url(models.Model):
    original_url = models.URLField(max_length=100, db_index=True,
                                   validators=[validators.URLValidator(message='Введен некорректный URL-адрес')])
    short_url = models.CharField(max_length=250, unique=True, null=True)
    owners = models.ManyToManyField(User)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'Адреса'
        verbose_name = 'Адрес'

    def __str__(self):
        return self.short_url

