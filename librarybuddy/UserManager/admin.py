# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *
# Register your models here.
# admin.site.register(Membership)
admin.site.register(Librarian)


# admin.site.register(Member)

@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
	icon = '<i class="material-icons">&#xE8D3;</i>'  # Material Icon


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
	icon = '<i class="material-icons">&#xE8A6;</i>'  # Material Icon
