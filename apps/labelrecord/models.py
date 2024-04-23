# 定义兴趣标签实体类
from django.db import models


class Labelrecord(models.Model):
    # 用户外键，userid其实是一个用户对象
    # on_delete=None, # 删除关联表中的数据时,当前表与其关联的field的行为
    # on_delete=models.CASCADE, # 删除关联数据,与之关联也删除
    # on_delete=models.DO_NOTHING, # 删除关联数据,什么也不做
    # on_delete=models.PROTECT, 删除关联数据,引发错误ProtectedError
    # blank=False 不能为空数据
    # null=False 数据不能为空
    # verbose_name 列表或者编辑显示的字段描述
    userid = models.ForeignKey('user.User', models.CASCADE,
                               db_column='userid', blank=False, null=False, verbose_name="用户名")
    # 兴趣标签外键
    typeid = models.ForeignKey('type.Type', models.CASCADE, db_column='typeid', blank=False,
                               null=False, verbose_name="兴趣标签名称")
    createtime = models.CharField(max_length=255, blank=False,
                                  null=False, verbose_name="添加时间")

    class Meta:
        managed = False
        db_table = 'labelrecord'
        verbose_name_plural = "兴趣标签"  # 这个选项是指定，模型的复数形式是什么
        verbose_name = "兴趣标签"  # 给模型类起一个更可读的名字
