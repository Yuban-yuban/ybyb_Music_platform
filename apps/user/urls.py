"""
前台用户url
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from apps.user import views

urlpatterns = [
    path('detailCommon',views.detailCommon),  # 用户详情
    path('edit',views.edit),  # 用户编辑
    path('doEdit',views.doEdit),  # 保存用户编辑
    path('password',views.password),  # 重置密码
    path('doPassword',views.doPassword),  # 保存重置密码
]
