# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid
from django.db import models
from localflavor.in_.forms import INPhoneNumberField, INAadhaarNumberField
from django.contrib.postgres.fields import ArrayField, JSONField


# TODO Class specific functions of User needs to be written
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
            help_text="Amount which is needed to be paid to get a membership in the library", default=100.0)
    validity = models.CharField(
            max_length=10,
            choices=VALIDITY_CHOICES,
            help_text="Validity of the Type of a Membership",
            default='1yr'
    )
    lending_power = models.IntegerField(default=1)
    mode = models.CharField(
            max_length=10, choices=MEMBERSHIP_CHOICES, unique=True, default='c'
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
            max_length=63, help_text='First Name', blank=False)
    middle_name = models.CharField(
            max_length=63, help_text='Middle Name', null=True, blank=True, default='')
    last_name = models.CharField(
            max_length=63, help_text='Last Name', blank=False)
    age = models.IntegerField(help_text='Age of the User eg 18', blank=True)
    occupation = models.CharField(
            max_length=20, choices=OCCUPATION_CHOICES, help_text='Select the Occupation of the User', blank=False)
    primary_mobile = INPhoneNumberField(
            help_text='Primary Mobile Number')
    alternate_mobile = INPhoneNumberField(
            help_text='Alternate Mobile Number')
    aadhar_id = INAadhaarNumberField(
            help_text='12 digit Aadhar Number', )
    email_address = models.EmailField(
            help_text='Email Address', blank=False, unique=True)
    twitter_handle = models.CharField(
            max_length=20, help_text='(optional) Twitter Handle', null="", blank=True)
    membership = models.BooleanField()
    membership_type = models.ForeignKey(
            'Membership', on_delete=models.CASCADE, )
    # membership_type = models.ForeignKey(
    #     'Membership', on_delete=models.CASCADE, default=Membership.objects.get(mode='c').primary_id)

    join_date = models.DateField(auto_now_add=True)
    entry_log = ArrayField(
            models.DateField(auto_now=True))
    lending_log = ArrayField(
            JSONField(blank=True, null=True), blank=True, null=True)


class Librarian(models.Model):
    ROLE_CHOICES = (
        ('pages', 'Pages'),
        ('technician', 'Library Technician'),
        ('librarian', 'Librarian'),
        ('manager', 'Manager'),
        ('director', 'Director'),
    )
    primary_id = models.UUIDField(
            primary_key=True, default=uuid.uuid4, editable=False)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    book_recommendations = ArrayField(
            JSONField(blank=True, null=True), blank=True, null=True)
