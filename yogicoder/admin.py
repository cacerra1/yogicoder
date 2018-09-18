from django.contrib import admin

from .models import Training, Student, Register

@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'version' )

admin.site.register(Student)
admin.site.register(Register)
