# -*- coding: utf-8 -*-
__author__ = 'guest007'
from django import template

register = template.Library()

@register.inclusion_tag('core/tag.side_menu.html', takes_context=True)
def side_menu(context):
    request = context['request']
    path = request.path.lower()

    return {}
