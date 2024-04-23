# 定义应用程序
from django.apps import AppConfig


class AppsConfig(AppConfig):
    name = 'apps.scorerecord'
    verbose_name = "9、评分记录管理"  # 后台admin首页显现的导航栏，9主要是为了排序
