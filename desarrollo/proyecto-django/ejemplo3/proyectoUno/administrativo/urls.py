"""
    Manejo de urls para la aplicación
    administrativo
"""
from django.urls import path
from . import views

from django.contrib import admin
urlpatterns = [
    path('', views.index, name='index'),

 ]
