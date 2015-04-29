# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('myhouse', '0003_photo_zdjecie'),
    ]

    operations = [
        migrations.DeleteModel(
            name='photo',
        ),
        migrations.AddField(
            model_name='home',
            name='zdjecie',
            field=models.FileField(default=datetime.date(2015, 4, 15), upload_to=b'profile/%Y/%m/%d'),
            preserve_default=False,
        ),
    ]
