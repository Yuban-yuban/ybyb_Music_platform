# 定义歌单实体类
from django.db import models


class Playlist(models.Model):
    # 歌单名称
    playlistname = models.CharField(max_length=255, blank=False, null=False, verbose_name="歌单名称")
    # 用户外键
    userid = models.ForeignKey('user.User', models.CASCADE,
                               db_column='userid', blank=False, null=False, verbose_name="用户名")
    # 添加时间
    createtime = models.CharField(max_length=255, blank=False, null=False, verbose_name="添加时间")

    # 这个是在后台编辑音乐的时候列表显示歌单名称而不是整个对象
    def __str__(self):
        return self.playlistname

    class Meta:
        managed = False
        db_table = 'playlist'
        verbose_name_plural = "歌单"
        verbose_name = "歌单"
