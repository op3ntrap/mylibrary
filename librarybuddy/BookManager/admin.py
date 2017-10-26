# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.html import format_html
from django.contrib import admin
from django import forms
from .models import Book, Magazine, Journal, ResearchPaper, DigitalRecords
from .extract import Extractor


class BookAdminForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ()


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'authors', 'is_available', 'access', 'publisher', 'published_date', 'tags', 'page_count',
        '_book_cover')
    list_filter = ('is_available', 'access',)

    def _book_cover(self, obj=None):
        return format_html('<img src="{}" />', obj.cover.url)

    _book_cover.allow_tags = True
    ordering = ['title']
    search_fields = ['identifier_value']
    date_hierarchy = 'last_modified_on'
    actions = ['update_availability_true', 'update_availability_false']
    form = BookAdminForm

    # Custom Actions on the Archive records
    def update_availability_false(self, request, queryset):
        rows_updated = queryset.update(is_available=False)
        if rows_updated == 1:
            message_bit = "1 archive was"
        else:
            message_bit = "%s archives were" % rows_updated
        self.message_user(request, "%s successfully marked as not available." % message_bit)

    update_availability_false.short_description = "Update the archives selected as not available"

    def update_availability_true(self, request, queryset):
        rows_updated = queryset.update(is_available=True)
        if rows_updated == 1:
            message_bit = "1 archive was"
        else:
            message_bit = "%s archives were" % rows_updated
        self.message_user(request, "%s successfully marked as available." % message_bit)

    update_availability_true.short_description = "Update the archives selected as available"
