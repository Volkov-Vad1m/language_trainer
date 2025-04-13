"""
Модель карточки для словаря в приложении cards.
"""

from django.db import models


class Card(models.Model):
    """Модель карточки со словом, переводом и ссылкой на изображение."""

    word = models.CharField(max_length=100)
    translation = models.CharField(max_length=100)
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.word} — {self.translation}"
