from django.core import validators
from django.db import models
from apps import user
from apps.util.util import Util


class User(models.Model):
    # 设置null=True，则仅表示在数据库中该字段可以为空，
    # 但使用后台管理添加数据时仍然要需要输入值，因为Django自动做了数据验证不允许字段为空
    # 想要在Django中也可以将字段保存为空值，则需要添加另一个参数：blank=True
    username = models.CharField(max_length=255, blank=False, null=False,verbose_name="用户名")
    password = models.CharField(max_length=255, blank=False, null=False,verbose_name="密码")
    email = models.CharField(max_length=255, blank=True, null=True,
                             validators=[validators.EmailValidator(message="邮箱格式不正确！")],verbose_name="邮箱")
    # header = models.CharField(max_length=255, blank=True, null=True)
    header = models.ImageField(upload_to=Util().upload_path_handler
                               , blank=True,null=False,verbose_name="头像")
    createtime = models.CharField(max_length=50, blank=False, null=False,verbose_name="注册时间")

    # 这个是在后台编辑电影的时候列表显示类型名称而不是整个对象
    def __str__(self):
        return self.username

    class Meta:
        managed = False
        db_table = 'user'
        verbose_name_plural = "前台用户"
        verbose_name = "前台用户"
        # 设置默认权限为空
        # default_permissions = ()
        # 以下是添加自定义的权限
        """permissions = (
            ("change_user_self", "修改前台用户"),
            ("delete_user_self", "删除前台用户"),
            ("view_user_self", "查看前台用户"),
        )"""


