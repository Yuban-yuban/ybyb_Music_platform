"""
前台播放记录url
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from apps.playrecord import views

urlpatterns = [
    path('save', views.save),  # 添加音乐播放记录
    path('list', views.list),  # 音乐播放记录列表
]
