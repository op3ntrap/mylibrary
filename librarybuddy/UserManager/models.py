from __future__ import unicode_literals

import uuid

from django.contrib.postgres.fields import ArrayField, JSONField
from django.db import models
from localflavor.in_.forms import INPhoneNumberField, INAadhaarNumberField
from django.apps import apps
from django.contrib.auth.models import User


class Membership(models.Model):
    """
    Membership Class to maintain operations related to memberships in library
    """
    MEMBERSHIP_CHOICES = (
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
        ('d', 'D'),
    )  # Field Choices for the Membership.mode field
    VALIDITY_CHOICES = (
        ('1yr', '1 year'),
        ('2yr', '2 year'),
        ('lifetime', 'lifetime'),
    )  # Field Choices for the validity field
    primary_id = models.UUIDField(
            primary_key=True, default=uuid.uuid4, editable=False)  # pk field

    joining_fee = models.FloatField(
            help_text="Amount which is needed to be paid to get a membership in the library", default=100.0,
            verbose_name="Joining Fee")

    validity = models.CharField(
            max_length=10,
            choices=VALIDITY_CHOICES,
            help_text="Validity of the Type of a Membership",
            default='1yr',
            verbose_name='Validity of the Membership Plan'
    )
    lending_power = models.IntegerField(default=1, verbose_name='Number of Books that can be borrowed')
    mode = models.CharField(
            max_length=10, choices=MEMBERSHIP_CHOICES, unique=True, default='c', verbose_name='Membership '
    )

    def __str__(self):
        return "Class {} Membership with {} validity".format(self.mode, self.validity)


# -*- coding: utf-8 -*-


class Member(models.Model):
    """
    Main Class of all the users of a library.
    This class does not hold the librarians working in the library.

    1.Format for lending log of the User class :
    lending_log = [
        {
        'Lend_ID': '34343434',
        'date':'date_time',
        'return_status': (boolean),
        'penalty_paid': (penalty_paid),
        }
    ]
    2.Format for creating a user:
    test_user = Member(
        first_name = "Risan",
        last_name="Raja",
        middle_name=" ",
        membership=True,
        membership_type_id = Membership.objects.get(mode='a').primary_id,
        occupation='student',
        twitter_handle="@risan_raja",
        age=21,
        entry_log=[datetime.datetime.now()],
        )
    test_user.save()
    """

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
    primary_id = models.UUIDField(
            primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(
            max_length=63, help_text='First Name', blank=False, verbose_name='First Name')
    middle_name = models.CharField(
            max_length=63, help_text='Middle Name', null=True, blank=True, default='', verbose_name='Middle Name')
    last_name = models.CharField(
            max_length=63, help_text='Last Name', blank=False, verbose_name='Last Name')
    age = models.IntegerField(help_text='Age of the User eg 18', verbose_name='Age')
    occupation = models.CharField(
            max_length=20, choices=OCCUPATION_CHOICES, help_text='Select the Occupation of the User', blank=False,
            verbose_name='Occupation')
    primary_mobile = INPhoneNumberField(
            help_text='Primary Mobile Number')
    alternate_mobile = INPhoneNumberField(
            help_text='Alternate Mobile Number')
    aadhar_id = INAadhaarNumberField(
            help_text='12 digit Aadhar Number', )
    email_address = models.EmailField(
            help_text='Email Address', blank=False, unique=True, verbose_name='Email Address')
    twitter_handle = models.CharField(
            max_length=20, help_text='(optional) Twitter Handle', null="", blank=True, verbose_name='Twitter Handle')
    membership = models.NullBooleanField(verbose_name='Is a Member?', null=True)
    membership_type = models.ForeignKey(
            'Membership', on_delete=models.CASCADE, null=True,
            verbose_name='Membership Type')
    join_date = models.DateField(auto_now_add=True, verbose_name='Joining Date')
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    profile_pic = models.ImageField(verbose_name="Profile Picture", null=True)

    def get_lending_history(self):
        records_db = apps.get_model('TransactionManager', 'Lend')
        logs = records_db.objects.get(user=self)
        payload = ""
        if len(logs) != 0:
            payload = [val.__dict__ for val in logs]
        else:
            payload = [{}]
        return payload

    # lending_log = ArrayField(JSONField(null=True, blank=True), default=get_lending_log, blank=True, null=True)

    def __str__(self):
        if self.middle_name is not None:
            return "{} {} {}".format(self.first_name, self.middle_name, self.last_name)
        else:
            return "{} {}".format(self.first_name, self.last_name)


class Librarian(models.Model):
    """
    Main Class for the Staff Members
    """
    ROLE_CHOICES = (
        ('pages', 'Pages'),
        ('technician', 'Library Technician'),
        ('librarian', 'Librarian'),
        ('manager', 'Manager'),
        ('director', 'Director'),
    )
    primary_id = models.UUIDField(
            primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(
            max_length=63, help_text='First Name', blank=False, verbose_name='First Name')
    middle_name = models.CharField(
            max_length=63, help_text='Middle Name', null=True, blank=True, default='', verbose_name='Middle Name')
    last_name = models.CharField(
            max_length=63, help_text='Last Name', blank=False, verbose_name='Last Name')
    profile_pic = models.ImageField(verbose_name="Profile Picture", null=True)

    def __str__(self):
        if self.middle_name is not None:
            return "{} {} {}".format(self.first_name, self.middle_name, self.last_name)
        else:
            return "{} {}".format(self.first_name, self.last_name)

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, verbose_name='Role')
    book_recommendations = ArrayField(
            JSONField(blank=True, null=True), blank=True, null=True)
    primary_mobile = INPhoneNumberField(
            help_text='Primary Mobile Number')
    alternate_mobile = INPhoneNumberField(
            help_text='Alternate Mobile Number')
    aadhar_id = INAadhaarNumberField(
            help_text='12 digit Aadhar Number', )
    email_address = models.EmailField(
            help_text='Email Address', blank=False, unique=True, verbose_name='Email Address')
