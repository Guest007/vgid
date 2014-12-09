# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _
from datetime import date
from sorl.thumbnail import ImageField
from ckeditor.fields import RichTextField


def get_file_name(instance, filename):
        url = "%s/%s/%s" % (instance.__class__.__name__,
                            date.today().strftime("%Y_%m_%d"),
                            filename)
        return url


class SimpleAbstract(models.Model):
    """
    Abstract parent for all main records
    """
    title = models.CharField(u"Заголовок", max_length=500, default="")
    slug = models.SlugField(_("slug"))
    created = models.DateTimeField(_('Created'), auto_now_add=True)
    changed = models.DateTimeField(_('Modified'), auto_now=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.title


class ParentModel(SimpleAbstract):
    """
    Abstract parent for all main records
    """
    is_publish = models.BooleanField(u'Опубликовано?', default=False)
    description = RichTextField(u"Описание", blank=True, null=True)
    text = RichTextField(u"Текст", blank=True, null=True)
    gallery = models.ManyToManyField("Gallery", blank=True, null=True)
    geo = models.CharField(u'Координаты', max_length=50, blank=True, default='',
                           help_text=u'Координаты для показа на карте')

    meta_title = models.CharField(u'Мета-заголовок', max_length=80, blank=True,
                                  help_text=u'meta tag title не длиннее 80 символов')
    meta_description = models.CharField(u'Мета-описание', max_length=200, blank=True,
                                        help_text=u'meta tag description не длиннее 200 символов')
    meta_keyword = models.CharField(u'Ключевые слова', max_length=250, blank=True,
                                    help_text=u'meta tag keyword не длиннее 250 символов')

    class Meta:
        abstract = True


class Gallery(SimpleAbstract):
    """
    Galleries with description
    Images in separate model
    """
    class Meta:
        verbose_name = u'Галерея'
        verbose_name_plural = u'Галереи'


class Image(models.Model):
    """
    Image storage for all apps
    """
    gallery = models.ForeignKey("Gallery", blank=True, null=True)
    image = ImageField(_("Image"), upload_to=get_file_name)
    is_checked = models.BooleanField(_('Checked'), default=False)
    created = models.DateTimeField(_('Created'), auto_now_add=True)

    def __unicode__(self):
        return self.image.url


class Section(SimpleAbstract):
    """
    Описание разделов. Изображения берутся из постов. Или все, или ставить
    там галочки...
    """
    text = RichTextField(_("Text"), blank=True, null=True,
                            help_text=u'Описание раздела')

    class Meta:
        verbose_name = u'Раздел сайта'
        verbose_name_plural = u'Разделы сайта'


class Locality(ParentModel):
    """
        Населённый пункт
    """
    class Meta:
        verbose_name = u'Населённый пункт'
        verbose_name_plural = u'Населённые пункты'
