# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-08 07:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
	dependencies = [
		('TransactionManager', '0009_auto_20171108_1234'),
	]

	operations = [
		migrations.AlterField(
				model_name='lend',
				name='returning_date',
				field=models.DateTimeField(default=datetime.datetime(2017, 12, 8, 7, 5, 31, 413613, tzinfo=utc)),
		),
		migrations.AlterField(
				model_name='returning',
				name='returning_date',
				field=models.DateTimeField(default=datetime.datetime(2017, 12, 8, 7, 5, 31, 413613, tzinfo=utc)),
		),
	]
