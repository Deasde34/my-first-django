from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    
    return HttpResponse("Welcome")
    
def about(request):
    
    return HttpResponse("about")

def contact(request):
    
    return HttpResponse("contact")

def pageFour(request):
    
    return HttpResponse("page four")

def pageFive(request):
    
    return HttpResponse("page five")

def pageSix(request):
    
    return HttpResponse("page six")

def pageSeven(request):

    return HttpResponse("page seven")

def pageEight(request):

    return HttpResponse("page eight")

def pageNine(request):

    return HttpResponse("page nine")

def pageTen(request):

    return HttpResponse("page ten")

def pageEleven(request):

    return HttpResponse("page eleven")

def pageTwelve(request):
    
    return HttpResponse("page twelve")

def pageThirteen(request):

    return HttpResponse("page thirteen")