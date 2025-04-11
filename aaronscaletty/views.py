from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import loader
from django.shortcuts import get_object_or_404
import pandas as pd
# Create your views here.

import numpy as np
df= pd.read_csv('../resumecsv/resume.csv')
print(df)
activity= np.empty((8,1), dtype= object)
i=0
while i < 8:
    activity[i]= df.iloc[i,1]
    i+=1
def home(request):
    return render(request, "aaronscaletty/home.html" )


