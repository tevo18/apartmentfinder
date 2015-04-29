__author__ = 'madzik'
from django.conf.urls import patterns, url
from myshop import showData

urlpatterns = patterns('',
    url(r'^$', showData.index, name='index'),
    url(r'^(?P<home_id>\d+)/$', showData.detail, name='detail'),
    url(r'^export/$', showData.supermarket_list, name='supermarket_list'),
    url(r'^(?P<pk>[0-9]+)/export/$', showData.shop_detail, name='shop_detail'),
)