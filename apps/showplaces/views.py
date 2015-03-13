# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from .models import Place, PlaceType
from endless_pagination.views import AjaxListView


class ShowPlacesList(AjaxListView):
    model = Place
    queryset = Place.objects.filter(is_publish=True).order_by('weight')
    # paginate_by = 8
    template_name = 'showplaces/place_list.html'
    page_template = 'showplaces/place_page.html'
    default_filter_param = 'all'

    def get_queryset(self):
        qs = super(ShowPlacesList, self).get_queryset()
        dist = self.request.GET.get('dist')
        p_type = self.request.GET.get('pt')
        if dist:
            if '-' not in dist:
                if dist == "1":
                    qs = qs.filter(distance__lt=1.00)
                elif dist == "2":
                    qs = qs.filter(distance__gt=1.00, distance__lt=10.01)
                elif dist == "3":
                    qs = qs.filter(distance__gt=10.00, distance__lt=30.01)
                elif dist == "4":
                    qs = qs.filter(distance__gt=30.00, distance__lt=50.01)
                elif dist == "5":
                    qs = qs.filter(distance__gt=50.00, distance__lt=100.01)
                elif dist == "6":
                    qs = qs.filter(distance__gt=100.00)

        if p_type:
            if '-' not in p_type:
                qs = qs.filter(place_type=p_type)

        return qs

    def get_context_data(self, **kwargs):
        context = super(ShowPlacesList, self).get_context_data(**kwargs)
        context['p_types'] = PlaceType.objects.all()

        dist = self.request.GET.get('dist')
        if dist:
            if '-' not in dist:
                context['dist'] = dist

        pt = self.request.GET.get('pt')
        if pt:
            if '-' not in pt:
                context['pt_active'] = PlaceType.objects.get(pk=pt)

        return context


class ShowPlacesDetail(DetailView):
    model = Place
    template_name = 'showplaces/place_detail.html'
