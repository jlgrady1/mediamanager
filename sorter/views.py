from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render

from sorter.models import Configuration

def home(request):
    context = {}
    return render(request, 'sorter/index.html', context)

def config(request):
    configuration_list = Configuration.objects.all()
    context = {'configuration_list': configuration_list}
    return render(request, 'sorter/configuration.html', context)

def editconfig(request):
    print "do some stuff"
    newkey = request.POST['newkey']
    newvalue = request.POST['newvalue']
    newtype_id = request.POST['newtype']
    if newkey is not None and newvalue is not None and newtype_id is not None:
        newconfig = Configuration(key=newkey, \
                                  value=newvalue, \
                                  type=Type.objects.get(pk=newtype_id))
        newconfig.save()
    return config(request)
