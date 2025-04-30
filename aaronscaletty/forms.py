from django.forms import ModelForm
from django import forms
from .models import terminalForm

class terminalForm(ModelForm):
    terminal_input = forms.CharField(label="aaronscaletty$", max_length=100)
    class Meta:
        model = terminalForm
        fields= ['terminal_input']
        #widgets ={
         #   'terminal_input': forms.TextInput(attrs={'class':'form-control'})
          ##  }
    

