# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core import validators
from django.contrib import admin
from django.apps import apps
from .models import Lend, Returning
from django import forms


class LendForm(forms.ModelForm):
    class Meta:
        model = apps.get_model('TransactionManager', model_name='Lend')
        exclude = ()


@admin.register(Lend)
class LendAdmin(admin.ModelAdmin):
    form = LendForm
    list_display = ('archive', 'client', 'issuer', 'issue_date',)
    search_fields = ['archive__identifier_value']
    list_filter = ('issue_date', 'client__email_address')
    ordering = ['issue_date']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'archive':
            archive_instance = apps.get_model('BookManager', model_name='Book')
            kwargs['queryset'] = archive_instance.objects.filter(is_available=True, access=True)
        return super(LendAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = ['issue_date', 'returning_record']
        if obj is not None:
            if obj.returning_record.returned is False:
                return readonly_fields
            else:
                readonly_fields.extend(['archive', 'client', 'issuer', ])
                return readonly_fields
        return readonly_fields


class ReturningForm(forms.ModelForm):
    class Meta:
        model = apps.get_model('TransactionManager', model_name='Returning')
        exclude = ()

        # def clean(self):
        #     cleaned_data = super(ReturningForm, self).clean()
        #     status = cleaned_data.get('Returned')


@admin.register(Returning)
class ReturningAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        readonly_fields = ['issue_date', 'returned_date', 'archive', 'client', 'issuer', ]
        if obj.returned is False:
            return readonly_fields
        else:
            readonly_fields.append('returned')
            readonly_fields.append('penalty_charged')
            return readonly_fields

    ordering = ['returned_date']
    form = ReturningForm
    list_display = ('archive', 'client', 'issuer', 'issue_date',)
    search_fields = ['archive__identifier_value']
    list_filter = ('issue_date', 'client__email_address', 'returned')
