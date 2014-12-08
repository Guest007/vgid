# -*- coding: utf-8 -*-
from django.contrib import admin
from leisure.models import Leisure, Section
from sorl.thumbnail.admin import AdminImageMixin


class LeisureAdmin(AdminImageMixin, admin.ModelAdmin):
    pass


admin.site.register(Leisure, LeisureAdmin)
admin.site.register(Section)
