# 后台admin音乐管理功能
import os

from django.contrib import admin, messages
from django.contrib.admin import SimpleListFilter
from django.utils.safestring import mark_safe
from apps.common.models import Constant
from apps.music.models import Music
from apps.type.models import Type
from apps.util.util import Util


@admin.register(Music)  # 将music类加入后台admin管理
class MusicAdmin(admin.ModelAdmin):
    # 列表展示字段
    list_display = ['musicname', 'showTypename','singer','createtime']
    # 页表页面的搜索框字段
    search_fields = ['musicname']
    # 每页展示的条数
    list_per_page = Constant.pageSizeAdmin
    # 编辑页面需要编辑的字段
    fields = ["musicname","typeid",'singer',"showImage","image","showUrl","url","lyric"]
    # 编辑页面的只读字段
    readonly_fields = ["showImage","showUrl",]
    # 列表页面的过滤器过滤字段
    list_filter = ('typeid',)

    # 列表展示页面，有些字段需要格式化或者显示外键的某些属性，类型外键的类型名
    def showTypename(self,obj):
        return obj.typeid.typename

    # 设置字段显示的标题
    showTypename.short_description = '音乐类型'

    # 编辑页面，有些字段需要格式化或者显示外键的某些属性，音乐封面
    def showImage(self,obj):
        try:
            image = mark_safe('<img src="%s" width="80px" />' % (obj.image.url,))
        except Exception as e:
            image = ''
        return image

    # 设置字段显示的标题
    showImage.short_description = "图片展示"

    # 编辑页面，有些字段需要格式化或者显示外键的某些属性，音乐Mp3
    def showUrl(self, obj):
        try:
            url = mark_safe('<a href="%s" target="_black">下载</a>' % (obj.url.url,))
        except Exception as e:
            url = ''
        return url

    # 设置字段显示的标题
    showUrl.short_description = "音乐MP3展示"

    # 重写保存方法
    def save_model(self, request, obj, form, change):
        if not change:
            # 添加
            obj.createtime = Util().getCurrentTime()
        url = obj.url
        fileName = url.name
        fileType = os.path.splitext(fileName)[1]  # .mp3  获取文件名后缀
        if not fileType == ".mp3":
            messages.error(request, "操作失败！音乐格式必须是mp3！")
            messages.set_level(request, messages.ERROR)
        else:
            super().save_model(request, obj, form, change)
