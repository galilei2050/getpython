from django.http import Http404
from shortcut.models import *
from collections import UserDict


class ShortUrlStorage(UserDict):
    def __missing__(self, key):
        shortcut = ShortUrl.objects.get(key=key)
        self[key] = shortcut
        return shortcut

    def shortcut(self, url):
        short_url_qs = ShortUrl.objects.filter(url=url)[:1]
        if short_url_qs:
            short_url = short_url_qs[0]
            return short_url.key
        num = ShortUrl.objects.count() + 1
        key = f'{num:x}'
        short_url = ShortUrl(key=key, url=url)
        short_url.save()
        self[key] = short_url
        return key

    def url(self, short_key):
        short_url = self[short_key]
        short_url.visits += 1
        short_url.save()
        return short_url.url

short_storage = ShortUrlStorage()
