# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('showplaces', '0004_remove_place_place_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='place_type',
            field=models.ManyToManyField(to='showplaces.PlaceType', null=True, blank=True),
            preserve_default=True,
        ),
    ]
