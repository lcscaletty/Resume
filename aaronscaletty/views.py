from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import loader, redirect
from django.shortcuts import get_object_or_404
from django.contrib.staticfiles.storage import staticfiles_storage
import pandas as pd
import os
from .forms import terminalForm
import time
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
log= np.empty(1000, dtype=np.dtype('U100'))
i=0
def form(request):
    global log
    global i
    #form = terminalForm(request.POST)
       #print('before iteration',i, log)
    # check whether it's valid:
    form= terminalForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            print('in form save part')
            #process the data in form.cleaned_data as required
            form.save
            log[i]=form.cleaned_data['terminal_input'] 
            response = processinput(i,log)
            i=i+1
            form_name= 'm'+str(i)
            print(i)
            print('passed formname', form_name)
        else: 
            print(form.errors.as_data())
                        #print(log)
                        #print("passed response:",response)

    context = {
                'form': terminalForm(),
                'i': i,
                'form_name': form_name,
                'response': response,
                 }
           #print(context['response'])
    return render(request, "aaronscaletty/partials/form.html", context)

def home(request):
    # create a form instance and populate it with data from the request:
   if i==0:
       hider= 'hidden'
       print('hiding pre div')
   else:
       hider=""
       print(' pre div unhidden')
   form_name= 'm'+str(i)
   dict = {
            'activity': activity,
            'personal': personal,
            'combined':combined,
            'combined1':combined1,
            'form':terminalForm(),
            'i':i,
            'form_name': form_name,
            "hider": hider,
            }
   return render(request, 'aaronscaletty/home.html', dict)
def processinput(n, log):
    print('i value', n)
    if log[n] == 'help':
        print('help called')
        return  """"get cv:                           download my resume
                    projects:                         My projects
                    skills:                           My tech skills
                    contact:                          Contact method
                    clear:                            clear terminal
                    normal:                 turn this page into a normal website 
                        type one of the above to view."""
    if log[n] == 'clear':
        log[:]=""
        i= 0
        print('cleared' ,log)
        return 'clear terminal'
    if log[n] == 'skills':
        return 'CAD, Python, C++, Soldering, Manual Drafting, Project Management'
    else:
        print('else called')
        return 'command not found'
    
    

