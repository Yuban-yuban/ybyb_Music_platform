"""
前台用户兴趣标签url
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from apps.labelrecord import views

urlpatterns = [
    path('listCommon',views.listCommon),  # 标签公共列表
    path('saveCommon',views.saveCommon),  # 标签公共保存
    path('edit',views.edit),  # 编辑标签
    path('save',views.save),  # 保存标签
]
