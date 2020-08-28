from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .auth_form import AuthForm


def auth(request: HttpRequest):
    if request.method != "POST":
        return HttpResponse(status=405)
    go_next = request.GET.get('redirect', '/')
    if request.user.is_authenticated:
        return HttpResponseRedirect(go_next)
    auth_form = AuthForm(request.POST)
    if not auth_form.is_valid():
        return HttpResponse(400)
    user = authenticate(request, **auth_form.cleaned_data)
    if user:
        login(request, user)
        return HttpResponseRedirect(go_next)
    else:
        return HttpResponse(403)

