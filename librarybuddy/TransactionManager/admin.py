# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Lend, Returning


# Register your models here.

@admin.register(Lend)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('book', 'client', 'issuer', 'issue_date')
