"""
前台音乐url
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from apps.music import views

urlpatterns = [
    path('detail', views.detail),  # 音乐详情url
    path('list', views.list),  # 音乐列表url
]
