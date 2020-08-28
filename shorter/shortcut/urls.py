from django.contrib import admin
from django.urls import path, include
from .views import index
from .s import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('s/', include(urls.urlpatterns))
]
