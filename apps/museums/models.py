# -*- coding: utf-8 -*-
from django.db import models
from core.models import (ParentModel, get_file_name)
from events.models import Event
from django.utils.translation import ugettext, ugettext_lazy as _
from datetime import date
from sorl.thumbnail import ImageField


class Museum(ParentModel):
    """
    main Museum model. Has link to Events
    """
    image = ImageField(_("Image"), upload_to=get_file_name, blank=True,
                       null=True)
    w_hours = models.CharField(_('Working hours'), max_length=100, blank=True,
                               default='')
    tickets = models.TextField(_("Ticket's cost"), blank=True, default='')
    events = models.ManyToManyField(Event, blank=True, null=True)


class Section(SimpleAbstract):
    """
        Раздел. Может иметь связь с другими моделями
    """
