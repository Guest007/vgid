# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from .models import Event, Section
from endless_pagination.views import AjaxListView


class EventsList(AjaxListView):
    model = Event
    # queryset = Event.objects.filter(is_publish=True)
    queryset = Event.objects.all()
    # paginate_by = 8
    template_name = 'events/events_list.html'
    page_template = 'events/events_page.html'
    default_filter_param = 'all'

    def get_queryset(self):
        qs = super(EventsList, self).get_queryset()
        dist = self.request.GET.get('dist')
        p_type = self.request.GET.get('type')
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
                else:
                    qs = qs

        # if p_type:
        #     qs = qs.filter(type_of_catering__slug=p_type)  # FIXME: must be changed for real type!!!

        return qs

    def get_context_data(self, **kwargs):
        context = super(EventsList, self).get_context_data(**kwargs)
        # context['p_types'] = PlaceType.objects.all()

        dist = self.request.GET.get('dist')
        if dist:
            if '-' not in dist:
                context['dist'] = dist

        pt = self.request.GET.get('type', None)
        context['type_active'] = pt if pt else 'one'

        return context


class EventsDetail(DetailView):
    model = Event
    template_name = 'events/events_detail.html'
