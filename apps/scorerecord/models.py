# 定义评分实体类
from django.db import models

from apps.music.models import Music


class Scorerecord(models.Model):
    # 用户外键
    userid = models.ForeignKey('user.User', models.CASCADE, db_column='userid',
                               blank=False, null=False, verbose_name="用户名")
    # 音乐外键
    musicid = models.ForeignKey(Music, models.CASCADE, db_column='musicid',
                                  blank=False, null=False, verbose_name="音乐名称")
    # 评分
    score = models.IntegerField(blank=False, null=False, verbose_name="评分")
    # 添加时间
    createtime = models.CharField(max_length=255, blank=False, null=False, verbose_name="评分时间")

    class Meta:
        managed = False
        db_table = 'scorerecord'
        verbose_name_plural = "评分记录"  # 这个选项是指定，模型的复数形式是什么
        verbose_name = "评分记录"  # 给模型类起一个更可读的名字
