# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, render
from apartmentfinder.models import Home
from apartmentfinder.models import Myhouse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from rest_framework_xml.parsers import XMLParser
from rest_framework_xml.renderers import XMLRenderer
from apartmentfinder.serializers import homeSerializer, MyhouseSerializer
from lxml import etree
from lxml import objectify
from io import StringIO, BytesIO


def index(request):
    home_list = Home.objects.all().order_by('-data_publikacji')
    paginator = Paginator(home_list, 5) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        homes = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        homes = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        homes = paginator.page(paginator.num_pages)

    return render_to_response('apartmentfinder/index.html', {"homes": homes})


def detail(request, pk):
    home_detail = get_object_or_404(Home, pk=pk)
    return render(request, 'apartmentfinder/detail.html', {'home_detail': home_detail})



class XMLResponse(HttpResponse):
    """
    An HttpResponse that renders its content into XML.
    """
    def __init__(self, data, **kwargs):
        content = XMLRenderer().render(data)
        kwargs['content_type'] = 'application/xml'
        super(XMLResponse, self).__init__(content, **kwargs)

@csrf_exempt
def home_list(request):
    """
    List all code home, or create a new home.
    """
    if request.method == 'POST':
        data = XMLParser().parse(request)
        serializer = homeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return XMLResponse(serializer.data, status=201)
        return XMLResponse(serializer.errors, status=400)
    if request.GET.get('from_id'):
        # retrieve objects from the value to last django  (doesn't work correct!)
        all_houses = Home.objects.all()
        test = all_houses.count()
        min_house = int(request.GET['from_id'])
        roznica = test -  min_house
        table = all_houses[:roznica]
        serializer = homeSerializer(table, many=True)
        return XMLResponse(serializer.data)
    if not request.GET.get('from_id'):
        dom = Home.objects.all()
        serializer = homeSerializer(dom, many=True)
        return XMLResponse(serializer.data)


@csrf_exempt
def home_detail(request, pk):
    """
    Detail of home in XML
    :param request:
    :param pk: id of home in database
    :return: xml of detailed home
    """
    try:
        dom = Home.objects.get(pk=pk)
    except Home.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = homeSerializer(dom)
        return XMLResponse(serializer.data)

    elif request.method == 'PUT':
        data = XMLParser().parse(request)
        serializer = homeSerializer(dom, data=data)
        if serializer.is_valid():
            serializer.save()
            return XMLResponse(serializer.data)
        return XMLResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        dom.delete()
        return HttpResponse(status=204)

def test(request):
    # import pdb; pdb.set_trace()
    all_houses = Myhouse.objects.all()
    serializer = MyhouseSerializer(all_houses, many=True)
    return XMLResponse(serializer.data)