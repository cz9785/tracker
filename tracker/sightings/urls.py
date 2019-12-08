# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 22:54:39 2019

@author: Zhao Chenxi
"""

from django.urls import path

from . import views

app_name='sightings'

urlpatterns=[
    path('', views.sightings_list, name='sightings_list'),
    path('add/',views.Add,name='add'),
    path('stats/',views.stats,name='stats'),
    path('<Unique_Squirrel_Id>/',views.Update,name='update'),
    ]