from django.contrib import admin
from .models import Url

@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    list_display = ('original_url', 'short_url', 'owner', 'created')
    search_fields = ('original_url', 'owner')
    raw_id_fields = ('owner',)
    ordering = ('created',)
