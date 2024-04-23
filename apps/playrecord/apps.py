# 定义应用程序
from django.apps import AppConfig


class AppsConfig(AppConfig):
    name = 'apps.playrecord'
    verbose_name = "9、播放记录管理"  # 后台admin首页显现的导航栏，10主要是为了排序
