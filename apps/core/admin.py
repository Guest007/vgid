# -*- coding: utf-8 -*-
from django.contrib import admin
import reversion
from core.models import Gallery, Image, Locality, Section
from sorl.thumbnail.admin import AdminImageMixin
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.safestring import mark_safe
from django.forms import ModelForm
from sorl.thumbnail import get_thumbnail


class AdminImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None):
        output = []
        if value and getattr(value, "url", None):
            t = get_thumbnail(value,'80x80')
            output.append('<img src="{}">'.format(t.url))
        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))


class ImageForm(ModelForm):

    class Meta:
        model = Image
        exclude = ['created']
        widgets = {
          'image': AdminImageWidget,
        }


class ImagesInline(AdminImageMixin, admin.TabularInline):
    model = Image
    form = ImageForm


class GalleryAdmin(AdminImageMixin, reversion.VersionAdmin):
    inlines = [
        ImagesInline,
    ]


class LocalityAdmin(AdminImageMixin, reversion.VersionAdmin):
    pass


admin.site.register(Locality, LocalityAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Section)
