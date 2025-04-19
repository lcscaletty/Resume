from django import forms
from .models import Bullet

class BulletForm(forms.ModelForm):
    class Meta:
        model = Bullet
        fields = ['content', 'category']