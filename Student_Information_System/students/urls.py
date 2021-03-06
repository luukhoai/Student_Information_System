# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 16:41:43 2016

@author: sev_user
"""

from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

app_name = 'students'
urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^index/$', views.IndexView.as_view(), name='index'),
    url(r'^department/$', views.ShowDepartmentList.as_view(), name='departmentlist'),
    url(r'^departmentmixin/(?P<pk>[0-9]+)/$', views.ShowDepartmentListMixin.as_view(), name='departmentlistmixin'),
    url(r'^department/(?P<pk>[0-9]+)/$', views.DepartmentDetail.as_view(), name='departmentdetail'),
    url('^department/subject/(?P<dept_id>[0-9]+)/$', views.show_subjects_in_department, name='subjectindept'),
    url(r'^subject/$', views.ShowSubjectList.as_view(), name='subjectlist'),
    url(r'^subject/(?P<pk>[0-9]+)/$', views.SubjectDetail.as_view(), name='subjectdetail'),
    url(r'^subject/student/(?P<sub_id>[0-9]+)/$', views.show_students_in_subject, name='studentsinsubject'),
    url(r'^student/$', views.ShowStudentList.as_view(), name='studentlist'),
    #url(r'^student/(?P<pk>[0-9]+)/$', views.StudentDetail.as_view(), name='studentdetail'),
    url(r'^student/triggerlist/$', views.show_trigger_list, name='triggerlist'),
    #url(r'^student/create/$', views.add_student, name='student_add'),
    url(r'^student/create/$', views.StudentCreate.as_view(), name='student_create'),
    url(r'^student/(?P<pk>[0-9]+)/$', views.StudentUpdate.as_view(), name='student_update'),
    url(r'^student/delete/(?P<pk>[0-9]+)/$', views.StudentDelete.as_view(), name='student_delete'),
    url(r'^search/$', views.AllSearch.as_view(), name='search'),
]