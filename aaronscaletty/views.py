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
df.columns = df.columns.str.strip()
def home(request):
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
    print(combined1)
    dict = {
            'activity': activity,
            'personal': personal,
            'combined':combined,
            'combined1':combined1,
    }

    return render(request, "aaronscaletty/home.html", dict)

