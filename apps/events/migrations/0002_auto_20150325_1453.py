# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date_end',
            field=models.DateField(null=True, verbose_name='End', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='date_start',
            field=models.DateField(default=datetime.date(2015, 3, 25), verbose_name='Start'),
            preserve_default=True,
        ),
    ]
