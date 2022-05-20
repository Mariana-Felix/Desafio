
from django.contrib import admin
from django.urls import path

from challenger.view import list_family

urlpatterns = [
    path('family/',list_family),
]
