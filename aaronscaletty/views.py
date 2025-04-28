from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import loader
from django.shortcuts import get_object_or_404
from django.contrib.staticfiles.storage import staticfiles_storage
import pandas as pd
import os
from .forms import terminalForm
from .models import terminalLog
# Create your views here.
csvpath= staticfiles_storage.path('resumecsv/resume.csv')
import numpy as np
df= pd.read_csv(csvpath)
df.columns = df.columns.str.strip()
activity= []
activity = df['Title'].fillna('').astype(str).str.strip().tolist()
personal = activity[4:]
activity = activity[:4]
blurbs1 = df['Bullet 1'].fillna('').astype(str).str.strip().tolist()
blurbs2 = df['Bullet 2'].fillna('').astype(str).str.strip().tolist()
blurbs3 = df['Bullet 3'].fillna('').astype(str).str.strip().tolist()
blurbs4 = df['Bullet 4'].fillna('').astype(str).str.strip().tolist()
blurbs5 = df['Bullet 5'].fillna('').astype(str).str.strip().tolist()
blurbs1p = df['Bullet 1'][-5:].fillna('').astype(str).str.strip().tolist()
blurbs2p = df['Bullet 2'][-5:].fillna('').astype(str).str.strip().tolist()
blurbs3p = df['Bullet 3'][-5:].fillna('').astype(str).str.strip().tolist()
blurbs4p = df['Bullet 4'][-5:].fillna('').astype(str).str.strip().tolist()
blurbs5p = df['Bullet 5'][-5:].fillna('').astype(str).str.strip().tolist()
combined= zip(activity,blurbs1,blurbs2,blurbs3,blurbs4,blurbs5)
combined1= zip(personal,blurbs1p,blurbs2p,blurbs3p,blurbs4p,blurbs5p)
i=-1
log= np.empty(1000, dtype=np.dtype('U100'))
def form(request):
       form = terminalForm(request.POST) 
        # check whether it's valid:
       if form.is_valid():
            global i
            global logs
            i=i+1 
            
            # process the data in form.cleaned_data as required
            form.save
            log[i]=form.cleaned_data['terminal_input']
            print(log)
            # redirect to a new URL:
            return HttpResponseRedirect('/aaronscaletty') 
       return render(request, "aaronscaletty/home.html", {'form':form})

def home(request):
        # create a form instance and populate it with data from the request:
    form = terminalForm(request.POST) 

    dict = {
            'activity': activity,
            'personal': personal,
            'combined':combined,
            'combined1':combined1,
            'form': form,
            }

    return render(request, 'aaronscaletty/home.html', dict)
    # if a GET (or any other method) we'll create a blan

