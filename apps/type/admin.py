# 后台音乐类型模块
from django.contrib import admin
from apps.common.models import Constant
from apps.type.models import Type


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    # 列表展示字段
    list_display = ['typename']
    # 列表展示字段添加链接（跳转到详情或者修改页面）
    search_fields = ['typename']
    # 每页展示的条数
    list_per_page = Constant.pageSizeAdmin
    # 编辑页面需要编辑的字段
    fields = ["typename"]


