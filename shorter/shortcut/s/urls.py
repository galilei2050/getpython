from django.contrib import admin
from django.urls import path
from .short import short_url
from .long import long_url


urlpatterns = [
    path('', short_url),
    path('<str:short_key>', long_url)
]