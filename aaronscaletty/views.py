from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import loader, redirect
from django.shortcuts import get_object_or_404
from django.contrib.staticfiles.storage import staticfiles_storage
# Create your views here.
def home(request):
    # create a form instance and populate it with data from the request:
    return render(request, 'aaronscaletty/home.html')

    

