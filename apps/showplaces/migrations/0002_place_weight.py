# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('showplaces', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='weight',
            field=models.IntegerField(null=True, verbose_name='\u0412\u0435\u0441', blank=True),
            preserve_default=True,
        ),
    ]
