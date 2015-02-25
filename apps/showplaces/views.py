from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from .models import Place, PlaceType

class ShowPlacesList(ListView):
    model = Place
    queryset = Place.objects.filter(is_publish=True).order_by('weight')
    # paginate_by = 25
    template_name = 'showplaces/place_list.html'

    def get_queryset(self):
        qs = super(ShowPlacesList, self).get_queryset()
        # print "---> {}".format(len(qs))
        return qs
