# -*- coding: utf-8 -*-
from django.contrib import admin
from core.models import Gallery, Image
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
        widgets = {
          'image': AdminImageWidget,
        }


class ImagesInline(AdminImageMixin, admin.TabularInline):
    model = Image
    form = ImageForm


class GalleryAdmin(AdminImageMixin, admin.ModelAdmin):
    inlines = [
        ImagesInline,
    ]

admin.site.register(Gallery, GalleryAdmin)
# admin.site.register(Images)
