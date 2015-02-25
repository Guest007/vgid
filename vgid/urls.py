from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from showplaces.views import ShowPlacesList
from feedback.views import callback as callback_ajax

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vgid.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^showplaces/$', ShowPlacesList.as_view(), name='dostoprim'),
    url(r'^callback/$', callback_ajax, name='callback'),


    (r'^ckeditor/', include('ckeditor.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += (static(settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT))

