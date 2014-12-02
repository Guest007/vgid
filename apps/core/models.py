# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _
from datetime import date


class SimpleAbstract(models.Model):
    """
    Abstract parent for all main records
    """
    title = models.CharField(_("title"), max_length=500, default="")
    slug = models.SlugField(_("slug"))
    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)

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
    # image = models.ImageField(_("Image"))
    gallery = models.ManyToManyField("Galleries", blank=True, null=True,
                                related_name='gallery')
    geo = models.CharField(_('Coordinates'), max_length=50)

    class Meta:
        abstract = True


class Galleries(SimpleAbstract):
    """
    Galleries with description
    Images in separate model
    """
    pass


class Images(models.Model):
    """
    Image storage for all apps
    """
    gallery = models.ForeignKey("Galleries", blank=True, null=True, related_name='in-gallery')
    image = models.ImageField(_("Image"), upload_to=file)
    is_checked = models.BooleanField(_('Checked'), default=False)
    created = models.DateTimeField(auto_now_add=True)

    def file(self, filename):
        url = "%s/%s/%s" % (self.__class__.__name__,
                            date.today().strftime("%Y_%m_%d"),
                            filename)
        return url

    def __unicode__(self):
        return self.title
