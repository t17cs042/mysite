'''
Created on 2019/10/30

@author: t17cs042
'''
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]