from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Apartment

# Create your views here.
def index(request):
    return HttpResponse("Hello, Django!")

def contracts(request):
    t = loader.get_template('gestion/contracts/index.html')
    c = {}
    return HttpResponse(t.render(c, request))

def customers(request):
    return HttpResponse("Clients")

def apartments(request):
    ap = Apartment.objects.all()
    nbApts = Apartment.objects.all().count()
    t = loader.get_template('gestion/apartments/index.html')
    c = {'apts' : ap, 'nbApts' : nbApts  }
    return HttpResponse(t.render(c, request))

def options(request):
    return HttpResponse("Options")