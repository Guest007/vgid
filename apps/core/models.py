# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _
from datetime import date
from sorl.thumbnail import ImageField


def get_file_name(instance, filename):
        print(instance.__class__.__name__, date.today().strftime("%Y_%m_%d"), filename)
        url = "%s/%s/%s" % (instance.__class__.__name__,
                            date.today().strftime("%Y_%m_%d"),
                            filename)
        return url


class SimpleAbstract(models.Model):
    """
    Abstract parent for all main records
    """
    title = models.CharField(_("title"), max_length=500, default="")
    slug = models.SlugField(_("slug"))
    created = models.DateTimeField(_('Created'), auto_now_add=True)
    changed = models.DateTimeField(_('Modified'), auto_now=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.title


class ParentModel(SimpleAbstract):
    """
    Abstract parent for all main records
    """
    is_publish = models.BooleanField(_('Is Published'), default=False)
    description = models.TextField(_("Description"), blank=True, null=True)
    text = models.TextField(_("Text"), blank=True, null=True)
    gallery = models.ManyToManyField("Gallery", blank=True, null=True)
    geo = models.CharField(_('Coordinates'), max_length=50, blank=True, default='')

    class Meta:
        abstract = True


class Gallery(SimpleAbstract):
    """
    Galleries with description
    Images in separate model
    """
    pass


class Image(models.Model):
    """
    Image storage for all apps
    """
    gallery = models.ForeignKey("Gallery", blank=True, null=True)
    image = ImageField(_("Image"), upload_to=get_file_name)
    is_checked = models.BooleanField(_('Checked'), default=False)
    created = models.DateTimeField(_('Created'), auto_now_add=True)

    def __unicode__(self):
        return self.image.url


class Section(SimpleAbstract):
    """
    Описание разделов. Изображения берутся из постов. Или все, или ставить
    там галочки...
    """
    text = models.TextField(_("Text"), blank=True, null=True)
