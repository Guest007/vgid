# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20150325_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='section',
            field=models.ForeignKey(blank=True, to='events.Section', null=True),
            preserve_default=True,
        ),
    ]
