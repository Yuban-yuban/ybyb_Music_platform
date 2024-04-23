# 公共模块常量
import os

from django.db import models


# 定义常量类
from apps.util.util import Util


class Constant(object):

    pageSize = 8  # 前台分页条数

    pageSizeAdmin = 10  # 后台分页条数

    default_user_password = "123456"  # 后台充值密码的默认密码

    default_user_header = "default.jpg"  # 默认头像

    session_user_isLogin = "session_user_isLogin"  # session中保存的登录用户的判断键值

    session_user_id = "session_user_id"  # session中保存的登录用户的主键键值

    session_user_username = "session_user_username"  # session中保存的登录用户的用户名键值

    session_user_header = "session_user_header"  # session中保存的登录用户的头像键值







