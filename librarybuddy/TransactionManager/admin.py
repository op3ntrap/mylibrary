# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# from django.core import validators
from django.contrib import admin
from django.apps import apps
from .models import Lend, Returning
from django import forms
from django.utils.html import *


class LendForm(forms.ModelForm):
    class Meta:
        model = apps.get_model('TransactionManager', model_name='Lend')
        exclude = ()


@admin.register(Lend)
class LendAdmin(admin.ModelAdmin):
    form = LendForm
    fields = ['archive', 'client', 'issuer', 'issue_date', '_QR_Code', ]
    list_display = ('archive', 'client', 'issuer', 'issue_date',)
    search_fields = ['archive__identifier_value']
    list_filter = ['issue_date', 'client__email_address']
    ordering = ['issue_date']

    def _QR_Code(self, obj):
        """
        Generate QrCode using the python QRCode Library and save it in the media folders
        :param obj: Lending Record being edited
        :return: Markup Element
        """
        if obj.archive_id is None:
            return '<div class="right-align"><button type="submit" value="Save and add another" class="waves-effect waves-light btn white-text" name="_continue">Process</button></div>'
        else:
            import qrcode
            qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
            )
            returning_url = 'http://127.0.0.1:8000/TransactionManager/returning/{}/change/'.format(
                    str(obj.returning_record._id))
            qr.add_data(returning_url, optimize=20)
            qr.make()
            img = qr.make_image(fill_color="white", back_color="indigo")
            img.save(stream='covers/' + str(obj.returning_record_id) + '.png', format='png')
            qr_code = '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"><link href="/static/material/css/materialize.admin.min.css" rel="stylesheet"><script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script><script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script><div class=wrapper><button type="button" value="Save and add another" class="waves-effect waves-light btn white-text" data-toggle="modal" data-target="#myModal" style="box-sizing: none; overflow: none;" align="right">Code</button><style type="text/css">@media print{body{visibility: hidden;}.to-print{visibility: visible; position: absolute; top: 0; left: 0;}}</style><div class="modal fade " id="myModal" role="dialog" style="display : inline;background-color: #fafafa00;box-shadow: 0 8px 10px 1px rgba(0, 0, 0, 0),0 3px 14px 2px rgba(0,0,0,0),0 5px 5px -3px rgba(0,0,0,0);"> <div class="modal-dialog modal-sm"><div class="modal-content"> <div class="modal-header"> <button type="button" class="close" data-dismiss="modal">&times;</button> <h4 class="modal-title">QR Code</h4></div><div class="modal-body"><p align="center"><img class="to-print" height="200" width="200" src=' + '/covers/' + str(
                    obj.returning_record._id) + '.png' + ' alt="this is the image"/></p></div><div class="modal-footer"><button type="button" class="btn btn-default" onclick="window.print();">Print</button> </div></div></div></div></div>'
            print(qr_code)
            return qr_code

    _QR_Code.allow_tags = True
    _QR_Code.short_description = "QR Code"

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """
        Only display books which are available.
        :param db_field:
        :param request:
        :param kwargs:
        :return:
        """
        if db_field.name == 'archive':
            archive_instance = apps.get_model('BookManager', model_name='Book')
            kwargs['queryset'] = archive_instance.objects.filter(is_available=True, access=True)
        return super(LendAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_readonly_fields(self, request, obj=None):
        """
        Restrict the fields which are to be edited after creating the object.
        :param request:
        :param obj:
        :return:
        """
        readonly_fields = ['issue_date', 'returning_record', '_QR_Code', ]
        if obj is not None:
            readonly_fields.extend(['archive', 'client', 'issuer', ])
            return readonly_fields
        return readonly_fields

    def get_fields(self, request, obj=None):
        """
        Compute which fields are to be displayed and when. Standard library function replaced.
        :param request:
        :param obj:
        :return: Fields to display on the admin forms
        """
        fields = ['archive', 'client', 'issuer', 'issue_date', '_QR_Code', ]
        if obj is not None:
            fields = ['archive', 'client', 'issuer', 'issue_date', '_QR_Code', ]
            return fields
        return fields


@admin.register(Returning)
class ReturningAdmin(admin.ModelAdmin):
    ordering = ['returned_date']
    list_display = ('archive', 'client', 'issuer', 'issue_date',)
    search_fields = ['archive__identifier_value']
    list_filter = ('issue_date', 'client__email_address', 'returned')

    def get_readonly_fields(self, request, obj=None):
        """
        Restrict the fields which are to be edited after creating the object.
        :param request:
        :param obj:
        :return:
        """
        readonly_fields = ['issue_date', 'returned_date', 'archive', 'client', 'issuer', ]
        if obj.returned is False:
            return readonly_fields
        else:
            readonly_fields.append('returned')
            readonly_fields.append('penalty_charged')
            return readonly_fields
