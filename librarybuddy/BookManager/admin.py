# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Book, Magazine, Journal, ResearchPaper, DigitalRecords


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    pass


class JournalAdmin(admin.ModelAdmin):
    pass


admin.site.register(Book)
admin.site.register(Magazine)
