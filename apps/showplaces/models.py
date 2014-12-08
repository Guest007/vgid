# -*- coding: utf-8 -*-
from django.db import models
from core.models import (ParentModel, SimpleAbstract, get_file_name)
# from tours.models import Tour
from django.utils.translation import ugettext, ugettext_lazy as _
from datetime import date
from sorl.thumbnail import ImageField


class Place(ParentModel):
    """
    main ShowPlaces model
    """
    image = ImageField(_("Image"), upload_to=get_file_name, blank=True,
                       null=True)
    distance = models.DecimalField(u'Расстояние', max_digits=5,
                                   decimal_places=2, blank=True, null=True,
                                   help_text=u'Расстояние от города в км.')
    tickets = models.TextField(_("Ticket's cost"), blank=True, default='')
    place_type = models.ForeignKey("PlaceType", blank=True, null=True)
    locality = models.ForeignKey("Locality", blank=True, null=True)
    # tours = models.ManyToManyField(Tour, blank=True, null=True)


class PlaceType(SimpleAbstract):
    """
        Type of showplace
    """
    pass


class Locality(ParentModel):
    """
        Населённый пункт
    """
    pass
