# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 21:14:18 2016

@author: Silver Lighting
"""
from django.conf.urls import url
from django.views.generic import TemplateView
from views import PublisherList

app_name = 'books'
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name = 'books/index.html')),
    url(r'^publishers/$', PublisherList.as_view()),
]