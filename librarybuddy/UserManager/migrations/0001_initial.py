# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-20 16:48
from __future__ import unicode_literals

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Librarian',
            fields=[
                ('primary_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(help_text='First Name', max_length=63, verbose_name='First Name')),
                ('middle_name',
                 models.CharField(blank=True, default='', help_text='Middle Name', max_length=63, null=True,
                                  verbose_name='Middle Name')),
                ('last_name', models.CharField(help_text='Last Name', max_length=63, verbose_name='Last Name')),
                ('role', models.CharField(
                    choices=[('pages', 'Pages'), ('technician', 'Library Technician'), ('librarian', 'Librarian'),
                             ('manager', 'Manager'), ('director', 'Director')], max_length=20, verbose_name='Role')),
                ('book_recommendations', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True), blank=True, null=True, size=None)),
                ('email_address', models.EmailField(help_text='Email Address', max_length=254, unique=True,
                                                    verbose_name='Email Address')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('primary_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(help_text='First Name', max_length=63, verbose_name='First Name')),
                ('middle_name',
                 models.CharField(blank=True, default='', help_text='Middle Name', max_length=63, null=True,
                                  verbose_name='Middle Name')),
                ('last_name', models.CharField(help_text='Last Name', max_length=63, verbose_name='Last Name')),
                ('age', models.IntegerField(help_text='Age of the User eg 18', verbose_name='Age')),
                ('occupation', models.CharField(
                    choices=[('engineer', 'Engineer'), ('doctor', 'Doctor'), ('student', 'Student'),
                             ('researcher', 'Researcher'), ('home_maker', 'Home Maker'), ('artist', 'Artist'),
                             ('management', 'Manager'), ('entrepreneur', 'Entrepreneur'), ('teacher', 'Teacher'),
                             ('other', 'Other')], help_text='Select the Occupation of the User', max_length=20,
                    verbose_name='Occupation')),
                ('email_address', models.EmailField(help_text='Email Address', max_length=254, unique=True,
                                                    verbose_name='Email Address')),
                ('twitter_handle',
                 models.CharField(blank=True, help_text='(optional) Twitter Handle', max_length=20, null='',
                                  verbose_name='Twitter Handle')),
                ('membership', models.BooleanField(verbose_name='Is a Member?')),
                ('join_date', models.DateField(auto_now_add=True, verbose_name='Joining Date')),
                ('entry_log', django.contrib.postgres.fields.ArrayField(base_field=models.DateField(auto_now=True), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('primary_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('joining_fee', models.FloatField(default=100.0,
                                                  help_text='Amount which is needed to be paid to get a membership in the library',
                                                  verbose_name='Joining Fee')),
                ('validity', models.CharField(choices=[('1yr', '1 year'), ('2yr', '2 year'), ('lifetime', 'lifetime')],
                                              default='1yr', help_text='Validity of the Type of a Membership',
                                              max_length=10, verbose_name='Validity of the Membership Plan')),
                ('lending_power', models.IntegerField(default=1, verbose_name='Number of Books that can be borrowed')),
                ('mode',
                 models.CharField(choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D')], default='c', max_length=10,
                                  unique=True, verbose_name='Membership ')),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='membership_type',
                field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE,
                                        to='UserManager.Membership', verbose_name='Membership Type'),
        ),
    ]
