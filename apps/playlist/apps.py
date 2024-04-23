# 定义应用程序
from django.apps import AppConfig


class AppsConfig(AppConfig):
    name = 'apps.playlist'
    verbose_name = "5、歌单管理"  # 后台admin首页显现的导航栏，3主要是为了排序
