# -*- coding: utf-8 -*-
from django.contrib import admin
from events.models import Event, Section
from sorl.thumbnail.admin import AdminImageMixin


class EventAdmin(AdminImageMixin, admin.ModelAdmin):
    pass


admin.site.register(Event, EventAdmin)
admin.site.register(Section)
