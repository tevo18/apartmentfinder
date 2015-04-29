# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('myhouse', '0005_home_opis'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='tytul',
            field=models.CharField(default=datetime.date(2015, 4, 16), max_length=60),
            preserve_default=False,
        ),
    ]
