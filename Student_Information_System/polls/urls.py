# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 22:40:12 2016

@author: Silver Lighting
"""

from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    #url(r'^$', views.index, name='index'),
    #url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    #url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    #url(r'^loadtemplate/$', views.loadTemplate, name="loadTemplate"),

    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views)
]