from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import loader
from django.shortcuts import get_object_or_404
from django.contrib.staticfiles.storage import staticfiles_storage
import pandas as pd
import os
# Create your views here.
csvpath= staticfiles_storage.path('resumecsv/resume.csv')
import numpy as np
df= pd.read_csv(csvpath)
def home(request):
    activity= []
    activity= df['Title '].to_list()
    personal= activity[4:]

    #activity= activity[:4]
    dict = {
            'activity': activity,
            'personal': personal,
    }

    return render(request, "aaronscaletty/home.html", dict)

