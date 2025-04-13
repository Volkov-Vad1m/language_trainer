"""
Формы для добавления карточек в приложении cards.
"""

from django import forms
from .models import Card


class CardForm(forms.ModelForm):
    """Форма для создания одной карточки."""

    class Meta:
        """Метаданные: связываем форму с моделью Card и указываем поля."""

        model = Card
        fields = ["word", "translation", "image_url"]


class BulkUploadForm(forms.Form):
    """Форма для батчевой загрузки карточек"""

    bulk_text = forms.CharField(widget=forms.Textarea)
