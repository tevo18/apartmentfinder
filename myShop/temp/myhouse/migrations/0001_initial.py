# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='home',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nazwa_dzielnicy', models.CharField(default=b'Fabryczna', max_length=12, choices=[(b'Fabryczna', b'Fabryczna'), (b'Krzyki', b'Krzyki'), (b'Psie Pole', b'Psie Pole'), ('\u015ar\xf3dmie\u015bcie', '\u015ar\xf3dmie\u015bcie')])),
                ('liczba_pokoi', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('cena', models.FloatField(default=1, max_length=8, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('wspolrzedne_dl', models.FloatField(default=17.0, max_length=8, validators=[django.core.validators.MinValueValidator(16.8), django.core.validators.MaxValueValidator(17.18)])),
                ('wspolrzedne_szer', models.FloatField(default=51.1, max_length=8, validators=[django.core.validators.MinValueValidator(51.0), django.core.validators.MaxValueValidator(51.21)])),
                ('data_publikacji', models.DateTimeField(verbose_name=b'Data publikacji')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
