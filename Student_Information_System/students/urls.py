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
    url(r'^$', views.IndexView.as_view(), name = 'index'),
    url(r'^objectlist/$', views.ShowObjectList.as_view(), name = 'objectlist'),
]