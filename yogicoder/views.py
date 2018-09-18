
from django.http import HttpResponse, HttpResponseRedirect
from .models import Training, Student
from django.shortcuts import render, Http404, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views import generic, View
from django.utils import timezone
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import redirect
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from django.contrib.auth.mixins import PermissionRequiredMixin
#from django_sortable.helpers import sortable_helper
# includes for the update view below
from django.views.generic import UpdateView
from .models import Student
from MyProject1.mixins import ActiveOnlyMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator





def index(request):
    return HttpResponse("Hello, Django. You're at the YogiCoder index.")

permission = ('yogicoder.view_training', 'yogicoder.add_training')
@login_required
#@staff_member_required(login_url='/accounts/login/')
#@permission_required('yogicoder.view_training')
@permission_required(permission, raise_exception=False, login_url='/not_permitted/')
def lists(request):


    training = Training.objects.order_by('title')
    #trainings_new = sortable_helper(request, training)
    return render(request, 'yogicoder/datatables.html', {'training': training})


def detail(request, student_id):

    try:
        student = Student.objects.get(pk=student_id)
        hw = Training.objects.filter(student__id=student_id) # sets a variable to grab the training sessions that a given student has taken


    except Student.DoesNotExist:
        raise Http404("That Student does not exist") # raises 404 if record with request ID does not exist
    return render(request, 'yogicoder/detail.html', {'detail': detail, 'student': student, 'hw':hw})


class TrainingList(ListView, PermissionRequiredMixin, View):
    model = Training
    permission_required = ('yogicoder.view_training', 'yogicoder.add_training') # perms required to a class-based view


class TrainingDetail(DetailView):

    model = Training  # this is the same as queryset = Training.objects.all()
    template_name = 'yogicoder/training_detail.html'

class OurStudents(ListView, PermissionRequiredMixin, View, ActiveOnlyMixin, LoginRequiredMixin):   # I created this in the mixin.py file in Myproject

    permission_required = ('yogicoder.change_student')
    raise_exception = False
    login_url='/not_permitted/'

    model = Student  # this is the same as queryset = Training.objects.all()
    template_name = 'yogicoder/our_students.html'


class StudentTrainingList(ListView):
    template_name = 'yogicoder/training_by_student.html'

    def get_queryset(self):
        self.student = get_object_or_404(Student, fname=self.kwargs['student'])
        return Training.objects.filter(student=self.student)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['student'] = self.student
        return context

class TrainingDetailView(DetailView):

    queryset = Training.objects.all()
    template_name = 'yogicoder/training_detail_view.html'


    def get_object(self):
        obj = super().get_object()
        # Record the last accessed date
        obj.last_accessed = timezone.now()

        obj.save()
        return (obj)



from .forms import NameForm, ContactForm
from django.core.mail import send_mail


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('yogicoder/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'yogicoder/name.html', {'form': form})


def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['imtheyogicoder@gmail.com']

            if cc_myself:
                recipients.append(sender)

            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('yogicoder/thanks/')
    else:
        form = ContactForm()

    return render(request, 'yogicoder/contactform.html', {'form': form})

def thanks(request):
    content = "Yogi Coder"
    return render(request, 'yogicoder/thanks.html', {'content': content})


def homes(request):
    content = "Yogi Coder"
    return render(request, 'yogicoder/home.html', {'content': content})

def mystory(request):
    content = "Yogi Coder"
    return render(request, 'yogicoder/mystory.html', {'content': content})

def coder(request):
    content = "Yogi Coder"
    return render(request, 'yogicoder/coder.html', {'content': content})


def not_permitted(request):
    content = "not authorized"
    return render(request, 'yogicoder/not_permitted.html', {'content': content})


#my student update view

class StudentUpdate(UpdateView):
    model = Student
    fields = ['fname','lname', 'email']
    template_name_suffix = '_update_form'
    success_url = '/thanks/'
    permission_required = ('yogicoder.add_student','yogicoder.change_student' )


def inactive_registration(request):
    content = "Not Permitted"
    return render(request, 'yogicoder/inactive_registration.html', {'content': content})


 # generic view to show my python courses only
@method_decorator(login_required, name='dispatch')
class PythonClasses(ListView):
    queryset = Training.objects.filter(title__contains='Python')
    context_object_name = 'python_training'
    template_name = 'yogicoder/python_classes.html'

 # generic view to show my python courses only
@method_decorator(login_required, name='dispatch')
class DjangoClasses(ListView):
    queryset = Training.objects.filter(courseID__contains='CD2')
    context_object_name = 'django_training'
    template_name = 'yogicoder/django_classes.html'