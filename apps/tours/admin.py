# -*- coding: utf-8 -*-
from django.contrib import admin
from tours.models import Tour, TourType
from sorl.thumbnail.admin import AdminImageMixin


class TourAdmin(AdminImageMixin, admin.ModelAdmin):
    pass


admin.site.register(Tour, TourAdmin)
admin.site.register(TourType)
