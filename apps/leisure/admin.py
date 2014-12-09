# -*- coding: utf-8 -*-
from django.contrib import admin
import reversion
from leisure.models import Leisure, Section
from sorl.thumbnail.admin import AdminImageMixin


class LeisureAdmin(AdminImageMixin, reversion.VersionAdmin):
    pass


admin.site.register(Leisure, LeisureAdmin)
admin.site.register(Section)
