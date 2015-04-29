# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
# from django import forms
# from time import time
from random import randint
import datetime



#define function to rename file
def get_upload_file_name():
        return "%s" % (randint(1000000, 100000000))


class home(models.Model):
    tytul = models.CharField(max_length=60)
    opis = models.CharField(max_length=1024)
    dzielnice = (
        ('Fabryczna', 'Fabryczna'),
        ('Krzyki', 'Krzyki'),
        ('Psie Pole', 'Psie Pole'),
        ('Stare Miasto', 'Stare Miasto'),
        (u'Śródmieście', u'Śródmieście'),
    )
    nazwa_dzielnicy = models.CharField(max_length=12, choices=dzielnice, default='Fabryczna')
    liczba_pokoi= models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(5)], default=1)
    cena = models.FloatField(max_length=8,
                             validators=[MinValueValidator(1), MaxValueValidator(10000000)],
                             default=100000)
    wspolrzedne_dl = models.FloatField(max_length=8,
                                       validators=[MinValueValidator(16.80), MaxValueValidator(17.18)],
                                       default=17.00)
    wspolrzedne_szer = models.FloatField(max_length=8,
                                       validators=[MinValueValidator(51.00), MaxValueValidator(51.21)],
                                       default=51.10)
    zdjecie = models.FileField(upload_to='profile/%Y/%m/%d')



    data_publikacji = models.DateTimeField('Data publikacji')

    def dodany_dzis(self):
        return self.data_publikacji >= timezone.now() - datetime.timedelta(days=1)



