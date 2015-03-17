from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from showplaces.views import ShowPlacesList, ShowPlacesDetail
from museums.views import MuseumsList, MuseumsDetail
from living.views import LivingList, LivingDetail

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vgid.views.home', name='home'),

    url(r'^showplaces/$', ShowPlacesList.as_view(), name='dostoprim'),
    url(r'^showplaces/(?P<slug>[-\w]+)/$', ShowPlacesDetail.as_view(), name='dp'),

    url(r'^museums/$', MuseumsList.as_view(), name='museums'),
    url(r'^museums/(?P<slug>[-\w]+)/$', MuseumsDetail.as_view(), name='museum'),

    url(r'^living/$', LivingList.as_view(), name='living'),
    url(r'^living/(?P<slug>[-\w]+)/$', LivingDetail.as_view(), name='live'),




    url(r'^feedback/', include('feedback.urls')),


    (r'^ckeditor/', include('ckeditor.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += (static(settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT))

