from django.http import Http404


class ShortUrlStorage(object):
    def __init__(self):
        self._short_urls = {}

    def shortcut(self, url):
        short = self.next()
        self._short_urls[short] = url
        return short

    def url(self, short_key):
        u = self._short_urls.get(short_key, None)
        if u is None:
            raise Http404(f'Key {short_key} not found')
        return u

    def next(self):
        num = len(self._short_urls) + 1
        return f'{num:x}'


short_storage = ShortUrlStorage()
