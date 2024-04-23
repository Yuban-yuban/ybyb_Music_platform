"""
前台歌单记录url
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from apps.playlistrecord import views

urlpatterns = [
    path('save', views.save),  # 向歌单中添加音乐
    path('delete', views.delete),  # 删除歌单中的音乐
    path('listCommon', views.listCommon),  # 公共歌单详情
]
