# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 22:40:12 2016

@author: Silver Lighting
"""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index')
]