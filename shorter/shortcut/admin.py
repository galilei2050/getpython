from django.contrib import admin

# Register your models here.
from .models import ShortUrl


class ShortUrlAdmin(admin.ModelAdmin):
    pass


admin.site.register(ShortUrl, ShortUrlAdmin)
