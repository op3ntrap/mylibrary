# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-14 05:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('UserManager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
                model_name='librarian',
                name='role',
                field=models.CharField(
                    choices=[('pages', 'Pages'), ('technician', 'Library Technician'), ('librarian', 'Librarian'),
                             ('manager', 'Manager'), ('director', 'Director')], max_length=20, verbose_name='Role'),
        ),
        migrations.AlterField(
                model_name='member',
                name='age',
                field=models.IntegerField(blank=True, help_text='Age of the User eg 18', verbose_name='Age'),
        ),
        migrations.AlterField(
                model_name='member',
                name='email_address',
                field=models.EmailField(help_text='Email Address', max_length=254, unique=True,
                                        verbose_name='Email Address'),
        ),
        migrations.AlterField(
                model_name='member',
                name='first_name',
                field=models.CharField(help_text='First Name', max_length=63, verbose_name='First Name'),
        ),
        migrations.AlterField(
                model_name='member',
                name='join_date',
                field=models.DateField(auto_now_add=True, verbose_name='Joining Date'),
        ),
        migrations.AlterField(
                model_name='member',
                name='last_name',
                field=models.CharField(help_text='Last Name', max_length=63, verbose_name='Last Name'),
        ),
        migrations.AlterField(
                model_name='member',
                name='membership',
                field=models.BooleanField(verbose_name='Is a Member?'),
        ),
        migrations.AlterField(
                model_name='member',
                name='membership_type',
                field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE,
                                        to='UserManager.Membership', verbose_name='Membership Type'),
        ),
        migrations.AlterField(
                model_name='member',
                name='middle_name',
                field=models.CharField(blank=True, default='', help_text='Middle Name', max_length=63, null=True,
                                       verbose_name='Middle Name'),
        ),
        migrations.AlterField(
                model_name='member',
                name='occupation',
                field=models.CharField(choices=[('engineer', 'Engineer'), ('doctor', 'Doctor'), ('student', 'Student'),
                                                ('researcher', 'Researcher'), ('home_maker', 'Home Maker'),
                                                ('artist', 'Artist'), ('management', 'Manager'),
                                                ('entrepreneur', 'Entrepreneur'), ('teacher', 'Teacher'),
                                                ('other', 'Other')], help_text='Select the Occupation of the User',
                                       max_length=20, verbose_name='Occupation'),
        ),
        migrations.AlterField(
                model_name='member',
                name='twitter_handle',
                field=models.CharField(blank=True, help_text='(optional) Twitter Handle', max_length=20, null='',
                                       verbose_name='Twitter Handle'),
        ),
        migrations.AlterField(
                model_name='membership',
                name='joining_fee',
                field=models.FloatField(default=100.0,
                                        help_text='Amount which is needed to be paid to get a membership in the library',
                                        verbose_name='Joining Fee'),
        ),
        migrations.AlterField(
                model_name='membership',
                name='lending_power',
                field=models.IntegerField(default=1, verbose_name='Number of Books that can be borrowed'),
        ),
        migrations.AlterField(
                model_name='membership',
                name='mode',
                field=models.CharField(choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D')], default='c',
                                       max_length=10, unique=True, verbose_name='Membership '),
        ),
        migrations.AlterField(
                model_name='membership',
                name='validity',
                field=models.CharField(choices=[('1yr', '1 year'), ('2yr', '2 year'), ('lifetime', 'lifetime')],
                                       default='1yr', help_text='Validity of the Type of a Membership', max_length=10,
                                       verbose_name='Validity of the Membership Plan'),
        ),
    ]
