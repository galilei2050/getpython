import logging

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .form import ShortUrlForm
from .storage import short_storage

def short_url(request: HttpRequest):
    if request.method != "POST":
        return HttpResponse(status=405)
    form = ShortUrlForm(request.POST)
    if not form.is_valid():
        return render(request, 'index.html', context={'short_url_form': form})

    short_key = short_storage.shortcut(form.cleaned_data['url'])
    scheme = request.scheme
    host = request.get_host()
    port = request.get_port()
    port = '' if port not in {80, 443} else f':{port}'
    short_url = f'{scheme}://{host}{port}/s/{short_key}'
    logging.info("Short %s for user %s", short_url, request.user)
    return render(request, 'shorturl.html', context={'short_url': short_url})
