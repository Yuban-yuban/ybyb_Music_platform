# 后台admin兴趣标签功能
from django.contrib import admin
from apps.common.models import Constant
from apps.labelrecord.models import Labelrecord
from apps.util.util import Util


# 后台admin的兴趣标签功能类
@admin.register(Labelrecord)  # Labelrecord
class LabelrecordAdmin(admin.ModelAdmin):
    # 列表展示字段
    list_display = ['userid', 'typeid', 'createtime']
    # 页表页面的搜索框字段
    search_fields = ['userid__username']
    # 每页展示的条数
    list_per_page = Constant.pageSizeAdmin
    # 编辑页面需要编辑的字段
    fields = ["userid", "typeid", 'createtime']
    # 编辑页面的只读字段
    readonly_fields = ["userid", "typeid", 'createtime']
    # 列表页面的过滤器过滤字段
    list_filter = ('typeid',)
