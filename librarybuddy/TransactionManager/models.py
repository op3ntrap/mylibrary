# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid
from django.db import models

# Don't recreate new ids for entry in the database

# TODO when return is processed following things have to be executed
# TODO Calculate Penalty and update it in the database
# TODO Update the availability of the book
"""
Lending Actions:

"""


class Lend(models.Model):
    """
    This class holds all the records of Lending Transactions within the library.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    book = models.ForeignKey('BookManager.Books', on_delete=models.CASCADE, null=True, blank=True)
    client = models.ForeignKey('UserManager.Member', on_delete=models.CASCADE, null=True, blank=True)
    issue_date = models.DateTimeField(auto_now_add=True)
    issuer = models.ForeignKey('UserManager.Librarian', on_delete=models.CASCADE, null=True, blank=True)


class Returning(models.Model):
    """
    This class holds all the records and methods for the Returning Transactions within the library.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    returned_date = models.DateTimeField(auto_now_add=True)
    lend = models.ForeignKey('Lend', on_delete=models.CASCADE, null=True, blank=True)
    issuer = models.ForeignKey('UserManager.Librarian', on_delete=models.CASCADE, null=True, blank=True)
    penalty_charged = models.FloatField()
