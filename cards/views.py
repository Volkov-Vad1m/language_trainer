"""
Представления для приложения cards: отображение слов, добавление, тренировка и поиск.
"""

import random
import json
from django.shortcuts import render, redirect
from django.db import models
from .models import Card
from .forms import CardForm, BulkUploadForm


def index(request):
    """Главная страница со списком карточек и формой поиска."""
    query = request.GET.get("q")
    if query:
        cards = Card.objects.filter(
            models.Q(word__icontains=query) |
            models.Q(translation__icontains=query)
        )
    else:
        cards = Card.objects.all()
    return render(request, "cards/index.html", {"cards": cards})


def add_card(request):
    """Форма добавления одной карточки."""
    if request.method == "POST":
        form = CardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = CardForm()
    return render(request, "cards/add_card.html", {"form": form})


def add_bulk(request):
    """Форма массовой загрузки карточек."""
    if request.method == "POST":
        form = BulkUploadForm(request.POST)
        if form.is_valid():
            lines = form.cleaned_data["bulk_text"].splitlines()
            for line in lines:
                parts = [p.strip() for p in line.split("-")]
                if len(parts) >= 2:
                    word, translation = parts[0], parts[1]
                    image_url = parts[2] if len(parts) == 3 else ""
                    Card.objects.create(
                        word=word, translation=translation, image_url=image_url
                    )
            return redirect("index")
    else:
        form = BulkUploadForm()
    return render(request, "cards/add_bulk.html", {"form": form})


def train(request):
    """Режим тренировки слов с пользовательским вводом."""
    cards = list(Card.objects.all())
    random.shuffle(cards)
    cards_data = [{"word": c.word, "translation": c.translation} for c in cards]
    return render(
        request,
        "cards/train.html",
        {"cards": cards, "cards_json": json.dumps(cards_data, ensure_ascii=False)},
    )
