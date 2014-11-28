from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _


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
    gallery = models.ForeignKey("Gallery", blank=True, null=True)

    class Meta:
        abstract = True


class Gallery(models.Model):
    """
    Main gallery for all apps
    """
    image = models.ImageField(_("Image"))
    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)
