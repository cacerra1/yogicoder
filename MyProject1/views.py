from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from users.forms import CustomUserCreationForm
#from .forms import NameForm, ContactForm
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect

def welcome(request):
    content = "Yogi Coder"
    return render(request, 'admin/welcome.html', {'content': content})

def goodbye(request):  #uses this one
    content = "Yogi Coder"
    return render(request, 'admin/goodbye.html', {'content': content})


def thanks(request):  #uses this one
    content = "Yogi Coder"
    return render(request, 'admin/thanks.html', {'content': content})

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def not_permitted(request): # use this one for the view
    content = "not authorized"
    return render(request, 'admin/not_permitted.html', {'content': content})




