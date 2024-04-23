# 后台admin播放记录功能
from django.contrib import admin
from apps.common.models import Constant
from apps.playrecord.models import Playrecord
from apps.util.util import Util


# 后台admin的评分功能类
@admin.register(Playrecord)  # 将Playrecord类加入后台admin管理
class PlayrecordAdmin(admin.ModelAdmin):
    # 列表展示字段
    list_display = ['userid', 'musicid', 'createtime']
    # 页表页面的搜索框字段
    search_fields = ['userid__username', 'musicid__musicname']
    # 每页展示的条数
    list_per_page = Constant.pageSizeAdmin
    # 编辑页面需要编辑的字段
    fields = ["userid", "musicid", 'createtime']
    # 编辑页面的只读字段
    readonly_fields = ["userid", "musicid", 'createtime']