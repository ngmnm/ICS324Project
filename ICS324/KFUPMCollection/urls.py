from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.courses, name='KFUPMCollection/courses.html'),
    path('resource/upload_done/', views.upload_done, name='KFUPMCollection/upload_done.html'),
    path('resource/upload/', views.upload, name='KFUPMCollection/upload.html'),
    path('resource/', views.resource, name='KFUPMCollection/resource.html'),
    path('newDep/', views.newDep, name='newDep'),
    path('newDep_submit/', views.newDep_submit, name='KFUPMCollection/newDep_submit.html'),
    path('newCourse/', views.newCourse, name='newCourse'),
    path('newCourse_submit/', views.newCourse_submit, name='KFUPMCollection/newCourse_submit.html'),
    path('about/', views.about, name='KFUPMCollection/about.html'),
    path('instructors/', views.instructors, name='KFUPMCollection/instructors.html'),
    path('instructors/evaluations/', views.evaluations, name='KFUPMCollection/instructors/evaluations.html'),
    path('instructors/evaluations/evaluationd', views.evaluationdetailes, name='KFUPMCollection/instructors/evaluations/evaluationd.html'),
    path('newDep/', views.newDep, name='newDep'),
    path('newDep_submit/', views.newDep_submit, name='KFUPMCollection/newDep_submit.html'),
    path('newCourse/', views.newCourse, name='newCourse'),
    path('newCourse_submit/', views.newCourse_submit, name='KFUPMCollection/newCourse_submit.html'),
    path('addQuestion', views.addQuestion, name='KFUPMCollection/addQuestion.html'),
    path('addQuestionSubmission', views.addQuestionSubmission, name='KFUPMCollection/addQuestionSubmission.html'),
    path('instructors/evaluations/addEvaluation', views.addEvaluation, name='KFUPMCollection/instructors/evaluations/addEvaluation.html'),
    path('addEvaluationSubmission', views.addEvaluationSubmission, name='KFUPMCollection/addEvaluationSubmission.html'),
    path('newInstructor', views.newInstructor, name='KFUPMCollection/newInstructor.html'),
    path('newInstructor_submit/', views.newInstructor_submit, name='KFUPMCollection/newInstructor_submit.html'),

]