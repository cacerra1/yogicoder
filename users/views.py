from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from users.forms import CustomUserCreationForm
#from .forms import NameForm, ContactForm
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect



#class SignUp(generic.CreateView):
    #form_class = CustomUserCreationForm
    #success_url = reverse_lazy('login')
    #template_name = 'signup.html'

# nothing needed here. I am taking care
# of this through the MyProject1/views


def signup_form(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']

            email = form.cleaned_data['email']


            recipients = [email, 'imtheyogicoder@gmail.com']


            send_mail(username, email, recipients)
            return HttpResponseRedirect('yogicoder/thanks/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})