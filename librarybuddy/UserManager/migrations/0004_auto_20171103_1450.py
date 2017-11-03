# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-03 14:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('UserManager', '0003_member_user'),
    ]

    operations = [
        migrations.AddField(
                model_name='librarian',
                name='profile_pic',
                field=models.ImageField(null=True, upload_to='', verbose_name='Profile Picture'),
        ),
        migrations.AddField(
                model_name='librarian',
                name='user',
                field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE,
                                           to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
                model_name='member',
                name='profile_pic',
                field=models.ImageField(null=True, upload_to='', verbose_name='Profile Picture'),
        ),
    ]
