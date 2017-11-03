from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.archive_catalog, name='archive_catalog'),
    url(r'^base', views.view_base_template, name='base_template_preview')
]
