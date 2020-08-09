from django.contrib import admin
from django.urls import path
from .redirect import short_to_log_redirect

urlpatterns = [
    path('', short_to_log_redirect)
]