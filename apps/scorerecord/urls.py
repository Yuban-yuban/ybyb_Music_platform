"""
评分功能前台url
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from apps.scorerecord import views

urlpatterns = [
    path('save',views.save),  # 添加评分
    path('list',views.list),  # 评分列表
]
