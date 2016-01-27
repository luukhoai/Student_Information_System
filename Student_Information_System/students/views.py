from django.shortcuts import render

# Create your views here.
from django.views import generic
from students.models import Student, Subject, Department

class IndexView(generic.ListView):
    template_name = 'students/studentlist.html'
    context_object_name = 'student_list'

    def get_queryset(self):
        #return Student.objects.all()
        #return Student.objects.filter(id = 1)
        #return Student.objects.filter(name__startswith = 'Al')
        #return Student.objects.filter(name__iendswith = 'ta')
        #return Student.objects.filter(subjects__name = 'Room 1')
        #return Subject.objects.filter(students__name = 'Alpha')
        return Department.objects.filter(subject__name = 'Room 1')
        
class ShowObjectList(generic.ListView):
    template_name = 'students/objectlist.html'
    context_object_name = 'object_list'
    
    def get_queryset(self):
        ""
        return [1, 2, 34]        
        #return Student.objects.get_students_with_Address2()