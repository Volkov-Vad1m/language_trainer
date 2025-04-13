"""
URL-маршруты для приложения cards.
"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add_card, name="add_card"),
    path("add-bulk/", views.add_bulk, name="add_bulk"),
    path("train/", views.train, name="train"),
]
