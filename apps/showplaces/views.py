from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from .models import Place, PlaceType


class ShowPlacesList(ListView):
    model = Place
    queryset = Place.objects.filter(is_publish=True).order_by('weight')
    # paginate_by = 25
    template_name = 'showplaces/place_list.html'
    default_filter_param = 'all'

    def get_queryset(self):
        qs = super(ShowPlacesList, self).get_queryset()
        dist = self.request.GET.get('dist')
        if dist:
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



        # print "---> {}".format(len(qs))
        return qs
    
    def get_context_data(self, **kwargs):
        context = super(ShowPlacesList, self).get_context_data(**kwargs)

        dist = self.request.GET.get('dist')
        if dist:
            # print dist
            context['dist'] = dist

        # context['filters'] = f

        return context
