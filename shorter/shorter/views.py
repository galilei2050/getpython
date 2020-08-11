from datetime import datetime

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .s import ShortUrlForm


def index(request: HttpRequest):
    if request.method == "POST":
        form = ShortUrlForm(request.POST)
    elif request.method == "GET":
        form = ShortUrlForm()
    else:
        return HttpResponse(status=405)
    context = {
        'short_url_form': form,
        'today': datetime.now()
    }
    return render(request, 'index.html', context)
