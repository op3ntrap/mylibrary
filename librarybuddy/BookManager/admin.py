# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Book, Magazine, Journal, ResearchPaper, DigitalRecords

# Register your models here.
# TODO using the below documented Template Populate ModelAdmin Classes for every APP.
"""
@admin.register(model1,model2,model3,model4)
class ModelAdmin(admin.ModelAdmin):
    exclude = ('field_name',)
    list_display=('',)
    list_filter=(('',admin.RelatedOnlyFieldListFilter),)
    ordering =
    admin.site.disable_action('delete_selected')
    search_fields=['model__fieldname']
    actions=['action_type']
    def action_type(self,request,queryset):
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s successfully marked as published." % message_bit)
    action_type.short_description = ""
    # Another Action for intermediary pages and export of data.
    from django.contrib import admin
    from django.contrib.contenttypes.models import ContentType
    from django.http import HttpResponseRedirect
    def export_selected_objects(modeladmin, request, queryset):
        selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
        ct = ContentType.objects.get_for_model(queryset.model)
        return HttpResponseRedirect("/export/?ct=%s&ids=%s" % (ct.pk, ",".join(selected)))
        # TODO write a view for this function
    admin.site.add_action(export_selected_objects, 'export_selected') # to make the action available sitewide   
    from .widgets import RichTextEditorWidget
    formfield_overrides = {
        models.TextField: {'widget': RichTextEditorWidget},
    }
    # Class Method for controlling the available options between the users.
    def formfield_for_choice_field(self, db_field, request, ** kwargs):
        if db_field.name == "status":
            kwargs['choices'] = (
            ('accepted', 'Accepted'),
            ('denied', 'Denied'),
            )
        if request.user.is_superuser:
            kwargs['choices'] += (('ready', 'Ready for deployment'),)
        return super(MyModelAdmin, self).formfield_for_choice_field(db_field,request, ** kwargs)
    # Other Methods that will be useful
    ModelAdmin.message_user(request,message,level=messages.INFO,extra_tags=’‘,fail_silently=False)
    ModelAdmin.has_delete_permission(request, obj=None)
    ModelAdmin.has_add_permission(request, obj=None)
    ModelAdmin.has_create_permission(request, obj=None)
    ModelAdmin.has_update_permission(request, obj=None) # others include module,change user permission statistics
    class Media:
        # Media Static files for django admin assets.
        css = {
        "all": ("my_styles.css",)
        }
        js = ("my_code.js",)
admin.site.register(Model,ModelAdmin)
"""


@admin.register(Book)
class ArchiveAdmin(admin.ModelAdmin):
    list_display = ('title', 'authors', 'is_available', 'access', 'publisher', 'published_date', 'tags', 'page_count')
    list_filter = ('is_available', 'access',)
    ordering = ['title']
    search_fields = ['title', 'authors', 'description', 'tags']
    date_hierarchy = 'last_modified_on'

    def get_actions(self, request):
        actions = super(ArchiveAdmin, self).get_actions(request)
        if request.user.is_superuser is False and 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

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
