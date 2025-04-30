from django.urls import path
from . import views 
urlpatterns= [
path("", views.home, name='home'),
path("/terminal", views.form, name= 'form'),
]
