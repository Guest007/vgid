# -*- coding: utf-8 -*-
from django.contrib import admin
import reversion
from events.models import Event, Section
from sorl.thumbnail.admin import AdminImageMixin


class EventAdmin(AdminImageMixin, reversion.VersionAdmin):
    pass


admin.site.register(Event, EventAdmin)
admin.site.register(Section)
