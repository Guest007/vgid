# -*- coding: utf-8 -*-
from django.contrib import admin
from living.models import Living, LivingType
from sorl.thumbnail.admin import AdminImageMixin


class LivingAdmin(AdminImageMixin, admin.ModelAdmin):
    pass


admin.site.register(Living, LivingAdmin)
admin.site.register(LivingType)
