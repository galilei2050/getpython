from django.db import models


class ShortUrl(models.Model):

    key = models.CharField(max_length=256)
    url = models.URLField()
    visits = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.url} - {self.key} - {self.visits}'

