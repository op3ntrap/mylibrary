# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import ArrayField,JSONField

# Create your models here.
PUBLICATION_TYPE_CHOICES = ()
LANGUAGE_CHOICES = ()


class Books(models.Model):
    """
    Book Objects
    """
    isbn = models.CharField(max_length=15, help_text="ISBN Identifier of the book")
    asin = models.CharField(max_length=15, help_text="ASIN Identifier of the book")
    title = models.CharField(max_length=100, help_text="Book Title")
    authors = ArrayField(
        models.CharField(max_length=100)
    )
    publisher = models.CharField(max_length=30)
    published_date = models.DateField(auto_now_add=False)
    publication_type = models.CharField(max_length=30, choices=PUBLICATION_TYPE_CHOICES)
    languages = models.CharField(max_length=30, choices=LANGUAGE_CHOICES)
    cover = models.ImageField()
    tags = ArrayField(models.CharField(max_length=50))
    is_available = models.BooleanField(default=True)
    lending_log = ArrayField(JSONField())
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

