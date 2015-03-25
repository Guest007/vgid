# -*- coding: utf-8 -*-
from django.db import models
from core.models import (ParentModel, SimpleAbstract, Image, Gallery,
                         get_file_name)
from django.utils.translation import ugettext, ugettext_lazy as _
from datetime import date
from sorl.thumbnail import ImageField


class Event(ParentModel):
    """
        main Event model for important events
    """
    image = ImageField(_("Image"), upload_to=get_file_name, blank=True, null=True)
    section = models.ForeignKey("Section", blank=True, null=True)
    date_start = models.DateField(_('Start'), default=date.today())
    date_end = models.DateField(_('End'), blank=True, null=True)

    class Meta:
        verbose_name = u'Событие'
        verbose_name_plural = u'События'

    def get_absolute_path(self):
        return "/events/{}".format(self.slug)


class Section(SimpleAbstract):

    class Meta:
        verbose_name = u'Раздел'
        verbose_name_plural = u'Разделы'

