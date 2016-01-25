# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 08:36:50 2016

@author: sev_user
"""
from django.db import models

        
class ClassManager(models.Manager):

    def get_students_with_Address2(self):
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM students_student WHERE id =1 """)
        result_list = []
        for row in cursor.fetchall():
            p = self.model(id = row[0], name = row[1], code = row[2], address = row[3], joined_date = row[4], average_score = row[5], email = row[6] )
            result_list.append(p)
        return result_list
   
     

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.IntegerField()
    
    def __str__(self):
        return self.name
        

class Student(models.Model):
    name = models.CharField(max_length=100)
    code = models.IntegerField()
    address = models.CharField(max_length=200)
    joined_date = models.DateField()
    average_score = models.FloatField()
    email = models.EmailField(default = 'user@gmail.com')
    objects = ClassManager()
    
    class Meta:
        '''Order by joined_date descending '''
        ordering = ['-joined_date']
    
    def __str__(self):
        return self.name
        
    
class Classroom(models.Model):
    student = models.ManyToManyField(Student)
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    name = models.CharField(max_length=100)
    code = models.IntegerField()
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name