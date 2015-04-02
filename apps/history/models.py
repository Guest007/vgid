# -*- coding: utf-8 -*-
from django.db import models
from core.models import (ParentModel, SimpleAbstract, Image, Gallery,
                         get_file_name)
from events.models import Event
from django.utils.translation import ugettext, ugettext_lazy as _
from datetime import date
from sorl.thumbnail import ImageField


class History(ParentModel):
    """
        main Event model for news and history
    """
    image = ImageField(_("Image"), upload_to=get_file_name, blank=True, null=True)
    section = models.ForeignKey("Section", blank=True)
    is_history = models.BooleanField(u'История', default=False,
                                     help_text=u'История - да, Новости - нет')
    event = models.ForeignKey(Event, blank=True)

    class Meta:
        verbose_name = u'Новость'
        verbose_name_plural = u'Новости'

    def get_absolute_path(self):
        return "/history/{}".format(self.slug)

class Section(SimpleAbstract):

    class Meta:
        verbose_name = u'Раздел'
        verbose_name_plural = u'Разделы'
