# -*- coding: utf-8 -*-
from django.contrib import admin
from history.models import History, Section
from sorl.thumbnail.admin import AdminImageMixin


class HistoryAdmin(AdminImageMixin, admin.ModelAdmin):
    pass


admin.site.register(History, HistoryAdmin)
admin.site.register(Section)
