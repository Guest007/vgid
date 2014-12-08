# -*- coding: utf-8 -*-
from django.contrib import admin
from showplaces.models import Place, PlaceType
from sorl.thumbnail.admin import AdminImageMixin


class PlaceAdmin(AdminImageMixin, admin.ModelAdmin):
    pass


admin.site.register(Place, PlaceAdmin)
admin.site.register(PlaceType)
