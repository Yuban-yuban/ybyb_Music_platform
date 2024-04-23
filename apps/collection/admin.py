# 后台admin收藏功能
from django.contrib import admin
from apps.collection.models import Collection
from apps.common.models import Constant
from apps.util.util import Util


# 后台admin的收藏功能类
@admin.register(Collection)  # 将collection类加入后台admin管理
class CollectionAdmin(admin.ModelAdmin):
    # 列表展示字段
    list_display = ['showUsername', 'showMusicname', 'createtime']
    # 列表展示字段添加链接（跳转到详情或者修改页面）
    list_display_links = ['showUsername', 'showMusicname', ]
    # 页表页面的搜索框字段
    search_fields = ['userid__username', 'musicid__musicname']
    # 每页展示的条数
    list_per_page = Constant.pageSizeAdmin
    # 编辑页面需要编辑的字段
    fields = ["userid", "musicid", 'createtime']
    # 编辑页面的只读字段
    readonly_fields = ["userid", "musicid", 'createtime']

    # 列表展示页面，有些字段需要格式化或者显示外键的某些属性，用户外键的用户名
    def showUsername(self, obj):
        return obj.userid.username

    # 设置字段显示的标题
    showUsername.short_description = '用户名'

    # 列表展示页面，有些字段需要格式化或者显示外键的某些属性，音乐外键的电影名
    def showMusicname(self, obj):
        return obj.musicid.musicname

    # 设置字段显示的标题
    showMusicname.short_description = '音乐名称'

