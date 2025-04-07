from django.shortcuts import render
from django.http import HttpResponse
    

def index(request):
    return HttpResponse("hello world. ur at polls")
# Create your views here.
