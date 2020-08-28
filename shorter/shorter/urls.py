from django.contrib import admin
from django.urls import path, include
from shortcut.urls import urlpatterns as shortcut_urls
from user.urls import urlpatterns as user_urls
import logging

logging.root.setLevel(logging.INFO)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(shortcut_urls)),
    path('user/', include((user_urls, 'user'), namespace='u'))
]
