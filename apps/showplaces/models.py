# -*- coding: utf-8 -*-
from ckeditor.fields import RichTextField
from django.db import models
from core.models import (ParentModel, SimpleAbstract, get_file_name, Locality)
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
    tickets = RichTextField(_("Ticket's cost"), blank=True, default='')
    place_type = models.ForeignKey("PlaceType", blank=True, null=True)
    locality = models.ForeignKey(Locality, blank=True, null=True)
    weight = models.IntegerField(_(u"Вес"), blank=True, null=True)
    # tours = models.ManyToManyField(Tour, blank=True, null=True)

    class Meta:
        verbose_name = u'Достопримечательность'
        verbose_name_plural = u'Достопримечательности'

    def get_absolute_path(self):
        return "/showplaces/{}".format(self.slug)

    def save(self):
      "Get last value of Weight from database, and increment before save"
      if not self.weight:
          top = Place.objects.order_by('-weight')[0]
          self.weight = top.weight + 1
      super(Place, self).save()


class PlaceType(SimpleAbstract):
    """
        Type of showplace
    """
    class Meta:
        verbose_name = u'Тип достопримечательность'
        verbose_name_plural = u'Тип достопримечательности'
