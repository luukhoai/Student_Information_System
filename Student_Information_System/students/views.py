from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView, View
from students.models import Student, Subject, Department
from django.shortcuts import get_object_or_404, render
from students.forms import StudentForm
from django.http import HttpResponseRedirect, Http404, HttpResponse, HttpResponseNotFound
from django.core.urlresolvers import reverse, reverse_lazy
from django.template.context_processors import csrf
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import SingleObjectMixin


class HomeView(TemplateView):
    template_name = 'students/base.html'


class IndexView(ListView):
    template_name = 'students/departmentlist.html'
    context_object_name = 'department_list'

    def get_queryset(self):
        #return Student.objects.all()
        #return Student.objects.filter(id = 1)
        #return Student.objects.filter(name__startswith = 'Al')
        #return Student.objects.filter(name__iendswith = 'ta')
        #return Student.objects.filter(subjects__sub_name = 'Room 3')
        #return Subject.objects.filter(name = 'Room 1')
        return Department.objects.filter(dept_name='Computer Science')


class ShowDepartmentList(ListView):
    template_name = 'students/departmentlist.html'
    context_object_name = 'department_list'

    def get_queryset(self):
        return Department.objects.all()


class ShowDepartmentListMixin(SingleObjectMixin, ListView):
    paginate_by = 2
    template_name = 'students/departmentlist_mixin.html'
    #context_object_name = 'department_list'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Department.objects.all())
        return super(ShowDepartmentListMixin, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ShowDepartmentListMixin, self).get_context_data(**kwargs)
        context['department'] = self.object
        return context

    def get_queryset(self):
        return self.object.subject_set.all()


class DepartmentDetail(DetailView):
    model = Department
    template_name = 'students/departmentdetail.html'


class ShowSubjectList(ListView):
    template_name = 'students/subjectlist.html'
    context_object_name = 'subject_list'
    
    def get_queryset(self):
        return Subject.subjects.all()


class SubjectDetail(DetailView):
    model = Subject
    template_name = 'students/subjectdetail.html'

    def get_context_data(self, **kwargs):
        context = super(SubjectDetail, self).get_context_data(**kwargs)
        context['student_list'] = Student.objects.all()
        return context


@method_decorator(login_required, name='dispatch')
class ShowStudentList(ListView):
    #template_name = 'students/studentlist.html'
    #context_object_name = 'student_list'
    
    #def get_queryset(self):
    #    return Student.objects.all()

    def get(self, request, *args, **kwargs):
        args = {}
        args.update(csrf(request))
        args['student_list'] = Student.objects.all()
        return render(request, 'students/studentlist.html', args)


class StudentDetail(DetailView):
    model = Student
    template_name = 'students/studentdetail.html'


class StudentCreate(CreateView):
    template_name = 'students/student_form.html'
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('students:studentlist')


class StudentUpdate(UpdateView):
    template_name = 'students/student_form.html'
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('students:studentlist')


class StudentDelete(DeleteView):
    model = Student
    template_name = 'students/student_confirm_delete.html'
    success_url = reverse_lazy('students:studentlist')


class AllSearch(TemplateView):

    def post(self, request, *args, **kwargs):
        search_text = request.POST['search']

        department = Department.objects.filter(dept_name__contains= search_text)
        if department.count():
            return render(request, 'students/departmentlist.html', {"department_list": department})

        subject = Subject.subjects.filter(sub_name__contains=search_text)
        if subject.count():
            return render(request, 'students/subjectlist.html', {"subject_list": subject})

        student = Student.objects.filter(per_name__contains=search_text)
        if student.count():
            return render(request, 'students/studentlist.html', {"student_list":student})

        return HttpResponseNotFound('<h1>Object not found</h1>')


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


def add_student(request):
    if not request.user.username in request.session:
        return HttpResponseRedirect(reverse('accounts:login'))

    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:studentlist'))
    else:
        form = StudentForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render(request, 'students/student_add.html', args)


def save_student(request):
    student = Student.objects.get(pk=1)
    form = StudentForm(request.POST, instance=student)
    form.save()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render(request, 'students/student_add.html', args)
