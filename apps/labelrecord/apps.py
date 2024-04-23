# 定义应用程序
from django.apps import AppConfig


class AppsConfig(AppConfig):
    name = 'apps.labelrecord'
    verbose_name = "4、兴趣标签管理"  # 后台admin首页显现的导航栏，4主要是为了排序
