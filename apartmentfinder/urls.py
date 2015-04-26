from django.conf.urls import patterns, url
from apartmentfinder import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<home_id>\d+)/$', views.detail, name='detail'),
    url(r'^export/$', views.home_list, name='home_list'),
    url(r'^(?P<pk>[0-9]+)/export/$', views.home_detail, name='home_detail'),
)