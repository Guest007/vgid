from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from showplaces.views import ShowPlacesList, ShowPlacesDetail
from museums.views import MuseumsList, MuseumsDetail
from living.views import LivingList, LivingDetail
from catering.views import FoodList, FoodDetail
from events.views import EventsList, EventsDetail
from tours.views import ToursList, ToursDetail

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vgid.views.home', name='home'),

    url(r'^showplaces/$', ShowPlacesList.as_view(), name='dostoprim'),
    url(r'^showplaces/(?P<slug>[-\w]+)/$', ShowPlacesDetail.as_view(),
        name='dp'),

    url(r'^museums/$', MuseumsList.as_view(), name='museums'),
    url(r'^museums/(?P<slug>[-\w]+)/$', MuseumsDetail.as_view(), name='museum'),

    url(r'^living/$', LivingList.as_view(), name='living'),
    url(r'^living/(?P<slug>[-\w]+)/$', LivingDetail.as_view(), name='live'),

    url(r'^catering/$', FoodList.as_view(), name='foods'),
    url(r'^catering/(?P<slug>[-\w]+)/$', FoodDetail.as_view(), name='food'),

    url(r'^events/$', EventsList.as_view(), name='events'),
    url(r'^events/(?P<slug>[-\w]+)/$', EventsDetail.as_view(), name='event'),

    url(r'^tours/$', ToursList.as_view(), name='tours'),
    url(r'^tours/(?P<slug>[-\w]+)/$', ToursDetail.as_view(), name='tour'),




    url(r'^feedback/', include('feedback.urls')),


    (r'^ckeditor/', include('ckeditor.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += (static(settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT))

