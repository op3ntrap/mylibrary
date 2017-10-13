# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid
from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField

# Create your models here.
PUBLICATION_TYPE_CHOICES = ()
LANGUAGE_CHOICES = ()
ACCESS_CHOICES = ()
MEMBERSHIP_CHOICES = (
    ('a', 'A'),
    ('b', 'B'),
    ('c', 'C'),
    ('d', 'D'),
    ('all', 'All')
)


class Archives(models.Model):
    """
    Abstract Class: All Library Objects
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(
            max_length=100, help_text="Book Title", null=False, blank=False)
    authors = ArrayField(
            models.CharField(max_length=100, default="Unknown Author")
    )
    publisher = models.CharField(max_length=30, null=True, blank=True)
    published_date = models.DateField(auto_now_add=False)
    publication_type = models.CharField(
            max_length=30, choices=PUBLICATION_TYPE_CHOICES, null=False, blank=False)
    languages = models.CharField(
            max_length=30, choices=LANGUAGE_CHOICES, null=False, blank=False)
    cover = models.ImageField()
    tags = ArrayField(models.CharField(max_length=50, null=True, blank=True))
    is_available = models.BooleanField(default=True)
    lending_log = ArrayField(
            JSONField(blank=True, null=True), blank=True, null=True)
    access = models.BooleanField(default=True)
    accessibility = models.CharField(max_length=10, choices=MEMBERSHIP_CHOICES, default='all')
    identifier = models.CharField(max_length=10, default='isbn')
    id_val = models.CharField(max_length=40, default="s", unique=True)
    penalty = models.FloatField()

    class Meta:
        abstract = True


class DigitalRecords(Archives):
    file_format = models.CharField(max_length=20)
    source_url = models.URLField(null=True, blank=True)


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
# TODO Create this Heirarchy
Class Hierarchy:
    |-->Archives
        |-->Books
            |-->Genre
        |-->Journals
            |-->Subjects
                |-->Year
        |-->Research Papers
            |-->Subject
                |-->Year
        |-->Digital Records
            |-->Format
        |-->Magazines
            |-->Genre
                |-->Publication
                    |-->Date
"""
GENRE_CHOICES = ()
SUBJECT_CHOICES = ()
JOURNAL_TYPE_CHOICES = (
    ('open', 'Open'),
    ('peer', 'Peer-Reviewed'),
    ('scholarly', 'Scholarly Articles')
)
FORMAT_CHOICES = ()

PERIODICITY_CHOICES = ()


class Books(Archives):
    """Books Inherit from Archives"""
    genre = models.CharField(max_length=30, help_text='Book - Genre',
                             null=False, default='Uncategorised', blank=True)


class Magazines(Books):
    periodical_type = models.CharField(
            max_length=39, choices=PERIODICITY_CHOICES)
    archive_editions = ArrayField(models.DateField(), null=True, blank=True)


class Journals(Archives):
    subject = models.CharField(
            max_length=30, choices=SUBJECT_CHOICES, help_text='Subject')
    journal_type = models.CharField(
            max_length=30, choices=JOURNAL_TYPE_CHOICES, help_text='Journal Type', default="Peer-Reviewed")


class ResearchPaper(Journals):
    citations_count = models.IntegerField(default=0)
    citation_sources = ArrayField(models.CharField(
            max_length=30, help_text='Identifier'))
    journals_ctr = models.OneToOneField(
            Journals, on_delete=models.CASCADE, parent_link=True)
