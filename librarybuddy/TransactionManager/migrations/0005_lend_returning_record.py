# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 06:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TransactionManager', '0004_auto_20171025_0657'),
    ]

    operations = [
        migrations.AddField(
            model_name='lend',
            name='returning_record',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='TransactionManager.Returning'),
        ),
    ]
