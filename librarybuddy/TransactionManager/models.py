# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid
from django.utils.deconstruct import deconstructible
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

# @deconstructible
# class DeriveLendRecord(object):
#     path = "students/{0}/{1}{2}"

#     def __init__(object, sub_path):
#         object.sub_path = sub_path

#     def __call__(object, instance, filename):
#         return path.format(instance.user.username, object.sub_path, filename)

# upload_dir = UploadToStudentDir('committee/reports/')


class Transaction(models.Model):
    """
    This is the super class of all the transactions within the library
    """
    primary_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    book = models.ForeignKey(
        'BookManager.Book', on_delete=models.CASCADE, )
    client = models.ForeignKey(
        'UserManager.Member', on_delete=models.CASCADE,)
    issuer = models.ForeignKey(
        'UserManager.Librarian', on_delete=models.CASCADE,)
    issue_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Lend(Transaction):
    """
    This class holds all the records of Lending Transactions within the library.
    """
    lend_membership = models.ForeignKey(
        'UserManager.Membership', on_delete=models.CASCADE, null=True)


class take:
    def derive_lend_record(object):
        return Lend.objects.get(
            client=object.client, book=object.book, issue_date=object.issue_date)


class Returning(models.Model):
    """
    This class holds all the records and methods for the Returning Transactions within the library.
    """
    returned_date = models.DateTimeField(auto_now_add=True)
    lending_record = models.ForeignKey(
        'Lend', on_delete=models.CASCADE, null=True, default=Returning.derive_lend_record)
    penalty_charged = models.FloatField()
