# 后台admin歌单管理功能
from django.contrib import admin

from apps.common.models import Constant
from apps.playlist.models import Playlist


@admin.register(Playlist)  # 将Playlist类加入后台admin管理
class PlaylistAdmin(admin.ModelAdmin):
    # 列表展示字段
    list_display = ['userid', 'playlistname', 'createtime']
    # 页表页面的搜索框字段
    search_fields = ['userid__username', 'playlistname']
    # 每页展示的条数
    list_per_page = Constant.pageSizeAdmin
    # 编辑页面需要编辑的字段
    fields = ['userid', 'playlistname', 'createtime']
    # 编辑页面的只读字段
    readonly_fields = ['userid', 'playlistname', 'createtime']


