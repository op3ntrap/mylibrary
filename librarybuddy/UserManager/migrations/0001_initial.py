# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-12 05:45
from __future__ import unicode_literals

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
                name='Librarian',
                fields=[
                    ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                    ('role', models.CharField(
                            choices=[('pages', 'Pages'), ('technician', 'Library Technician'),
                                     ('librarian', 'Librarian'),
                                     ('manager', 'Manager'), ('director', 'Director')], max_length=20)),
                    ('book_recommendations', django.contrib.postgres.fields.ArrayField(
                            base_field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
                            blank=True,
                            null=True, size=None)),
                ],
        ),
        migrations.CreateModel(
                name='Member',
                fields=[
                    ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                    ('first_name', models.CharField(help_text='First Name', max_length=63)),
                    ('middle_name', models.CharField(blank=True, help_text='Middle Name', max_length=63)),
                    ('last_name', models.CharField(help_text='Last Name', max_length=63)),
                    ('age', models.IntegerField(blank=True, help_text='Age of the User eg 18')),
                    ('occupation', models.CharField(
                            choices=[('engineer', 'Engineer'), ('doctor', 'Doctor'), ('student', 'Student'),
                                     ('researcher', 'Researcher'), ('home_maker', 'Home Maker'), ('artist', 'Artist'),
                                     ('management', 'Manager'), ('entrepreneur', 'Entrepreneur'),
                                     ('teacher', 'Teacher'),
                                     ('other', 'Other')], help_text='Select the Occupation of the User',
                            max_length=20)),
                    ('email_address', models.EmailField(help_text='Email Address', max_length=254, unique=True)),
                    ('twitter_handle',
                     models.CharField(blank=True, help_text='(optional) Twtitter Handle', max_length=20, null='')),
                    ('membership', models.BooleanField()),
                    ('join_date', models.DateField(auto_now_add=True)),
                    ('entry_log',
                     django.contrib.postgres.fields.ArrayField(base_field=models.DateField(auto_now=True), size=None)),
                    ('lending_log', django.contrib.postgres.fields.ArrayField(
                            base_field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
                            blank=True,
                            null=True, size=None)),
                ],
        ),
        migrations.CreateModel(
                name='Membership',
                fields=[
                    ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                    ('joining_fee', models.FloatField(
                            help_text='Amount which is needed to be paid to get a membership in the library')),
                    ('validity',
                     models.CharField(choices=[('1yr', '1 year'), ('2yr', '2 year'), ('lifetime', 'lifetime')],
                                      help_text='Validity of the Type of a Membership', max_length=10)),
                    ('lending_power', models.IntegerField()),
                    ('type', models.CharField(choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D')], max_length=10)),
                ],
        ),
        migrations.AddField(
                model_name='member',
                name='membership_type',
                field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserManager.Membership'),
        ),
    ]
