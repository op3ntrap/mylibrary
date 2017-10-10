# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from localflavor.in_.forms import INPhoneNumberField, INAadhaarNumberField
from django.contrib.postgres.fields import ArrayField, JSONField
# from django.contrib.localflavor

# TODO Class specific functions of User needs to be written

OCCUPATION_CHOICES = (
    ('engineer', 'Engineer'),
    ('doctor', 'Doctor'),
    ('student', 'Student'),
    ('researcher', 'Researcher'),
    ('home_maker', 'Home Maker'),
    ('artist', 'Artist'),
    ('management', 'Manager'),
    ('entrepreneur', 'Entrepreneur'),
    ('teacher', 'Teacher'),
    ('other', 'Other'),
)
MEMBERSHIP_CHOICES = (
    ('a', 'A'),
    ('b', 'B'),
    ('c', 'C'),
    ('d', 'D'),
)


class User(models.Model):
    """
    Main Class of all the users of a library.
    This class does not hold the librarians working in the library.
    """
    first_name = models.CharField(max_length=63, help_text='First Name')
    middle_name = models.CharField(max_length=63, help_text='Middle Name')
    last_name = models.CharField(max_length=63, help_text='Last Name')
    age = models.IntegerField(help_text='Age of the User eg 18')
    occupation = models.CharField(
        max_length=20, choices=OCCUPATION_CHOICES, help_text='Select the Occupation of the User')
    primary_mobile = INPhoneNumberField(
        help_text='Primary Mobile Number')
    alternate_mobile = INPhoneNumberField(
        help_text='Alternate Mobile Number')
    aadhar_id = INAadhaarNumberField(help_text='12 digit Aadhar Number')
    email_address = models.EmailField()
    twitter_handle = models.CharField(max_length=20)
    membership = models.BooleanField()
    membership_type = models.CharField(
        max_length=20, choices=MEMBERSHIP_CHOICES)
    join_date = models.DateField(auto_now_add=True)
    entry_log = ArrayField(
        models.DateField(auto_now=True))
    lending_log = ArrayField(
        JSONField()
    )
    """
    Format for lending log of the User class is
    lending_log = [
    		{
    		'Lend_ID': '34343434',
    		'date':'date_time',
    		'return_status': (boolean),
			'penalty_paid': (penalty_paid),
    	}
    ]
    """
    def user_functions(self):
    	pass
