from django.contrib import admin

# Register your models here.
from students.models import Student, Department, Subject, Teacher,Score

admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Department)
admin.site.register(Score)
admin.site.register(Teacher)
