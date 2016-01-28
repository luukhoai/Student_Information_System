# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 23:46:21 2016

@author: Silver Lighting
"""
from django.db import models, connection

class SubjectManager(models.Manager):
    
    def show_Subject_List_Per_Student(self):
        cursor = connection.cursor()
        cursor.execute("""with temp_data as (select student_id, subject_id, middle_score, final_score from students_student inner join students_score on students_student.per_id = students_score.student_id and students_student.per_name = 'Alpha')
select sub_name, sub_code, sub_addr, middle_score, final_score from students_subject inner join temp_data on students_subject.sub_id = temp_data.subject_id""")
        result_list = []
        for row in cursor.fetchall():
            p = self.model(sub_name = row[0], sub_code= row[1], sub_addr = row[2])
            result_list.append(p)
        return result_list