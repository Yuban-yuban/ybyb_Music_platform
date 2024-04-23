# 后台admin歌单详情管理功能
from django.contrib import admin

from apps.common.models import Constant
from apps.playlistrecord.models import Playlistrecord


@admin.register(Playlistrecord)  # 将Playlistrecord类加入后台admin管理
class PlaylistrecordAdmin(admin.ModelAdmin):
    # 列表展示字段
    list_display = ['playlistid', 'musicid', 'createtime']
    # 页表页面的搜索框字段
    search_fields = ['playlistid__playlistname', 'musicid__musicname']
    # 每页展示的条数
    list_per_page = Constant.pageSizeAdmin
    # 编辑页面需要编辑的字段
    fields = ['playlistid', 'musicid', 'createtime']
    # 编辑页面的只读字段
    readonly_fields = ['playlistid', 'musicid', 'createtime']

