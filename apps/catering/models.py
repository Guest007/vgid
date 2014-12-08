# -*- coding: utf-8 -*-
from django.db import models
from core.models import (ParentModel, SimpleAbstract, get_file_name)
from django.utils.translation import ugettext, ugettext_lazy as _
from sorl.thumbnail import ImageField


class CatType(SimpleAbstract):
    """
        Тип заведения
    """
    class Meta:
        verbose_name = u'Тип заведения'
        verbose_name_plural = u'Типы заведений'


class Catering(ParentModel):
    """
    Питание
    """
    type_of_catering = models.ForeignKey(CatType, help_text=u'Тип заведения')
    image = ImageField(_("Image"), upload_to=get_file_name, blank=True,
                       null=True)
    address = models.CharField(u'Адрес', max_length=200)

    class Meta:
        verbose_name = u'Питание'
        verbose_name_plural = u'Точки общепита'

