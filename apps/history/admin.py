# -*- coding: utf-8 -*-
from django.contrib import admin
import reversion
from history.models import History, Section
from sorl.thumbnail.admin import AdminImageMixin


class HistoryAdmin(AdminImageMixin, reversion.VersionAdmin):
    prepopulated_fields = {"slug": ("title",)}


class SectionAdmin(AdminImageMixin, reversion.VersionAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(History, HistoryAdmin)
admin.site.register(Section, SectionAdmin)
