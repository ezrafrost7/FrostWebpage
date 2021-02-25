"""
Definition of urls for FrostWebpage.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('api/', views.jokes, name='jokes'),
    path('api/joke', views.tellJoke, name='tellJokes'),
    path('admin/', admin.site.urls),
]
