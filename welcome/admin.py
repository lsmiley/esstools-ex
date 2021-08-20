from django.contrib import admin

from .models import PageView
from . import models
# Register your models here.


class PageViewAdmin(admin.ModelAdmin):
    list_display = ['hostname', 'timestamp']


admin.site.register(PageView, PageViewAdmin)


