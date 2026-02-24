# this file is used to define routes 

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# takes an http request and gives back and http response
def hello_world_view(request):
    return HttpResponse("Hello World !")

def hello_python_view(request):
    return HttpResponse("Hello Python")