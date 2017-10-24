# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid
from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField
from languages.fields import LanguageField


def archive_url_json():
    urls = {
        'libgen'      : "",
        'google_books': ""
    }
    return urls


class Archive(models.Model):
    """
    Abstract Class: All Library Objects
    from django.utils.html import format_html
    def colored_name(self):
        return format_html(
        '<span style="color: #{};">{} {}</span>',
        self.color_code,
        self.first_name,
        self.last_name,
        )
    """
    # Field Choice Tuples
    MEMBERSHIP_CHOICES = (
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
        ('d', 'D'),
    )
    IDENTIFIER_CHOICES = (
        ('isbn', 'ISBN'),
        ('asin', 'ASIN'),
        ('issn', 'ISSN'),
        ('doi', 'DOI'),
        ('lccn', 'LCCN'),
        ('oclc', 'OCLC')
    )

    def __str__(self):
        return "{} by {}".format(self.title, self.authors)

    # Internal Reference
    _id = models.UUIDField(
            primary_key=True, default=uuid.uuid4, editable=False)
    last_modified_on = models.DateTimeField(auto_now=True, auto_created=True)

    lending_log = ArrayField(
            JSONField(null=True, editable=False),
            blank=True, null=True, editable=False)
    # MetaData Fields
    title = models.CharField(
            max_length=100, help_text="Book Title", null=False, blank=False)
    authors = models.TextField(max_length=100,
                               default="Unknown Author",
                               help_text='Enter the Author names separated by a comma: <br>Eg. good,bad <br>For Tags '
                                         'which contain spaces can be entered by surrounding them with double quotes. '
                                         '<br>Eg."Risan Raja"')
    publisher = models.CharField(max_length=30, null=True, blank=True)
    published_date = models.DateField(auto_now_add=False, null=True, blank=True, editable=False)
    cover = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    tags = models.CharField(max_length=50, null=True, blank=True,
                      help_text='Enter the relevant Tags separated by a comma: <br>Eg. good,bad <br>For Tags which '
                                'contain spaces can be entered by surrounding them with double quotes. <br>Eg."Machine '
                                'Learning"')
    page_count = models.IntegerField(null=True, blank=True)
    # Universal Identification
    identifier = models.CharField(
            max_length=10, choices=IDENTIFIER_CHOICES, default='isbn', help_text='Select the type of Identifier')
    identifier_value = models.CharField(max_length=13, default="654656", unique=True,
                                        help_text='Please enter the Identifier Code')
    # Access Control Parameters
    is_available = models.BooleanField(default=True, editable=False)
    access = models.BooleanField(default=True)
    accessibility = models.CharField(
            max_length=10, choices=MEMBERSHIP_CHOICES, default='d', help_text='Membership Level Required')
    # Others
    penalty = models.FloatField(default=100)
    urls = JSONField(default=archive_url_json)
    copies = models.IntegerField(default=1, editable=False, verbose_name='Number of Copies')

    class Meta:
        abstract = True
        unique_together = ['identifier', 'identifier_value']
        ordering = ['title', '-published_date']

    permissions = (('modify_access', 'Modify Access'), ('access_lending_logs', 'Access the Lending Logs'))


class DigitalRecords(Archive):
    file_format = models.CharField(max_length=20)
    source_url = models.URLField(null=True, blank=True)


class Book(Archive):
    """Books Inherit from Archive"""
    GENRE_CHOICES = ()
    genre = models.CharField(max_length=30, help_text='Book - Genre',
                             null=False, default='Uncategorised', blank=True)


class Magazine(Archive):
    PERIODICITY_CHOICES = (
        ('yearly', 'Yearly'),
        ('monthly', 'Monthly'),
        ('fortnightly', 'Fortnightly'),
        ('weekly', 'Weekly'),
        ('daily', 'Daily')
    )
    periodical_type = models.CharField(
            max_length=39, choices=PERIODICITY_CHOICES, help_text='Periodicity of the Magazine')
    archive_editions = ArrayField(models.DateField(help_text='enter date in YYYY-MM-DD'), null=True, blank=True,
                                  help_text='enter date in YYYY-MM-DD')


class Journal(Archive):
    JOURNAL_TYPE_CHOICES = (
        ('open', 'Open'),
        ('peer', 'Peer-Reviewed'),
        ('scholarly', 'Scholarly Articles')
    )
    SUBJECT_CHOICES = ()
    subject = models.CharField(
            max_length=30, choices=SUBJECT_CHOICES, help_text='Subject')
    journal_type = models.CharField(
            max_length=30, choices=JOURNAL_TYPE_CHOICES, help_text='Journal Type', default="Peer-Reviewed")


class ResearchPaper(Archive):
    citations_count = models.IntegerField(default=0)
    citation_sources = ArrayField(models.CharField(
            max_length=30, help_text='Identifier'))
    journal = models.ForeignKey(
            'Journal', on_delete=models.CASCADE, null=True)
