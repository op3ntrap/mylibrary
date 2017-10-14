# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid
from django.db import models
from localflavor.in_.forms import INPhoneNumberField, INAadhaarNumberField
from django.contrib.postgres.fields import ArrayField, JSONField


# TODO Class specific functions of User needs to be written
# TODO custom permissions need to be set up on each classes.
# TODO verbose_names of user_input processing Fields needs to be written.


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
    age = models.IntegerField(help_text='Age of the User eg 18', blank=True, verbose_name='Age')
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
    membership = models.BooleanField(verbose_name='Is a Member?')
    membership_type = models.ForeignKey(
            'Membership', on_delete=models.CASCADE, null=True,
            verbose_name='Membership Type')
    join_date = models.DateField(auto_now_add=True, verbose_name='Joining Date')
    entry_log = ArrayField(
            models.DateField(auto_now=True))
    lending_log = ArrayField(
            JSONField(blank=True, null=True), blank=True, null=True)


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
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, verbose_name='Role')
    book_recommendations = ArrayField(
            JSONField(blank=True, null=True), blank=True, null=True)
