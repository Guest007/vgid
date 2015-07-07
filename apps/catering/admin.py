# -*- coding: utf-8 -*-
from django.contrib import admin
import reversion
from catering.models import Catering, CatType
from sorl.thumbnail.admin import AdminImageMixin


class CateringAdmin(AdminImageMixin, reversion.VersionAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'is_publish', 'delivery' )
    list_editable = ('is_publish', 'delivery')

class CatTypeAdmin(AdminImageMixin, reversion.VersionAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Catering, CateringAdmin)
admin.site.register(CatType, CatTypeAdmin)
