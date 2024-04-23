# 定义音乐实体类
from django.db import models
from apps.util.util import Util


class Music(models.Model):
    # 音乐名称
    musicname = models.CharField(max_length=255, blank=False, null=False, verbose_name="音乐名称")
    # 音乐类型外键
    typeid = models.ForeignKey('type.Type', models.CASCADE,
                               db_column='typeid', blank=False, null=False, verbose_name="音乐类型")
    # image = models.CharField(max_length=255, blank=True, null=True)
    # 图片字段
    image = models.ImageField(upload_to=Util().upload_path_handler,
                              blank=False, null=False, verbose_name="音乐封面")
    # 歌手
    singer = models.CharField(max_length=255, blank=False, null=False, verbose_name="歌手")
    # 歌词
    lyric = models.TextField(blank=False, null=False,max_length=2000, verbose_name="歌词")
    # url = models.CharField(max_length=255, blank=True, null=True)
    # mp3
    url = models.FileField(upload_to=Util().upload_path_handler,
                              blank=False, null=False, verbose_name="音乐MP3")
    # 添加时间
    createtime = models.CharField(max_length=255, blank=False, null=False, verbose_name="添加时间")
    # 网络id
    wid = models.CharField(max_length=255, blank=True, null=True)

    # 这个是在后台编辑音乐的时候列表显示音乐名称而不是整个对象
    def __str__(self):
        return self.musicname

    class Meta:
        managed = False
        db_table = 'music'
        verbose_name_plural = "音乐"
        verbose_name = "音乐"
