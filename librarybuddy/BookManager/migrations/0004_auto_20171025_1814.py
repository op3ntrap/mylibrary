# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 18:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookManager', '0003_auto_20171025_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='tags',
            field=models.CharField(blank=True, help_text='Enter the relevant Tags separated by a comma: <br>Eg. good,bad <br>For Tags which contain spaces can be entered by surrounding them with double quotes. <br>Eg."Machine Learning"', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(blank=True, help_text='Book Title', max_length=100),
        ),
        migrations.AlterField(
            model_name='digitalrecords',
            name='publisher',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='digitalrecords',
            name='tags',
            field=models.CharField(blank=True, help_text='Enter the relevant Tags separated by a comma: <br>Eg. good,bad <br>For Tags which contain spaces can be entered by surrounding them with double quotes. <br>Eg."Machine Learning"', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='digitalrecords',
            name='title',
            field=models.CharField(blank=True, help_text='Book Title', max_length=100),
        ),
        migrations.AlterField(
            model_name='journal',
            name='publisher',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='journal',
            name='tags',
            field=models.CharField(blank=True, help_text='Enter the relevant Tags separated by a comma: <br>Eg. good,bad <br>For Tags which contain spaces can be entered by surrounding them with double quotes. <br>Eg."Machine Learning"', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='journal',
            name='title',
            field=models.CharField(blank=True, help_text='Book Title', max_length=100),
        ),
        migrations.AlterField(
            model_name='magazine',
            name='publisher',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='magazine',
            name='tags',
            field=models.CharField(blank=True, help_text='Enter the relevant Tags separated by a comma: <br>Eg. good,bad <br>For Tags which contain spaces can be entered by surrounding them with double quotes. <br>Eg."Machine Learning"', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='magazine',
            name='title',
            field=models.CharField(blank=True, help_text='Book Title', max_length=100),
        ),
        migrations.AlterField(
            model_name='researchpaper',
            name='publisher',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='researchpaper',
            name='tags',
            field=models.CharField(blank=True, help_text='Enter the relevant Tags separated by a comma: <br>Eg. good,bad <br>For Tags which contain spaces can be entered by surrounding them with double quotes. <br>Eg."Machine Learning"', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='researchpaper',
            name='title',
            field=models.CharField(blank=True, help_text='Book Title', max_length=100),
        ),
    ]
