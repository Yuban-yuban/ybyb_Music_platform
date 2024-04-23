"""
收藏功能前台url
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from apps.collection import views

urlpatterns = [
    path('save',views.save),  # 添加/取消收藏
    path('list',views.list),  # 收藏列表
]
