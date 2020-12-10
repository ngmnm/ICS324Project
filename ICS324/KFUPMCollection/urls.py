from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='KFUPMCollection/home.html'),
    path('courses/', views.courses, name='KFUPMCollection/courses.html'),
    path('about/', views.about, name='KFUPMCollection/about.html'),
]