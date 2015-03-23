# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museums', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='museum',
            name='distance',
            field=models.DecimalField(decimal_places=2, max_digits=5, blank=True, help_text='\u0420\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u043e\u0442 \u0433\u043e\u0440\u043e\u0434\u0430 \u0432 \u043a\u043c.', null=True, verbose_name='\u0420\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0435'),
            preserve_default=True,
        ),
    ]
