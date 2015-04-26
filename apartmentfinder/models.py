# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from random import randint
import datetime



# #define function to rename file
# def get_upload_file_name():
#         return "%s" % (randint(1000000, 100000000))
#

class Home(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=1024)
    districts = (
        ('Fabryczna', 'Fabryczna'),
        ('Krzyki', 'Krzyki'),
        ('Psie Pole', 'Psie Pole'),
        (u'Śródmieście', u'Śródmieście'),
    )
    district_name = models.CharField(max_length=12, choices=districts, default='Fabryczna')
    rooms_number= models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(5)], default=1)
    price = models.FloatField(max_length=8,
                             validators=[MinValueValidator(1), MaxValueValidator(10000000)],
                             default=100000)
    #szerokosc geograficzna
    latitude = models.FloatField(max_length=8,
                                 validators=[MinValueValidator(51.00), MaxValueValidator(51.21)],
                                 default=51.10)
    #dlugosc
    longitude = models.FloatField(max_length=8,
                                  validators=[MinValueValidator(16.80), MaxValueValidator(17.18)],
                                  default=17.00)

    photo = models.FileField(upload_to='profile/%Y/%m/%d')

    publication_date = models.DateTimeField('Data publikacji')

    def added_today(self):
        return self.publication_date >= timezone.now() - datetime.timedelta(days=1)


class Myhouse(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=1024)
    districts = (
        ('Fabryczna', 'Fabryczna'),
        ('Krzyki', 'Krzyki'),
        ('Psie Pole', 'Psie Pole'),
        (u'Śródmieście', u'Śródmieście'),
    )
    district_name = models.CharField(max_length=12, choices=districts, default='Fabryczna')
    rooms_number= models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(5)], default=1)
    price = models.FloatField(max_length=8,
                             validators=[MinValueValidator(1), MaxValueValidator(10000000)],
                             default=100000)
    #szerokosc geograficzna
    latitude = models.FloatField(max_length=8,
                                 validators=[MinValueValidator(51.00), MaxValueValidator(51.21)],
                                 default=51.10)
    #dlugosc
    longitude = models.FloatField(max_length=8,
                                  validators=[MinValueValidator(16.80), MaxValueValidator(17.18)],
                                  default=17.00)
    photo = models.FileField(upload_to='profile/%Y/%m/%d')

    publication_date = models.DateTimeField('Data publikacji')

