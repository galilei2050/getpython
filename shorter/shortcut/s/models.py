from django.db import models
import datetime


class ShortUrl(models.Model):
    key = models.CharField(max_length=200)
    url = models.URLField()
    date = models.DateTimeField(default=lambda : datetime.datetime.now())
