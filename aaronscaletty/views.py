from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import loader
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    message= "hi folks"
    return render(request, "aaronscaletty/home.html" )


