from django.shortcuts import render
from django.contrib import messages
from .models import departments, course, instructor
from django.http import HttpResponse 


def home(request):
    context = {
        'department': departments.objects.all()
    }
    return render(request, 'KFUPMCollection/home.html', context)


def courses(request):

    context = {
        'courses': course.objects.all(),
        'depID': request.GET.get('depID')
    }
    return render(request, 'KFUPMCollection/courses.html', context)


def instructors(request):
    context = {
        'instructors': instructor.objects.all()
    }
    return render(request, 'KFUPMCollection/instructors.html', context)


def evaluation(request):

    return render(request, 'KFUPMCollection/evaluation.html')


def about(request):
    return render(request, 'KFUPMCollection/about.html')


def newDep(request):
    
    return render(request, 'KFUPMCollection/newDep.html')


def newDep_submit(request):
    name = request.POST.get('name', False);
    icon = request.POST.get('icon', False);
    DID =  request.POST.get('DID', False);
    newDep = departments(name=name, icon=icon, DID=DID)
    newDep.save()
    messages.success(request, f' {name} has been created!')
    return render(request, 'KFUPMCollection/newDep_submit.html')


def newCourse(request):
    context = {
        'department': departments.objects.all()
    }
    return render(request, 'KFUPMCollection/newCourse.html', context)


def newCourse_submit(request):
    name = models.CharField('name')
    CID = models.CharField('courseID')
    prerequisites = models.CharField('prerequisties')
    
    newCourse = course(Name=name, CID=CID, prerequisites=prerequisites)
    newCourse.save()
    messages.success(request, f' {name} has been created!')
    return render(request, 'KFUPMCollection/newCourse_submit.html')
