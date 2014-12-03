# -*- coding: utf-8 -*-
from django.db import models
from core.models import (ParentModel, SimpleAbstract, Image, Gallery,
                         get_file_name)
from django.utils.translation import ugettext, ugettext_lazy as _
from datetime import date
from sorl.thumbnail import ImageField


class Event(ParentModel):
    """
        main Event model for current news and for past events
    """
    image = ImageField(_("Image"), upload_to=get_file_name, blank=True, null=True)
    section = models.ForeignKey("Section")


class Section(SimpleAbstract):
    pass
