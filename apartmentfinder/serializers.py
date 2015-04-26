# -*- coding: utf-8 -*-
from apartmentfinder.models import *

from rest_framework import routers, serializers, viewsets
from rest_framework_xml.parsers import XMLParser
from rest_framework_xml.renderers import XMLRenderer



class homeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Home
        fields = ('id', 'tytul', 'opis', 'nazwa_dzielnicy', 'liczba_pokoi', 'cena', 'wspolrzedne_dl','wspolrzedne_szer', 'data_publikacji','zdjecie')



class homeViewSet(viewsets.ModelViewSet):
    queryset = Home.objects.all()
    serializer_class = homeSerializer
    parser_classes = (XMLParser,)
    renderer_classes = (XMLRenderer,)