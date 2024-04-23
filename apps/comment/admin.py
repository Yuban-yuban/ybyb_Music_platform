# 后台admin评论功能
from django.contrib import admin
from apps.comment.models import Comment
from apps.common.models import Constant
from apps.util.util import Util


# 后台admin的评论功能类
@admin.register(Comment)  # 将comment类加入后台admin管理
class CommentAdmin(admin.ModelAdmin):
    # 列表展示字段
    list_display = ['showUsername', 'showmusicname','contentShort','createtime']
    # 列表展示字段添加链接（跳转到详情或者修改页面）
    list_display_links = ['showUsername', 'showmusicname','contentShort',]
    # 页表页面的搜索框字段
    search_fields = ['userid__username','musicid__musicname']
    # 每页展示的条数
    list_per_page = Constant.pageSizeAdmin
    # 编辑页面需要编辑的字段
    fields = ["userid","musicid",'parentid',"content",'createtime']
    # 编辑页面只读字段
    readonly_fields = ["userid","musicid",'parentid',"content",'createtime']

    # 列表展示页面，有些字段需要格式化或者显示外键的某些属性，用户外键的用户名
    def showUsername(self,obj):
        return obj.userid.username

    # 设置字段显示的标题
    showUsername.short_description = '用户名'

    # 列表展示页面，有些字段需要格式化或者显示外键的某些属性，音乐外键的音乐名
    def showmusicname(self,obj):
        return obj.musicid.musicname

    # 设置字段显示的标题
    showmusicname.short_description = '音乐名称'

    # 重写保存方法，添加或者修改
    def save_model(self, request, obj, form, change):
        if not change:
            # 添加
            obj.createtime = Util().getCurrentTime()  # 添加添加时间
        super().save_model(request, obj, form, change)

