# -*- coding: utf-8 -*-
from django.contrib import admin
from museums.models import Museum
from sorl.thumbnail.admin import AdminImageMixin


class MuseumAdmin(AdminImageMixin, admin.ModelAdmin):
    pass


admin.site.register(Museum, MuseumAdmin)