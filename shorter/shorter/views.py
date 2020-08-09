from django.http import HttpRequest, HttpResponse
from django.template import loader
import datetime
from datetime import datetime


def index(request: HttpRequest):

    template = loader.get_template('index.html')
    return HttpResponse(template.render({
        'today': datetime.now()
    }))
