# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 20:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('BookManager', '0008_auto_20171026_1617'),
    ]

    operations = [
        migrations.AlterField(
                model_name='book',
                name='identifier',
                field=models.CharField(
                    choices=[('isbn', 'ISBN'), ('asin', 'ASIN'), ('issn', 'ISSN'), ('doi', 'DOI'), ('lccn', 'LCCN'),
                             ('oclc', 'OCLC')], default='isbn',
                    help_text='Select the type of Identifier<br><div class="right-align"><button type="submit" value="Save and add another" class="waves-effect waves-light btn white-text" name="_continue">Autocomplete</button></div>',
                    max_length=10),
        ),
        migrations.AlterField(
                model_name='digitalrecords',
                name='identifier',
                field=models.CharField(
                    choices=[('isbn', 'ISBN'), ('asin', 'ASIN'), ('issn', 'ISSN'), ('doi', 'DOI'), ('lccn', 'LCCN'),
                             ('oclc', 'OCLC')], default='isbn',
                    help_text='Select the type of Identifier<br><div class="right-align"><button type="submit" value="Save and add another" class="waves-effect waves-light btn white-text" name="_continue">Autocomplete</button></div>',
                    max_length=10),
        ),
        migrations.AlterField(
                model_name='journal',
                name='identifier',
                field=models.CharField(
                    choices=[('isbn', 'ISBN'), ('asin', 'ASIN'), ('issn', 'ISSN'), ('doi', 'DOI'), ('lccn', 'LCCN'),
                             ('oclc', 'OCLC')], default='isbn',
                    help_text='Select the type of Identifier<br><div class="right-align"><button type="submit" value="Save and add another" class="waves-effect waves-light btn white-text" name="_continue">Autocomplete</button></div>',
                    max_length=10),
        ),
        migrations.AlterField(
                model_name='magazine',
                name='identifier',
                field=models.CharField(
                    choices=[('isbn', 'ISBN'), ('asin', 'ASIN'), ('issn', 'ISSN'), ('doi', 'DOI'), ('lccn', 'LCCN'),
                             ('oclc', 'OCLC')], default='isbn',
                    help_text='Select the type of Identifier<br><div class="right-align"><button type="submit" value="Save and add another" class="waves-effect waves-light btn white-text" name="_continue">Autocomplete</button></div>',
                    max_length=10),
        ),
        migrations.AlterField(
                model_name='researchpaper',
                name='identifier',
                field=models.CharField(
                    choices=[('isbn', 'ISBN'), ('asin', 'ASIN'), ('issn', 'ISSN'), ('doi', 'DOI'), ('lccn', 'LCCN'),
                             ('oclc', 'OCLC')], default='isbn',
                    help_text='Select the type of Identifier<br><div class="right-align"><button type="submit" value="Save and add another" class="waves-effect waves-light btn white-text" name="_continue">Autocomplete</button></div>',
                    max_length=10),
        ),
    ]
