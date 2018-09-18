from django import forms
from django.forms import ModelForm
from .models import Student

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

    #Don’t forget that a form’s output does not include the surrounding <form> tags, or the form’s submit control.
    #  You will have to provide these yourself


  # model for used to   create or update a student
class StudentUpdate(ModelForm):

    class Meta:
        model = Student
        fields = ['fname', 'lname', 'email']
