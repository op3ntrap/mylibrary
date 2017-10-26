# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
import uuid
from django.apps import apps
from django.db import models
from django.core import validators


# import qrcode
# from io import StringIO
# from django.core.urlresolvers import reverse
# from django.core.files.uploadedfile import InMemoryUploadedFile


# TODO when return is processed following things have to be executed
# TODO Create alert object for returning the book and alert the issuer if the book has not been returned.


class Transaction(models.Model):
    """
    This is the super class of all the transactions within the library
    """
    _id = models.UUIDField(
            primary_key=True, default=uuid.uuid4, editable=False)
    archive = models.ForeignKey(
            'BookManager.Book', on_delete=models.CASCADE, )
    client = models.ForeignKey(
            'UserManager.Member', on_delete=models.CASCADE, )
    issuer = models.ForeignKey(
            'UserManager.Librarian', on_delete=models.CASCADE, )
    from datetime import datetime
    issue_date = models.DateTimeField(default=datetime.now)

    class Meta:
        abstract = True

    def __str__(self):
        return "{} borrowed by {} on {}".format(self.archive, self.client, self.issue_date.date())


class Returning(Transaction):
    """
        This class holds all the records and methods for the Returning Transactions within the library.
        """

    returned = models.BooleanField(default=False)

    returned_date = models.DateTimeField(null=True)
    penalty_charged = models.FloatField(default=0)

    def save(self, *args, **kwargs):
        if self.returned is True and self.returned_date is None:
            book_thread = apps.get_model('BookManager', model_name='Book')
            book_instance = book_thread.objects.get(_id=self.archive_id)
            book_instance.is_available = True
            book_instance.save()
            self.returned_date = datetime.datetime.now()

        super(Returning, self).save(*args, **kwargs)

    def __str__(self):
        return "{} returned by {} on {}".format(self.archive, self.client, self.issue_date.date())


class Lend(Transaction):
    """
    This class holds all the records of Lending Transactions within the library.
    """

    # qrcode = models.ImageField(upload_to='qrcode', blank=True, null=True)
    #
    # def get_absolute_url(self):
    #     return reverse('Lend.views.details', args=[str(self.id)])

    # def generate_qrcode(self):
    #     qr = qrcode.QRCode(
    #             version=1,
    #             error_correction=qrcode.constants.ERROR_CORRECT_L,
    #             box_size=6,
    #             border=0,
    #     )
    #     qr.add_data(self.get_absolute_url())
    #     qr.make(fit=True)
    #
    #     img = qr.make_image()
    #
    #     buffer = StringIO()
    #     img.save(buffer)
    #     filename = 'events-%s.png' % (self.id)
    #     filebuffer = InMemoryUploadedFile(
    #             buffer, None, filename, 'image/png', buffer, None)
    #     self.qrcode.save(filename, filebuffer)

    def update_lending_log(self, book):
        lending_log = book.lending_log
        payload = self.__dict__
        for key in payload.keys():
            if key[0] == '_':
                # noinspection PyUnusedLocal
                garbage = payload.pop(key)
        lending_log.append(payload)

    returning_record = models.OneToOneField(Returning, on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        # Creating the return record.
        if self.returning_record is None:
            return_record = Returning.objects.create(archive_id=self.archive._id, client_id=self.client.primary_id,
                                                    issue_date=self.issue_date, issuer_id=self.issuer.primary_id)
        self.returning_record = return_record
        # updating the availability of the book
        book_thread = apps.get_model('BookManager', model_name='Book')
        book_instance = book_thread.objects.get(_id=self.archive_id)
        if book_instance.is_available is True:
            book_instance.is_available = False
        book_instance.save()
        super(Lend, self).save(*args, **kwargs)  # Call the "real" save() method.