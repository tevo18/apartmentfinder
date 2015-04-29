__author__ = 'madzik'
from models import supermarket
from rest_framework import routers, serializers, viewsets
from rest_framework_xml.parsers import XMLParser
from rest_framework_xml.renderers import XMLRenderer



class shopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = supermarket
        fields = ('id', 'tytul', 'opis', 'nazwa_dzielnicy', 'wspolrzedne_dl','wspolrzedne_szer','zdjecie')


class shopViewSet(viewsets.ModelViewSet):
    queryset = supermarket.objects.all()
    serializer_class = shopSerializer
    parser_classes = (XMLParser,)
    renderer_classes = (XMLRenderer,)