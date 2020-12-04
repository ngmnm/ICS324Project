from django.shortcuts import render

from .models import dep


def home(request):
    context = {
        'department': dep.objects.all()
    }
    return render(request, 'KFUPMCollection/home.html', context )


def about(request):
    return render(request, 'KFUPMCollection/about.html')