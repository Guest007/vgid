# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from feedback.views import callback, excurs, feedback


urlpatterns = patterns('',
    url(r'^callback/$', callback, name='callback'),
    url(r'^excurs/$', excurs, name='excurs'),
    url(r'^feedback/$', feedback, name='feedback'),
    )
