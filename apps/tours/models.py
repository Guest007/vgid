# -*- coding: utf-8 -*-
from django.db import models
from core.models import (ParentModel, SimpleAbstract, get_file_name)
from showplaces.models import Place
from django.utils.translation import ugettext, ugettext_lazy as _
from sorl.thumbnail import ImageField


class Tour(ParentModel):
    """
    main Tour model
    """
    image = ImageField(_("Image"), upload_to=get_file_name, blank=True,
                       null=True)
    duration = models.CharField(u"Длительность тура", max_length=100,
                                blank=True, default='')
    tour_type = models.ForeignKey("TourType", blank=True, null=True,
                                  help_text=u'для тематического фильтра - '
                                            u'военный, литература, кино, шведы...')
    g_ind = models.ForeignKey("GeoIndicator",
                              help_text=u'Географический признак (город/район)')
    places = models.ManyToManyField(Place, blank=True, null=True,
                                    related_name='tour-place')
    complect = models.ForeignKey("Complectation",
                                 help_text=u'Тип экскурсии - индивидуальная/сборная')
    route = models.URLField(u"Маршрут", blank=True,
                            help_text=u'Место для ссылки на карту с маршрутом')
    # here we need link to rewiews. How? VK and E-Mail...

    class Meta:
        verbose_name = u'"Экскурсия"'
        verbose_name_plural = u'Экскурсии'


class TourType(SimpleAbstract):
    """
        Type of Tour
        для тематического фильтра - военный, литература, кино, шведы...
    """
    class Meta:
        verbose_name = u'Тематический фильтр'
        verbose_name_plural = u'Тематические фильтры'


class GeoIndicator(SimpleAbstract):
    """
        Географический признак (город/район)
    """
    class Meta:
        verbose_name = u'Географический признак'
        verbose_name_plural = u'Географический признак'


class Complectation(SimpleAbstract):
    """
    тип экскурсии - индивидуальная/сборная
    """
    class Meta:
        verbose_name = u'Тип экскурсии'
        verbose_name_plural = u'Типы экскурсий'
