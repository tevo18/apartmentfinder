# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('myhouse', '0004_auto_20150415_0756'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='opis',
            field=models.CharField(default=datetime.date(2015, 4, 15), max_length=1024),
            preserve_default=False,
        ),
    ]
