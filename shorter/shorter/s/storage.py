from django.http import Http404
from shortcut.models import *


class ShortUrlStorage(object):
    def __init__(self):
        self._short_urls = {}

    def shortcut(self, url):
        short = self.next()
        self._short_urls[short] = url
        ShortUrl(url=url, key=short).save()
        return short

    def url(self, short_key):
        u = self._short_urls.get(short_key, None)
        if u is None:
            shortcut = ShortUrl.objects.get(key=short_key)
            self._short_urls[short_key] = shortcut.url
            shortcut.visits += 1
            shortcut.save()
            return shortcut.url
        return u

    def next(self):
        num = len(self._short_urls) + 1
        return f'{num:x}'


short_storage = ShortUrlStorage()
