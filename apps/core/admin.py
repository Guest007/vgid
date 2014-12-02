# -*- coding: utf-8 -*-
from django.contrib import admin
from core.models import Galleries, Images


class ImagesInline(admin.TabularInline):
    model = Images

class GalleriesAdmin(admin.ModelAdmin):
    inlines = [
        ImagesInline,
    ]

admin.site.register(Galleries, GalleriesAdmin)
# admin.site.register(Images)
