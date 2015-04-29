# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import myhouse.models


class Migration(migrations.Migration):

    dependencies = [
        ('myhouse', '0002_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='zdjecie',
            field=models.FileField(default=datetime.date(2015, 4, 13), upload_to=myhouse.models.get_upload_file_name),
            preserve_default=False,
        ),
    ]
