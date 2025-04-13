"""
Конфигурация приложения cards для Django.
"""

from django.apps import AppConfig


class CardsConfig(AppConfig):
    """Конфигурационный класс приложения cards."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "cards"
