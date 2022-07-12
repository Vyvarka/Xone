from django.db import models
from django.contrib.auth.models import User

class Url(models.Model):
    original_url = models.TextField()
    short_url = models.CharField(max_length=250, unique=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.short_url

