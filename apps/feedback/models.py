# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _
from datetime import date

FEEDBACK_TYPE = [
            ('callback', _("Заказ звонка")),
            ('tour', _("Approved")),
            ('feedback', _("Declined")),
            ('reservation', _("Declined")),
        ]

# class Feedback(models.Model):
#     type = models.CharField(_("Источник отзыва"), max_length=32,
#         choices=FEEDBACK_TYPE, default='callback')
#
#     name = models.CharField(u"Имя", max_length=500, default="")
#     slug = models.SlugField(_("slug"))
#     email = models.CharField(u"E-Mail", max_length=100, default="")
#     phone = models.CharField(u"Телефон", max_length=100, default="")
#
#     created = models.DateTimeField(_('Created'), auto_now_add=True)
#     changed = models.DateTimeField(_('Modified'), auto_now=True)
#
#     def __unicode__(self):
#         return self.name


"""
callback
--------
name
email
phone

tour
----
name
email
phone

feedback
--------
name
email
phone
text



"""