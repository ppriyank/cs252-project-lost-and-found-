from django.http import HttpResponse, Http404

from django.shortcuts import render

from .models import Data
from search import print_searchtag

def index(request):
    all_data= Data.objects.all()
    print_searchtag()
    html = ''
    for data in all_data :
        url = '/LostAndFound/'+ str(data.id) +'/'
        html += '<a href="' + url + '">' + data.name + '</a> <br>'

    return HttpResponse(html)



# Create your views here.


def Details(request, data_id):
    try:
        data = Data.objects.get(pk =data_id )
        return HttpResponse("<h2> Details for Object number : " + str(data_id) + " </h2> " )
    except Data.DoesNotExist :
        raise Http404("Such Database entry doesn't exists")

