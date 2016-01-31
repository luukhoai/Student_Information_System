from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from students.managers.subjectManager import SubjectManager
from students.managers.peopleManager import PeopleManager
# Create your models here.

@python_2_unicode_compatible
class Department(models.Model):
    
    dept_id = models.AutoField(primary_key = True)
    dept_name = models.CharField(max_length = 100)
    dept_code = models.PositiveIntegerField(unique= True)
    
    def __str__(self):
        return self.dept_name

@python_2_unicode_compatible
class Subject(models.Model):
    
    sub_id = models.AutoField(primary_key = True)
    sub_name = models.CharField(max_length = 100)
    sub_code = models.PositiveIntegerField(unique=True)
    sub_addr = models.CharField(max_length = 100)
    department = models.ForeignKey(Department, on_delete = models.CASCADE)   
    teacher = models.ForeignKey('Teacher', on_delete = models.CASCADE)
    subjects = SubjectManager()
    
    def __str__(self):
        return self.sub_name

@python_2_unicode_compatible
class People(models.Model):

    per_id = models.AutoField(primary_key = True)
    per_name = models.CharField(max_length =100)
    per_code = models.PositiveIntegerField(unique=True)
    per_addr = models.CharField(max_length = 200)
    per_email = models.EmailField()
    joined_date = models.DateField()
    objects = PeopleManager()

    class Meta:
        abstract = True
        
    def __str__(self):
        return self.per_name


class Student(People):
    
    average_score = models.FloatField()
    subjects = models.ManyToManyField(Subject, through = 'Score', related_name = "%(app_label)s_%(class)s_related")
    
    def get_score(self):
        return [self.average_score]
    
class Teacher(People):
    
    salary = models.PositiveIntegerField(default = 100)
    #classroom = models.OneToOneField(Classroom, on_delete = models.CASCADE, related_name = '%(class)s_students_teacher')

class Score(models.Model):
    
    student = models.ForeignKey(Student, on_delete = models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete = models.CASCADE)    
    middle_score = models.FloatField(default=0)
    final_score = models.FloatField(default=0)
