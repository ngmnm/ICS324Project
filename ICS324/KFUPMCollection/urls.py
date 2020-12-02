from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='KFUPMCollection/home.html'),
    path('about/', views.about, name='blog-about'),
]