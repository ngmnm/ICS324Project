from django.shortcuts import render
<<<<<<< HEAD

from django.contrib import messages
from .models import departments, course, instructor
from django.http import HttpResponse 


from .models import departments, course, instructor,evaluation, answer, question
=======
from .models import departments, course, instructor,evaluation, answer, question, contains
>>>>>>> 8781639d14452e7f98592e23654fa7415f765ea0
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
<<<<<<< HEAD
        'evaID': request.GET.get('evaID')
=======
        'evaluationQA': contains.objects.all(),
         'evaID': request.GET.get('evaID')
>>>>>>> 8781639d14452e7f98592e23654fa7415f765ea0
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
        'department': departments.objects.all(),
        'depID': request.GET.get('depID')
    }
    return render(request, 'KFUPMCollection/newCourse.html', context)


def newCourse_submit(request):
    name = request.POST.get('name', False);
    CID = request.POST.get('name', False);
    prerequisites = request.POST.get('prerequisties', False);
    DID = request.POST.get('depID', False);
    newCourse = course(Name=name, CID=CID, prerequisites=prerequisites, DID=DID )
    newCourse.save()
    messages.success(request, f' {name} has been created!')
<<<<<<< HEAD

    return render(request, 'KFUPMCollection/newCourse_submit.html')

=======
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

>>>>>>> 8781639d14452e7f98592e23654fa7415f765ea0
