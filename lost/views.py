from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Data
from mailing import form_entry

def index(request):
    all_data= Data.objects.all()
    return render(request,'lost/index.html',{'all_data':all_data})

def form(request):
    all_data= Data.objects.all()
    # mail = all_data.email
    print "----------------------"
    mail = 'shanuv@iitk.ac.in'
    print "======"
    form_entry(mail)
    return render(request,'lost/index.html',{'all_data':all_data})

# Create your views here.


def Details(request, data_id):
    try:
        data = Data.objects.get(pk =data_id )
        img_url="http://oa.cc.iitk.ac.in:8181/Oa/Jsp/Photo/" + str(data.rollno) + "_0.jpg"
        return render(request,'lost/details.html',{'data':data, 'img_url': img_url})
    except Data.DoesNotExist :
        raise Http404("Such Database entry doesn't exists")



