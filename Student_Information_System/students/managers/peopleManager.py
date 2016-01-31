# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 15:13:20 2016

@author: Silver Lighting
"""

from django.db import models, connection

class PeopleManager(models.Manager):
    
    def get_trigger_table(self):
        cursor = connection.cursor()
        cursor.execute("""Select trigger.per_id, trigger.entry_date from students_student_audit as trigger""")
        result_list = []
        for row in cursor.fetchall():
            result_list.append([row[0], row[1]])
        return result_list