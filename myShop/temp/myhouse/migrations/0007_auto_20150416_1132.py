# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('myhouse', '0006_home_tytul'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='cena',
            field=models.FloatField(default=100000, max_length=8, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10000000)]),
        ),
    ]
