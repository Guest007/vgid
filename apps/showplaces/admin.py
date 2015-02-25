# -*- coding: utf-8 -*-
from django.contrib import admin
import reversion
from showplaces.models import Place, PlaceType
from sorl.thumbnail.admin import AdminImageMixin


class PlaceAdmin(AdminImageMixin, reversion.VersionAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'is_publish', 'weight')
    list_editable = ('is_publish', 'weight')


class PlaceTypeAdmin(AdminImageMixin, reversion.VersionAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Place, PlaceAdmin)
admin.site.register(PlaceType, PlaceTypeAdmin)
