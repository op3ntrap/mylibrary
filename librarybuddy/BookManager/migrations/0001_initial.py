# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 05:30
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(blank=True, help_text='ISBN Identifier of the book', max_length=15, null=True)),
                ('asin', models.CharField(blank=True, help_text='ASIN Identifier of the book', max_length=15, null=True)),
                ('title', models.CharField(help_text='Book Title', max_length=100)),
                ('authors', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), size=None)),
                ('publisher', models.CharField(blank=True, max_length=30, null=True)),
                ('published_date', models.DateField()),
                ('publication_type', models.CharField(max_length=30)),
                ('languages', models.CharField(max_length=30)),
                ('cover', models.ImageField(upload_to=b'')),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), size=None)),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
    ]
