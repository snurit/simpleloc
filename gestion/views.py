from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, Django!")

def contracts(request):
    return HttpResponse("Contrats")

def customers(request):
    return HttpResponse("Clients")

def apartments(request):
    return HttpResponse("Appartements")