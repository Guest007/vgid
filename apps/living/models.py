# -*- coding: utf-8 -*-
from django.db import models
from core.models import (ParentModel, SimpleAbstract, get_file_name)
from django.utils.translation import ugettext, ugettext_lazy as _
from sorl.thumbnail import ImageField


class LivingType(SimpleAbstract):
    """
        Вид проживания
        гостиница, коттедж, квартира
    """
    pass


class Living(ParentModel):
    """
    Проживание
    Ещё должны быть реализованы:
        - Рейтинг
        - Заказ (СМС? ЕМАЙЛ?)
        - Заказать звонок
        - Похожие
        - Форма бронирования
            * ФИО
            * Дата заезда
            * дата отъезда
            * тип номера
            * тел./почта
            * часы звонка (для подтверждения)
            * доп. пожелания
    """
    type_of_living = models.ForeignKey(LivingType, help_text=u'Вид проживания')
    image = ImageField(_("Image"), upload_to=get_file_name, blank=True,
                       null=True)
    distance = models.DecimalField(u'Расстояние', max_digits=5,
                                   decimal_places=2, blank=True, null=True,
                                   help_text=u'Расстояние от города в км.')
    address = models.CharField(u'Адрес', max_length=200)
    category = models.CharField(u'Классность', max_length=100)
    service = models.TextField(u'', blank=True, help_text=u'Доп. услуги')


class Room(ParentModel):
    """
    Виды номеров
    """
    living = models.ForeignKey(Living)

