# 定义应用程序
from django.apps import AppConfig


class AppsConfig(AppConfig):
    name = 'apps.music'
    verbose_name = "3、音乐管理"  # 后台admin首页显现的导航栏，3主要是为了排序
