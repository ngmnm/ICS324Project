from django.shortcuts import render

from django.contrib import messages
from .models import departments, course, instructor
from django.http import HttpResponse


from .models import departments, course, instructor, evaluation, answer, question

from .models import departments, course, instructor, evaluation, answer, question, contains, resource
from django.contrib import messages
from .models import departments, course, instructor, workFor
from django.http import HttpResponse
from .models import departments, course, instructor, evaluation, answer, question, contains

from . import models
from . import forms
from users.forms import resource


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
        'instructors': instructor.objects.all(),
        'insID': request.GET.get('insID')
    }
    return render(request, 'KFUPMCollection/instructors.html', context)


def evaluation(request):
    return render(request, 'KFUPMCollection/evaluation.html')


def evaluations(request):
    context = {
        'evaluations': evaluation.objects.all(),
        'insID': request.GET.get('insID')
    }
    return render(request, 'KFUPMCollection/evaluation.html', context)


def evaluationdetailes(request):
    context = {
        'evaluationAnswers': answer.objects.all(),
        'evaluationQuestions': question.objects.all(),
        'evaID': request.GET.get('evaID'),
        'evaluationQA': contains.objects.all(),
    }
    return render(request, 'KFUPMCollection/evaluationd.html', context)


def newInstructor(request):
    return render(request, 'KFUPMCollection/newInstructor.html')


def newInstructor_submit(request):
    nameI = request.POST.get('Name_field', False)
    IIDI = request.POST.get('DID_field', False)
    DIDI = request.POST.get('DID_field', False)
    OfficePhoneI = request.POST.get('OfficePhone_field', False)
    EmailI = request.POST.get('Email_field', False)
    OfficeLocationI = request.POST.get('OfficeLocation_field', False)
    WebsiteI = request.POST.get('Website_field', False)
    newI = instructor(Name=nameI, IID=IIDI, Office_Phone_number=OfficePhoneI, Email=EmailI,
                      Office_location=OfficeLocationI, website=WebsiteI)
    newI.save()
    newWorkfor = workFor(DID=DIDI, IID=IIDI)
    newWorkfor.save()
    messages.success(request, f' {nameI} has been created!')
    return render(request, 'KFUPMCollection/newInstructor_submit.html')


def about(request):
    return render(request, 'KFUPMCollection/about.html')


def newDep(request):
    return render(request, 'KFUPMCollection/newDep.html')


def newDep_submit(request):
    department = departments.objects.all().count()+1

    name = request.POST.get('name', False)
    icon = request.POST.get('icon', False)
    DID = department
    newDep = departments(name=name, icon=icon, DID=DID)
    newDep.save()
    messages.success(request, f' {name} has been created!')
    return render(request, 'KFUPMCollection/newDep_submit.html')


def newCourse(request):
    context = {
        'department': departments.objects.all(),
        'depID': request.GET.get('depID')
    }
    return render(request, 'KFUPMCollection/newCourse.html', context)


def newCourse_submit(request):
    name = request.POST.get('name', False)
    CID = request.POST.get('name', False)
    prerequisites = request.POST.get('prerequisties', False)
    DID = request.POST.get('depID', False)
    newCourse = course(Name=name, CID=CID,
                       prerequisites=prerequisites, DID=DID)
    newCourse.save()
    messages.success(request, f' {name} has been created!')

    return render(request, 'KFUPMCollection/newCourse_submit.html')


def addQuestionSubmission(request):
    print("Question has been submitted.")
    question_new = request.POST["question_new1"]
    weight_new = request.POST["weight_new1"]
    QID_new = request.POST["QID_new1"]

    question_info = question(
        QID=QID_new, Qname=question_new, Weight=weight_new)
    question_info.save()
    return render(request, 'KFUPMCollection/addQuestion.html')


def addQuestion(request):
    return render(request, 'KFUPMCollection/addQuestion.html')


def upload_done(request):
    return render(request, 'KFUPMCollection/uplaod_done.html')


def upload(request):

    u = models.resource()
    form = forms.file_form(request.POST, request.FILES)
    u.CID = request.GET.get('courseID')

    if form.is_valid():
        u.Name = form.cleaned_data['name']
        u.Type = form.cleaned_data['Type']
        u.path = form.cleaned_data['file']

        u.save()

        return render(request, 'KFUPMCollection/upload_done.html')

    return render(request, 'KFUPMCollection/upload.html', {'forms': form})


def resource(request):
    context = {

        'resource': models.resource.objects.all(),

        'courseID': request.GET.get('CourseID')
    }

    return render(request, 'KFUPMCollection/resource.html', context)
