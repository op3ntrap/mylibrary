# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
from django.apps import apps
from django.db import models
import qrcode
from io import StringIO
from django.core.urlresolvers import reverse
from django.core.files.uploadedfile import InMemoryUploadedFile


# TODO when return is processed following things have to be executed
# TODO only issue books which are available.
# TODO Create alert object for returning the book and alert the issuer if the book has not been returned.


class Transaction(models.Model):
    """
    This is the super class of all the transactions within the library
    """
    _id = models.UUIDField(
            primary_key=True, default=uuid.uuid4, editable=False)
    book = models.ForeignKey(
            'BookManager.Book', on_delete=models.CASCADE, )
    client = models.ForeignKey(
            'UserManager.Member', on_delete=models.CASCADE, )
    issuer = models.ForeignKey(
            'UserManager.Librarian', on_delete=models.CASCADE, )
    issue_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return "{} borrowed by {} on {}".format(self.book, self.client, self.issue_date.date())


class Lend(Transaction):
    """
    This class holds all the records of Lending Transactions within the library.
    """
    lend_membership = models.ForeignKey(
            'UserManager.Membership', on_delete=models.CASCADE, null=True)

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

    returning_record = ""

    def save(self, *args, **kwargs):
        returning_record = Returning.objects.create(book_id=self.book._id, client_id=self.client.primary_id,
                                                    issue_date=self.issue_date, issuer_id=self.issuer.primary_id)
        # updating the availability of the book
        book_thread = apps.get_model('BookManager', model_name='Book')
        book_instance = book_thread.objects.get(_id=self.book_id)
        book_instance.is_available = False
        book_instance.save()
        # Creating the return record.
        self.returning_record = models.OneToOneField(Returning, on_delete=models.CASCADE, default=returning_record)
        super(Lend, self).save(*args, **kwargs)  # Call the "real" save() method.


class Returning(Transaction):
    """
        This class holds all the records and methods for the Returning Transactions within the library.
        """
    returned = models.BooleanField(default=False)
    returned_date = models.DateTimeField(auto_now_add=True)
    penalty_charged = models.FloatField(default=0)
