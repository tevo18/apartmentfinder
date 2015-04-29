from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
import myshop
admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'first.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^$', include('myshop.urls', namespace="myshop")),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^(?P<pk>\d+)/$', myshop.showData.detail, name='detail'),
    url(r'^(?P<pk>[0-9]+)/export/$', myshop.showData.shop_detail, name='shop_detail'),
    url(r'^export/$', myshop.showData.supermarket_list, name='supermarket_list'),
    
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
