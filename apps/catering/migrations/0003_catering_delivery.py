# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catering', '0002_catering_distance'),
    ]

    operations = [
        migrations.AddField(
            model_name='catering',
            name='delivery',
            field=models.BooleanField(default=False, verbose_name='\u0414\u043e\u0441\u0442\u0430\u0432\u043a\u0430'),
            preserve_default=True,
        ),
    ]
