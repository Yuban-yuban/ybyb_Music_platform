"""
前台歌单url
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from apps.playlist import views

urlpatterns = [
    path('save', views.save),  # 歌单添加或修改url
    path('list', views.list),  # 我的歌单列表url
    path('delete', views.delete),  # 删除歌单url
    path('detail', views.detail),  # 歌单详情url
    path('listCommon', views.listCommon),  # 公共个人歌单url
]
