from django.shortcuts import render

from .models import departments, course


def home(request):
    context = {
        'department': departments.objects.all()
    }
    return render(request, 'KFUPMCollection/home.html', context)


def courses(request):
    context = {
        'courses': course.objects.all()
    }
    return render(request, 'KFUPMCollection/courses.html', context)


def about(request):
    return render(request, 'KFUPMCollection/about.html')


