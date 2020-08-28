from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .storage import short_storage


def long_url(request: HttpRequest, short_key):
    if request.method != "GET":
        return HttpResponse(status=405)
    return HttpResponseRedirect(redirect_to=short_storage.url(short_key))
