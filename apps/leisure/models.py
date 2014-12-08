# -*- coding: utf-8 -*-
from django.db import models
from core.models import (ParentModel, SimpleAbstract, Image, Gallery,
                         get_file_name)
from events.models import Event
from django.utils.translation import ugettext, ugettext_lazy as _
from datetime import date
from sorl.thumbnail import ImageField


class Leisure(ParentModel):
    """
        Досуг
    """
    image = ImageField(_("Image"), upload_to=get_file_name, blank=True, null=True)
    section = models.ForeignKey("Section", blank=True)
    distance = models.DecimalField(u'Расстояние', max_digits=5,
                                   decimal_places=2, blank=True, null=True,
                                   help_text=u'Расстояние от города в км.')

    class Meta:
        verbose_name = u'Объект досуга'
        verbose_name_plural = u'Объекты досуга'


class Section(SimpleAbstract):
    image = ImageField(_("Image"), upload_to=get_file_name, blank=True, null=True)

    class Meta:
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'
