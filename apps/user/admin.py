# 后台admin用户功能
from django.contrib import admin, messages
from django.utils.safestring import mark_safe
from WebMusicCFRSPython import settings
from apps.common.models import Constant
from apps.user.models import User
from apps.util.util import Util


# admin.site.register(User)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'createtime']
    search_fields = ['username']
    list_per_page = Constant.pageSizeAdmin
    fields = ["username","email","showHeader",'header']
    # readonly_fields = ["username"]
    readonly_fields = ('showHeader',)
    # 动作集合，重置密码
    actions = ['resetPassword']

    def showHeader(self,obj):
        try:
            header = mark_safe('<img src="%s" width="80px" />' % (obj.header.url,))
        except Exception as e:
            header = mark_safe('<img src="%s" width="80px" />' % (settings.MEDIA_URL+Constant.default_user_header,))
        return header

    showHeader.short_description = "头像展示"

    # 重置密码
    def resetPassword(self, request, queryset):
        queryset.update(password=Constant.default_user_password)
        messages.info(request, "初始密码:%s！" % Constant.default_user_password)

    resetPassword.short_description = "重置用户密码"

    # 重写保存方法
    def save_model(self, request, obj, form, change):
        if change:
            # 修改
            # 判断用户名是否已经存在
            username = obj.username
            userid = obj.id
            users = User.objects.filter(username=username).exclude(id=userid)
            if len(users) > 0:
                messages.error(request, "操作失败！用户名已存在！")
                messages.set_level(request, messages.ERROR)
            else:
                super().save_model(request, obj, form, change)
        else:
            # 添加
            # 判断用户名是否已经存在
            username = obj.username
            users = User.objects.filter(username=username)
            if len(users) > 0:
                messages.error(request, "操作失败！用户名已存在！")
                messages.set_level(request, messages.ERROR)
            else:
                obj.password = Constant.default_user_password
                obj.createtime = Util().getCurrentTime()
                obj.header = Constant.default_user_header
                super().save_model(request, obj, form, change)
                messages.info(request, "初始密码:%s！" % Constant.default_user_password)
                # messages.set_level(request, messages.INFO)





