from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
import apartmentfinder
admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'first.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^$', include('apartmentfinder.urls', namespace="apartmentfinder")),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^(?P<pk>\d+)/$', apartmentfinder.views.detail, name='detail'),
    url(r'^(?P<pk>[0-9]+)/export/$', apartmentfinder.views.home_detail, name='home_detail'),
    url(r'^export/$', apartmentfinder.views.home_list, name='home_list'),
    
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
