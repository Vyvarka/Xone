from django.urls import path
from . import views


app_name = 'generator_url'
urlpatterns = [
    path('', views.home, name='home'),
    path('list', views.url_list, name='list'),
]
