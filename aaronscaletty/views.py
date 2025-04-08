from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import loader
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    template= loader.get_template("aaronscaletty/home.html")
    return render(request, "aaronscaletty/home.html")
