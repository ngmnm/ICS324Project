from django.shortcuts import render
from .models import departments, course, instructor,evaluation, answer, question, contains
from django.http import HttpResponse
from django.contrib import messages

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
        'evaluationQA': contains.objects.all(),
         'evaID': request.GET.get('evaID')
    }
    return render(request, 'KFUPMCollection/evaluationd.html', context)


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

def addQuestionSubmission(request):
    print("Question has been submitted.")
    question_new = request.POST["question_new1"]
    weight_new = request.POST["weight_new1"]
    QID_new = request.POST["QID_new1"]

    question_info = question(QID=QID_new, Qname=question_new, Weight=weight_new)
    question_info.save()
    return render(request, 'KFUPMCollection/addQuestion.html')

def addQuestion(request):

    return render(request, 'KFUPMCollection/addQuestion.html')

