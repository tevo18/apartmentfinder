# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myhouse', '0007_auto_20150416_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='nazwa_dzielnicy',
            field=models.CharField(default=b'Fabryczna', max_length=12, choices=[(b'Fabryczna', b'Fabryczna'), (b'Krzyki', b'Krzyki'), (b'Psie Pole', b'Psie Pole'), (b'Stare Miasto', b'Stare Miasto'), ('\u015ar\xf3dmie\u015bcie', '\u015ar\xf3dmie\u015bcie')]),
        ),
    ]
