# 定义音乐类型实体类
from django.db import models


class Type(models.Model):
    # 音乐名称
    typename = models.CharField(max_length=255, blank=False, null=False,verbose_name="类型名称")
    # 添加时间
    createtime = models.CharField(max_length=255, blank=False, null=False, verbose_name="添加时间")

    # 这个是在后台编辑的时候列表显示类型的名称而不是整个对象
    def __str__(self):
        return self.typename

    class Meta:
        managed = False
        db_table = 'type'
        verbose_name_plural = "音乐类型"
        verbose_name = "音乐类型"


