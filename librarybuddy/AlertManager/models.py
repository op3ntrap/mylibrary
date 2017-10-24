# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid
from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.

class EmailAlerts(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subject = models.TextField(verbose_name='Subject', max_length=200, blank=True, null=False, default="Library Alert",
                               help_text="Subject of the email", auto_created=True)

    def default_email_sender():
        return ['op3ntrap@gmail.com']

    sender = ArrayField(models.EmailField(null=True, blank=False), null=False, blank=False,
                        default=default_email_sender, verbose_name='From')
    recipient = ArrayField(models.EmailField(null=True, blank=True), null=True, blank=False,
                           default=default_email_sender, verbose_name='To')
    reply_expected = models.BooleanField(default=False,
                                         help_text='Specify Whether the Recipient can reply to the email.')
    header = models.TextField(default="LibraryBuddy<br>An Easy Way to Manage your Community Library",
                              verbose_name='Header', help_text="Header of the Email")
    footer = models.TextField(default="Yours Faithfully,<br>LibraryBuddy", verbose_name='Signature of the Email',
                              help_text="Signature")
    date = models.DateTimeField(auto_now_add=True, editable=False)
    body = models.TextField(default="Hello There")
    title = models.CharField(default="{}".format(subject), verbose_name="Email Template Reference Title",
                             help_text="Please specify a title for reusing this template in the future", max_length=300)

    def __str__(self):
        return self.title


class EmailClient(models.Model):
    client_name = models.CharField(null='False', blank='True', default="Library Email Client", max_length=60)
