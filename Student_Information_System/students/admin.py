from django.contrib import admin

# Register your models here.
from students.models import Student, Course, Classroom, ClassManager

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Classroom)
