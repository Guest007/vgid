# -*- coding: utf-8 -*-
from django.contrib import admin
import reversion
from museums.models import Museum
from sorl.thumbnail.admin import AdminImageMixin


class MuseumAdmin(AdminImageMixin, reversion.VersionAdmin):
    pass


admin.site.register(Museum, MuseumAdmin)