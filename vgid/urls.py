from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vgid.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    (r'^ckeditor/', include('ckeditor.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += (static(settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT))

