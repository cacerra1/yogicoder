from django.urls import path, include
from.views import TrainingList, TrainingDetail, StudentTrainingList, TrainingDetailView, OurStudents, StudentUpdate, PythonClasses, DjangoClasses
from django.contrib.auth import views as auth_views

from . import views

app_name = 'yogicoder'

urlpatterns = [
    path('lists/', views.lists, name='lists'),
    path('index/', views.index, name='index'),
    path('details/<int:student_id>/', views.detail, name='detail'), # /yogicoder/details/1/
    path('training/', TrainingList.as_view(), name='training_list'),

    path('<int:pk>/', TrainingDetail.as_view()),
    path('training/<student>/', StudentTrainingList.as_view()),
    path('trainings/<int:pk>', TrainingDetailView.as_view(), name='training_details'),
    path ('name/', views.get_name, name='name'),
    path ('name/yogicoder/thanks/', views.thanks, name='thanks'), # special way this gets built on the name/ template
    path ('yogicoder/thanks/', views.thanks, name='thanks'),
    path ('not_permitted/', views.not_permitted, name='not_permitted'),
    path ('contactform', views.contact_form, name='contactform'),
    path ('homes/', views.homes, name='homes'),
    path ('mystory/', views.mystory, name='mystory'),
    path ('coder/', views.coder, name='coder'),
    path('homes/change-password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html'), ),
    path('mystory/change-password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html'),),
    path('coder/change-password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html'),),
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html'),),
    path('studentroster/', OurStudents.as_view(), name='student_roster'), # this one just gets students
    path ('student_update/<fname>', StudentUpdate.as_view(), name='student_update'),
    path ('inactive_registration', views.inactive_registration, name='inactive_registration'),
    path('python_classes/', PythonClasses.as_view(), name='python_classes'),   # for Python Classes only
    path('django_classes/', DjangoClasses.as_view(), name='django_classes'),   # for Django Classes only





    ]
