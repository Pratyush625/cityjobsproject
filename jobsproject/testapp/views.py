from django.shortcuts import render
from testapp.models import *
# Create your views here.
def index(request):
    return render(request,'testapp/index.html')

def hydjobsinfo(request):
    jobs_list=hydjobs.objects.order_by('company')
    my_dict={'jobs_list':jobs_list}
    return render(request,'testapp/hydjobs.html',context=my_dict)

def blorejobsinfo(request):
    jobs_list=hydjobs.objects.all()
    my_dict={'jobs_list':jobs_list}
    return render(request,'testapp/blorejobs.html',context=my_dict)

def chennaijobsinfo(request):
    jobs_list=blorejobs.objects.all()
    my_dict={'jobs_list':jobs_list}
    return render(request,'testapp/chennaijobs.html',context=my_dict)

def punejobsinfo(request):
    jobs_list=punejobs.objects.all()
    my_dict={'jobs_list':jobs_list}
    return render(request,'testapp/punejobs.html',context=my_dict)
