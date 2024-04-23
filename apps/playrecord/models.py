# 定义播放记录实体类
from django.db import models

from apps.music.models import Music


class Playrecord(models.Model):
    # 用户外键
    userid = models.ForeignKey('user.User', models.CASCADE,
                               db_column='userid', blank=False, null=False, verbose_name="用户名")
    # 音乐外键
    musicid = models.ForeignKey(Music, models.CASCADE,
                                db_column='musicid', blank=False, null=False, verbose_name="音乐名称")
    # 添加时间
    createtime = models.CharField(max_length=255, blank=False, null=False, verbose_name="添加时间")

    class Meta:
        managed = False
        db_table = 'playrecord'
        verbose_name_plural = "播放记录"
        verbose_name = "播放记录"
