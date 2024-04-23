# 定义应用程序
from django.apps import AppConfig


class AppsConfig(AppConfig):
    name = 'apps.collection'
    verbose_name = "7、收藏记录管理"  # 后台admin首页显现的导航栏，7主要是为了排序
