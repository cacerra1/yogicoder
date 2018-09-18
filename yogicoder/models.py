from django.db import models
from users.models import CustomUser
from django.conf import settings
import datetime

class Training(models.Model):

    VIDEO = 'VD'
    LIVE = 'LV'
    DOCUMENT = 'DC'
    TrainingType = (
        (VIDEO, "Video"),
        (LIVE, "Live"),
        (DOCUMENT, "Document"),
    )

    title = models.CharField(max_length=250)
    courseID = models.CharField(max_length=500, default= "C")
    description = models.TextField()
    version = models.FloatField(default=1.0)
    djangoVer = models.FloatField(default=2.0)
    trainType = models.CharField(max_length=2, choices=TrainingType, default= VIDEO)
    yearProd = models.DateTimeField('date created')
    active = models.BooleanField(null=True)
    imageCourse = models.ImageField(null=True, default=None, blank=True)
    location = models.URLField(blank=True)
    hostedSite = models.CharField(max_length=65)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    series = models.CharField(max_length=250, default="Inch by Inch")
    last_accessed = models.DateTimeField()


    def __str__(self):

        return ' Title: {} Authored by:  {}'.format(self.title, self.author)


class Student(models.Model):
    fname = models.CharField(max_length=250)
    lname = models.CharField(max_length=250)
    email = models.EmailField(max_length=254, null=True)
    active = models.BooleanField(null=True)
    trainings = models.ManyToManyField(Training, default=False) # student can be registered in many courses and courses have more than 1 student


    def __str__(self):
        return '{} {}'.format(self.fname, self.lname)



class Register(models.Model):
    training_class = models.ForeignKey(Training, on_delete=models.CASCADE)
    student_enrolled = models.ForeignKey(Student, on_delete=models.CASCADE)
    date_enrolled = models.DateTimeField()
    date_completed = models.DateTimeField()
