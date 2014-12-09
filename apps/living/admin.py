# -*- coding: utf-8 -*-
from django.contrib import admin
import reversion
from living.models import Living, LivingType, Room
from sorl.thumbnail.admin import AdminImageMixin


class LivingAdmin(AdminImageMixin, reversion.VersionAdmin):
    prepopulated_fields = {"slug": ("title",)}


class LivingTypeAdmin(AdminImageMixin, reversion.VersionAdmin):
    prepopulated_fields = {"slug": ("title",)}


class RoomAdmin(AdminImageMixin, reversion.VersionAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Living, LivingAdmin)
admin.site.register(LivingType, LivingTypeAdmin)
admin.site.register(Room, RoomAdmin)
