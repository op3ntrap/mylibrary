# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid
from django.db import models
from BookManager.models import Book
from UserManager.models import Member, Membership, Librarian


"""
# Don't recreate new ids for entry in the database

# TODO when return is processed following things have to be executed
# TODO Calculate Penalty and update it in the database
# TODO Update the availability of the book

Lending Actions:

"""


class Transaction(models.Model):
    """
    This is the super class of all the transactions within the library
    """
    primary_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    book = models.ForeignKey(
        'Book', on_delete=models.CASCADE, null=False, default=Book.objects.get(title='Test Book(Application)').primary_id)
    client = models.ForeignKey(
        'Member', on_delete=models.CASCADE, null=False, default=Member.objects.get(email_address='op3ntrap@gmail.com').primary_id)
    issuer = models.ForeignKey(
        'Librarian', on_delete=models.CASCADE, null=False, default=Librarian.objects.get(email_address='op3ntrap@gmail.com').primary_id)


class Lend(Transaction):
    """
    This class holds all the records of Lending Transactions within the library.
    """
    issue_date = models.DateTimeField(auto_now_add=True)


class Returning(models.Model):
    """
    This class holds all the records and methods for the Returning Transactions within the library.
    """
    returned_date = models.DateTimeField(auto_now_add=True)
    lending_record = models.ForeignKey(
        'Lend', on_delete=models.CASCADE, null=True)
    penalty_charged = models.FloatField()
