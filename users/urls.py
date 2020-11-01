"""Определяет схемы url для пользователей"""
from django.urls import path, include

app_name = 'users'
urlpatterns = [
    # включить url авторизации по умолчанию
    path('', include('django.contrib.auth.urls')),
]