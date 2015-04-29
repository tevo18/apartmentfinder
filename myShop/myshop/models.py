__author__ = 'madzik'
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# from django import forms
# from time import time
from random import randint


def get_upload_file_name():


    return "%s" % (randint(1000000, 100000000))


class supermarket(models.Model):


    tytul = models.CharField(max_length=60)
    opis = models.CharField(max_length=1024)
    dzielnice = (
        ('Fabryczna', 'Fabryczna'),
        ('Krzyki', 'Krzyki'),
        ('Psie Pole', 'Psie Pole'),
        ('Stare Miasto', 'Stare Miasto'),
        ('Srodmiescie', 'Srodmiescie')
    )
    nazwa_dzielnicy = models.CharField(max_length=12, choices=dzielnice, default='Stare Miasto')
    wspolrzedne_dl = models.FloatField(max_length=8,
                                   validators=[MinValueValidator(16.80), MaxValueValidator(17.18)],
                                   default=17.00)
    wspolrzedne_szer = models.FloatField(max_length=8,
                                     validators=[MinValueValidator(51.00), MaxValueValidator(51.21)],
                                     default=51.10)
    zdjecie = models.FileField(upload_to='profile/%Y/%m/%d')

