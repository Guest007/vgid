# -*- coding: utf-8 -*-
from django.contrib import admin
import reversion
from tours.models import Tour, TourType, GeoIndicator, Complectation
from sorl.thumbnail.admin import AdminImageMixin


class TourAdmin(AdminImageMixin, reversion.VersionAdmin):
    pass


admin.site.register(Tour, TourAdmin)
admin.site.register(TourType)
admin.site.register(GeoIndicator)
admin.site.register(Complectation)
