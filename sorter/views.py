from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render

from sorter.models import Configuration

def home(request):
    return HttpResponse("Hello you are at the sorter home page.")

def config(request):
    configuration_list = Configuration.objects.all()
    context = {'configuration_list': configuration_list}
    print configuration_list
    return render(request, 'sorter/configuration.html', context)

def test(request):
    return HttpResponse("My Test")
