"""
Регистрация моделей приложения cards в административной панели Django.
"""

from django.contrib import admin
from .models import Card

admin.site.register(Card)
