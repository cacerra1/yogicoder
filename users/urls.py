from django.urls import path
from . import views


app_name = 'users'

urlpatterns = [

    #path('goodbye/', views.goodbye, name='goodbye'), # nothing needed here... defined in MyProjects1/urls.py
    path('signup/', views.signup_form, name='signup_form'),
]