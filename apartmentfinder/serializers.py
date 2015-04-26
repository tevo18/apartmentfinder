# -*- coding: utf-8 -*-
from apartmentfinder.models import *

from rest_framework import routers, serializers, viewsets
from rest_framework_xml.parsers import XMLParser
from rest_framework_xml.renderers import XMLRenderer



class homeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Home
        fields = ('id', 'title', 'description', 'district_name', 'rooms_number', 'price','latitude', 'longitude', 'publication_date','photo')

class homeViewSet(viewsets.ModelViewSet):
    queryset = Home.objects.all()
    serializer_class = homeSerializer
    parser_classes = (XMLParser,)
    renderer_classes = (XMLRenderer,)



class MyhouseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Myhouse
        fields = ('id', 'title', 'description', 'district_name', 'rooms_number', 'price', 'latitude', 'longitude', 'publication_date','photo')



class MyhouseViewSet(viewsets.ModelViewSet):
    queryset = Myhouse.objects.all()
    serializer_class = MyhouseSerializer
    parser_classes = (XMLParser,)
    renderer_classes = (XMLRenderer,)