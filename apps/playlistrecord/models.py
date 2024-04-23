# 定义歌单详情实体类
from django.db import models
from apps.music.models import Music
from apps.playlist.models import Playlist


class Playlistrecord(models.Model):
    # 歌单外键
    playlistid = models.ForeignKey(Playlist, models.CASCADE, db_column='playlistid',
                                   blank=False, null=False, verbose_name="歌单名称")
    # 音乐外键
    musicid = models.ForeignKey(Music, models.CASCADE, db_column='musicid',
                                blank=False, null=False, verbose_name="音乐名称")
    # 添加时间
    createtime = models.CharField(max_length=255, blank=False, null=False, verbose_name="添加时间")

    class Meta:
        managed = False
        db_table = 'playlistrecord'
        verbose_name_plural = "歌单详情"
        verbose_name = "歌单详情"
