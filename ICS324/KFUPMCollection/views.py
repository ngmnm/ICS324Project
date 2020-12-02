from django.shortcuts import render

from .models import Post


def home(request):
    
    return render(request, 'KFUPMCollection/home.html')


def about(request):
    return render(request, 'blog/about.html')