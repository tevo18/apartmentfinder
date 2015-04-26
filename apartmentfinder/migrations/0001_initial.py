# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=1024)),
                ('district_name', models.CharField(default=b'Fabryczna', max_length=12, choices=[(b'Fabryczna', b'Fabryczna'), (b'Krzyki', b'Krzyki'), (b'Psie Pole', b'Psie Pole'), ('\u015ar\xf3dmie\u015bcie', '\u015ar\xf3dmie\u015bcie')])),
                ('rooms_number', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('price', models.FloatField(default=100000, max_length=8, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10000000)])),
                ('longitude', models.FloatField(default=17.0, max_length=8, validators=[django.core.validators.MinValueValidator(16.8), django.core.validators.MaxValueValidator(17.18)])),
                ('latitude', models.FloatField(default=51.1, max_length=8, validators=[django.core.validators.MinValueValidator(51.0), django.core.validators.MaxValueValidator(51.21)])),
                ('photo', models.FileField(upload_to=b'profile/%Y/%m/%d')),
                ('publication_date', models.DateTimeField(verbose_name=b'Data publikacji')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Myhouse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=1024)),
                ('district_name', models.CharField(default=b'Fabryczna', max_length=12, choices=[(b'Fabryczna', b'Fabryczna'), (b'Krzyki', b'Krzyki'), (b'Psie Pole', b'Psie Pole'), ('\u015ar\xf3dmie\u015bcie', '\u015ar\xf3dmie\u015bcie')])),
                ('rooms_number', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('price', models.FloatField(default=100000, max_length=8, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10000000)])),
                ('longitude', models.FloatField(default=17.0, max_length=8, validators=[django.core.validators.MinValueValidator(16.8), django.core.validators.MaxValueValidator(17.18)])),
                ('latitude', models.FloatField(default=51.1, max_length=8, validators=[django.core.validators.MinValueValidator(51.0), django.core.validators.MaxValueValidator(51.21)])),
                ('photo', models.FileField(upload_to=b'profile/%Y/%m/%d')),
                ('publication_date', models.DateTimeField(verbose_name=b'Data publikacji')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
