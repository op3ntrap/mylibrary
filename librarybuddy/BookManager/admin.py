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
	icon = '<i class="material-icons">&#xE865;</i>'  # Book Material Icon
    fields = (
        '_Cover', 'identifier', 'identifier_value', 'title', 'description', 'authors', 'publisher', 'published_date',
        'page_count',
        'is_available', 'access', 'copies', 'accessibility', 'tags', 'genre',)
    readonly_fields = ('_Cover', '_Cover_list',)
    list_display = (
        'title', 'authors', 'is_available', '_Cover_list', 'access', 'publisher', 'published_date', 'tags',
        'page_count',)
    list_filter = ('is_available', 'access', 'genre')

    def _Cover(self, obj=None):
        return format_html(
                '<div><img style="Float : left" src="{}" /><img style="Float : right" height="150" width="150" src="{}" /></div><p style="clear: both;">',
                obj.cover.url, '/covers/' + obj.identifier_value + "_qr_code.png")

    _Cover.allow_tags = True
    _Cover.short_description = "Cover"

    # def _QR_Field(self, obj=None):
    #     return format_html(
    #             '<img style="Float : left" height="150" width="150" src="{}" /><p style="clear: both;">',
    #             '/covers/' + obj.identifier_value + "_qr_code.png")

    # _QR_Field.allow_tags = True
    # _QR_Field.short_description = "QR Code"

    def _Cover_list(self, obj=None):
        return format_html(
                '<img src="{}" />', obj.cover.url, '/covers/')

    _Cover_list.allow_tags = True
    _Cover_list.short_description = "Cover"
    ordering = ['title']
    search_fields = ['identifier_value', 'title', 'authors']
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
