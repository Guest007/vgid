# -*- coding: utf-8 -*-
__author__ = 'guest007'
from django import template

register = template.Library()

@register.inclusion_tag('showplaces/templatetags/filter.html', takes_context=True)
def showplace_filter(context):
    request = context['request']
    path = request.path.lower()

    return True
