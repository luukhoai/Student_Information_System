from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from students.managers.subjectManager import SubjectManager
from students.managers.peopleManager import PeopleManager
from time import time
from django.core.urlresolvers import reverse
# Create your models here.


def get_upload_file_name(instance, filename):
    return "uploaded_file/%s_%s" %(str(time()).replace('.', '_'), filename)


class Department(models.Model):
    
    dept_id = models.AutoField(primary_key = True)
    dept_name = models.CharField(max_length = 100)
    dept_code = models.PositiveIntegerField(unique= True)
    
    def __unicode__(self):
        return self.dept_name


class Subject(models.Model):
    
    sub_id = models.AutoField(primary_key = True)
    sub_name = models.CharField(max_length = 100)
    sub_code = models.PositiveIntegerField(unique=True)
    sub_addr = models.CharField(max_length = 100)
    department = models.ForeignKey(Department, on_delete = models.CASCADE)   
    teacher = models.ForeignKey('Teacher', on_delete = models.CASCADE)
    subjects = SubjectManager()
    
    def __unicode__(self):
        return self.sub_name


class People(models.Model):

    ADDRESS = (
        ('Addr1', 'Address 1'),
        ('Addr2', 'Address 2'),
        ('Addr3', 'Address 3'),
        ('Addr4', 'Address 4'),
        ('Addr5', 'Address 5'),
        ('Addr6', 'Address 6'),
        ('Addr7', 'Address 7'),
    )

    per_id = models.AutoField(primary_key = True)
    per_name = models.CharField(max_length =100)
    per_code = models.PositiveIntegerField(unique=True)
    per_addr = models.CharField(max_length = 200, choices=ADDRESS)
    per_email = models.EmailField()
    joined_date = models.DateField()
    picture = models.FileField(upload_to=get_upload_file_name)
    objects = PeopleManager()

    class Meta:
        abstract = True
        
    def __unicode__(self):
        return self.per_name
'''
    def get_absolute_url(self):
        return reverse('students:studentdetail', kwargs={'pk': self.pk})
'''


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
