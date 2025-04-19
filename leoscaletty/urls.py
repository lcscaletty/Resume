from django.urls import path, include
from django.http import HttpResponse
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path('add/', views.add_bullet, name='add_bullet'),
    path('success/', lambda request: HttpResponse("Bullet added!"), name='success'),
]
