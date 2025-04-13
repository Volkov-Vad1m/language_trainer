"""
Главный маршрутизатор проекта language_trainer.
Определяет базовые URL-адреса, включая админку и приложение cards.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("cards.urls")),
]
