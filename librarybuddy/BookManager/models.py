# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid

import requests
from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField
from .extract import Extractor
from dateutil import parser


def archive_url_json():
	urls = {
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
	lending_log = ArrayField(
			JSONField(null=True, editable=False),
			blank=True, null=True, editable=False)
	last_modified_on = models.DateTimeField(auto_now=True, auto_created=True)
	# Universal Identification
	identifier = models.CharField(
			max_length=10, choices=IDENTIFIER_CHOICES, default='isbn',
			help_text='Select the type of Identifier<br><div class="right-align"><button type="submit" value="Save and '
			          'add another" class="waves-effect waves-light btn white-text" name="_continue">Autocomplete</button></div>')
	identifier_value = models.CharField(max_length=13, default="654656", unique=True,
	                                    help_text='Please enter the Identifier Code')
	autocomplete_using_isbn = models.BooleanField(default=True, verbose_name="AutoComplete Using ISBN",
	                                              help_text="Check this box to autocomplete the book data using ISBN")

	# MetaData Fields
	title = models.CharField(
			max_length=100, help_text="Book Title", null=False, blank=True, )
	authors = models.CharField(max_length=255,
	                           default="Unknown Author",
	                           help_text='Enter the Author names separated by a comma: <br>Eg. good,bad ')
	publisher = models.CharField(max_length=255, null=True, blank=True)
	published_date = models.DateField(auto_now_add=False, null=True, blank=True, editable=True)
	cover = models.ImageField(null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	tags = models.CharField(max_length=255, null=True, blank=True,
	                        help_text='Enter the relevant Tags separated by a comma: <br>Eg. good,bad <br>For Tags which '
	                                  'contain spaces can be entered by surrounding them with double quotes. <br>Eg."Machine '
	                                  'Learning"')
	page_count = models.IntegerField(null=True, blank=True)
	# Access Control Parameters
	is_available = models.BooleanField(default=True, )
	access = models.BooleanField(default=True)
	accessibility = models.ForeignKey('UserManager.Membership', on_delete=models.CASCADE,
	                                  help_text='Membership Level Required', null=True, blank=True)
	# Others
	penalty = models.FloatField(default=100)
	urls = models.URLField(null=True, blank=True)
	copies = models.IntegerField(default=1, editable=True, verbose_name='Number of Copies')

	class Meta:
		abstract = True
		unique_together = ['identifier', 'identifier_value']
		ordering = ['title', '-published_date']

	permissions = (('modify_access', 'Modify Access'), ('access_lending_logs', 'Access the Lending Logs'))


class DigitalRecords(Archive):
	"""
	All library objects which are stored and maintained in digital formats
	"""
	file_format = models.CharField(max_length=20)
	source_url = models.URLField(null=True, blank=True)


class Book(Archive):
	"""Books Inherit from Archive"""
	GENRE_CHOICES = [('Science', 'Science'),
	                 ('fiction', 'fiction'),
	                 ('Satire', 'Satire'),
	                 ('Drama', 'Drama'),
	                 ('Action', 'Action'),
	                 ('Adventure', 'Adventure'),
	                 ('Romance', 'Romance'),
	                 ('Mystery', 'Mystery'),
	                 ('Horror', 'Horror'),
	                 ('Selfhelp', 'Selfhelp'),
	                 ('Health', 'Health'),
	                 ('Guide', 'Guide'),
	                 ('Travel', 'Travel'),
	                 ('Children', 'Children'),
	                 ('Religion', 'Religion'),
	                 ('Spirituality & New', 'Spirituality & New'),
	                 ('Science', 'Science'),
	                 ('History', 'History'),
	                 ('Math', 'Math'),
	                 ('Anthology', 'Anthology'),
	                 ('Poetry', 'Poetry'),
	                 ('Encyclopedias', 'Encyclopedias'),
	                 ('Dictionaries', 'Dictionaries'),
	                 ('Comics', 'Comics'),
	                 ('Art', 'Art'),
	                 ('Cookbooks', 'Cookbooks'),
	                 ('Diaries', 'Diaries'),
	                 ('Journals', 'Journals'),
	                 ('Prayer', 'Prayer'),
	                 ('Series', 'Series'),
	                 ('Trilogy', 'Trilogy'),
	                 ('Biographies', 'Biographies'),
	                 ('Autobiographies', 'Autobiographies'),
	                 ('Fantasy', 'Fantasy'),
	                 ]
	genre = models.CharField(max_length=30, choices=GENRE_CHOICES, help_text='Book - Genre',
	                         null=False, default='Science', blank=True)

	def extract_metadata(self):
		if self.identifier_value is not None and len(self.identifier_value) in [13, 10]:
			payload_data = Extractor(self.identifier, self.identifier_value)
			payload = payload_data.metadata()
			if payload == 0:
				return
			else:
				self.urls = payload['google_url']
				self.description = payload['description']
				self.tags = payload['tags']
				cover = requests.get(payload['cover'])
				cover_format = cover.headers['Content-Type'].split('/')[1]
				with open('covers/' + self.identifier_value + '.' + cover_format, 'wb+') as cover_file:
					cover_file.write(cover.content)
				self.cover = self.identifier_value + '.' + cover_format
				self.published_date = payload['published_date']
				self.publisher = payload['publisher']
				self.authors = payload['authors']
				self.page_count = payload['page_count']
				self.title = payload['title']
		else:
			return 0

	def generate_qr_code(self, embedded_data, fp):
		"""
		Generate QrCode using the python QRCode Library and save it in the media folders
		:param rg:
		:param fp:
		:return:
		"""
		import qrcode
		qr = qrcode.QRCode(
				version=1,
				error_correction=qrcode.constants.ERROR_CORRECT_L,
				box_size=10,
				border=4,
		)
		qr.add_data(embedded_data, optimize=20)
		qr.make()
		img = qr.make_image(fill_color="white", back_color="indigo")
		img.save(stream=fp + '_qr_code.png', format='png')

	def save(self, *args, **kwargs):
		if self.autocomplete_using_isbn is True:
			self.extract_metadata()
		if self.identifier_value != None:
			self.generate_qr_code(self.identifier_value, 'covers/' + self.identifier_value)
		super(Book, self).save(*args, **kwargs)


class Magazine(Archive):
	"""
	Periodicals subscribed by the library.
	"""
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
	"""
	Scientific Journals within the possession of the library. Default identifier is the DOI string.
	"""
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
	"""
	Research Papers or Research Articles are scientific publications individually published or published in a subscribed, scientific journal.
	"""
	citations_count = models.IntegerField(default=0)
	citation_sources = ArrayField(models.CharField(
			max_length=30, help_text='Identifier'))
	journal = models.ForeignKey(
			'Journal', on_delete=models.CASCADE, null=True)
