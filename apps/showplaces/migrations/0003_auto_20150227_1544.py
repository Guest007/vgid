# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def nullify(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Place = apps.get_model("showplaces", "Place")
    for place in Place.objects.all():
        place.place_type = None
        place.save()


class Migration(migrations.Migration):

    dependencies = [
        ('showplaces', '0002_place_weight'),
    ]

    operations = [
        migrations.RunPython(nullify),
    ]
