# -*- coding: utf-8 -*-
from django.contrib import admin
import reversion
from catering.models import Catering, CatType
from sorl.thumbnail.admin import AdminImageMixin


class CateringAdmin(AdminImageMixin, reversion.VersionAdmin):
    pass


admin.site.register(Catering, CateringAdmin)
admin.site.register(CatType)
