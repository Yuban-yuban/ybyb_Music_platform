# 定义应用程序
from django.apps import AppConfig


class AppsConfig(AppConfig):
    name = 'apps.comment'
    verbose_name = "8、评论记录管理"  # 后台admin首页显现的导航栏，8主要是为了排序
