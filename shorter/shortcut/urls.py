from django.contrib import admin
from django.urls import path, include
from .views import index
from .s import urls

urlpatterns = [
    path('', index),
    path('s/', include(urls.urlpatterns))
]
