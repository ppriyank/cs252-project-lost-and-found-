from django.http import HttpResponse, Http404

from django.shortcuts import render

from .models import Data, Tag
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
    content = request.POST["content"]
    if "tags" in request.POST:
        tag_list=[]
        tags=request.POST["tags"]
        tag_list= [Tag.objects.get_or_create(name=tag)[0] for tag in tags.split()]
    try:
        data = Data.objects.get(pk =data_id )
        data.content = content
        for tag in tag_list:            #Create relationship between tag object and data
            data.tags.add(tag)
        return HttpResponse("<h2> Details for Object number : " + str(data_id) + " </h2> " )
    except Data.DoesNotExist :
        for tag in tag_list:
            data.tags.add(tag)
        raise Http404("Such Database entry doesn't exists")

