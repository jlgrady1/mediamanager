from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello you are at the sorter index.")

def config(request):
    return HttpResponse("Configuration.")

def test(request):
    return HttpResponse("My Test")
