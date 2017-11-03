# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(Membership)
admin.site.register(Librarian)
admin.site.register(Member)
