# -*- coding: utf-8 -*-
from django.contrib import admin
import reversion
from history.models import History, Section
from sorl.thumbnail.admin import AdminImageMixin


class HistoryAdmin(AdminImageMixin, reversion.VersionAdmin):
    pass


admin.site.register(History, HistoryAdmin)
admin.site.register(Section)
