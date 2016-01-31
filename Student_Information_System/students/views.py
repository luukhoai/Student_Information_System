from django.shortcuts import render

# Create your views here.
from django.views import generic
from students.models import Student, Subject, Department
from django.shortcuts import get_object_or_404, render

class IndexView(generic.ListView):
    template_name = 'students/studentlist.html'
    context_object_name = 'student_list'

    def get_queryset(self):
        #return Student.objects.all()
        #return Student.objects.filter(id = 1)
        #return Student.objects.filter(name__startswith = 'Al')
        #return Student.objects.filter(name__iendswith = 'ta')
        return Student.objects.filter(subjects__sub_name = 'Room 3')
        #return Subject.objects.filter(name = 'Room 1')
        #return Department.objects.filter(subject__name = 'Room 1')
        
class ShowDepartmentList(generic.ListView):
    template_name = 'students/departmentlist.html'
    context_object_name = 'department_list'
    
    def get_queryset(self):
        return Department.objects.all()
        
class DepartmentDetail(generic.DetailView):
    model = Department
    template_name = 'students/departmentdetail.html'
    
class ShowSubjectList(generic.ListView):
    template_name = 'students/subjectlist.html'
    context_object_name = 'subject_list'
    
    def get_queryset(self):
        return Subject.subjects.all()
        
class SubjectDetail(generic.DetailView):
    model = Subject
    template_name = 'students/subjectdetail.html'
    
class ShowStudentList(generic.ListView):
    template_name = 'students/studentlist.html'
    context_object_name = 'student_list'
    
    def get_queryset(self):
        return Student.objects.all()
    
class StudentDetail(generic.DetailView):
    model = Student
    template_name = 'students/studentdetail.html'
    

def show_subjects_in_department(request, dept_id):
    template_name = 'students/subjectlist.html'
    subject_list = Subject.subjects.filter(department__dept_id = dept_id)
    return render(request, template_name, {'subject_list': subject_list})

def show_students_in_subject(request, sub_id):
    template_name = 'students/studentlist.html'
    students = Student.objects.filter(subjects__sub_id = sub_id)
    return render(request, template_name, {'student_list': students})
    
def show_trigger_list(request):
    template_name = 'students/objectlist.html'
    trigger_list = Student.objects.get_trigger_table()
    return render(request, template_name, {'object_list':trigger_list})