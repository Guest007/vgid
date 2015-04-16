# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView


class HomepageView(TemplateView):
    """
    Home page of site
    """

    template_name = 'core/home.html'
