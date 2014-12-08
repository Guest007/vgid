# -*- coding: utf-8 -*-
from django.contrib import admin
from catering.models import Catering, CatType
from sorl.thumbnail.admin import AdminImageMixin


class CateringAdmin(AdminImageMixin, admin.ModelAdmin):
    pass


admin.site.register(Catering, CateringAdmin)
admin.site.register(CatType)
