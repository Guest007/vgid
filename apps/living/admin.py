# -*- coding: utf-8 -*-
from django.contrib import admin
import reversion
from living.models import Living, LivingType, Room
from sorl.thumbnail.admin import AdminImageMixin


class LivingAdmin(AdminImageMixin, reversion.VersionAdmin):
    pass


admin.site.register(Living, LivingAdmin)
admin.site.register(LivingType)
admin.site.register(Room)
