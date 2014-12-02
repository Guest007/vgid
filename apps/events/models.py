# -*- coding: utf-8 -*-
from django.db import models
from core.models import ParentModel, SimpleAbstract, Images, Galleries
from django.utils.translation import ugettext, ugettext_lazy as _


class Events(ParentModel):
    """
    main Event model for current news and for past events
    """
    image = models.ForeignKey(Images, blank=True, null=True)
    section = models.ForeignKey("Section")


class Section(SimpleAbstract):
    pass
