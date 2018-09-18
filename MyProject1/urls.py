"""MyProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from . import views
from yogicoder.views import StudentUpdate, StudentTrainingList

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),


    path('yogicoder/', include('yogicoder.urls', namespace='yogicoder')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('welcome/', views.welcome, name='welcome'),
    path('goodbye/', views.goodbye, name='goodbye'),
    path('thanks/', views.thanks, name='thanks'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('users/', include('users.urls')),
    path('accounts/login/change-password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html'),),
    path('goodbye/change-password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html'),),
    path('welcome/change-password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html'),),
    path('signup/change-password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html'),),
    path('signup/change-password/password-change-done', auth_views.PasswordChangeDoneView.as_view(template_name='registration/change-password-done.html'),),
    path('front-edit/', include('front.urls')),
    #path ('student_update/<int:pk>', StudentUpdate.as_view(), name='student_update'),
    path ('student_list/<int:pk>', StudentUpdate.as_view(), name='student_update'), #This updates the students
    path ('not_permitted/', views.not_permitted, name='not_permitted'),
    path('training/<student>/', StudentTrainingList.as_view()), # this is for the detail view showing the classes each student is enrolled in
]

