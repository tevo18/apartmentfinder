__author__ = 'madzik'
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from rest_framework_xml.parsers import XMLParser
from rest_framework_xml.renderers import XMLRenderer
from serializers import shopSerializer
from models import supermarket


def index(request):
    supermarket_list = supermarket.objects.all().order_by('-nazwa_dzielnicy')


    paginator = Paginator(supermarket_list, 5)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        shops = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer, deliver first page.
        shops = paginator.page(1)
    except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
        shops = paginator.page(paginator.num_pages)
    return render_to_response('myshop/index.html', {"shops": shops})


def detail(request, pk):
    shop_detail = get_object_or_404(supermarket, pk=pk)


    return render(request, 'myshop/detail.html', {'shop_detail': shop_detail})


class XMLResponse(HttpResponse):
    """
    An HttpResponse that renders its content into XML.
    """


    def __init__(self, data, **kwargs):
        content = XMLRenderer().render(data)


        kwargs['content_type'] = 'application/xml'
        super(XMLResponse, self).__init__(content, **kwargs)


@csrf_exempt
def supermarket_list(request):
    """
    List all code home, or create a new home.
    """


    if request.method == 'POST':
        data = XMLParser().parse(request)
        serializer = shopSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return XMLResponse(serializer.data, status=201)
        return XMLResponse(serializer.errors, status=400)
    if request.GET.get('from_id'):
    # retrieve objects from the value to last django (doesn't work correct!)
        all_shops = supermarket.objects.all()
        test = all_shops.count()
        min_house = int(request.GET['from_id'])
        roznica = test - min_house
        table = all_shops[:roznica]
        serializer = shopSerializer(table, many=True)
        return XMLResponse(serializer.data)
    if not request.GET.get('from_id'):
        sklep = supermarket.objects.all()
        serializer = shopSerializer(sklep, many=True)
        return XMLResponse(serializer.data)


@csrf_exempt
def shop_detail(request, pk):
    """
    Detail of home in XML
    :param request:
    :param pk: id of home in database
    :return: xml of detailed home
    """


    try:
        sklep = supermarket.objects.get(pk=pk)
    except supermarket.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = shopSerializer(sklep)
        return XMLResponse(serializer.data)
    elif request.method == 'PUT':
        data = XMLParser().parse(request)
        serializer = shopSerializer(sklep, data=data)
        if serializer.is_valid():
            serializer.save()
            return XMLResponse(serializer.data)
        return XMLResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        sklep.delete()
        return HttpResponse(status=204)