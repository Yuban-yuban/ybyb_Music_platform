from django.db import models


class Comment(models.Model):
    # 音乐外键，musicid其实是一个音乐对象
    musicid = models.ForeignKey('music.Music', models.CASCADE,
                                  db_column='musicid', blank=False, null=False, verbose_name="音乐名称")
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
    # 内评论内容实体外键
    parentid = models.ForeignKey('self', models.CASCADE,
                                 db_column='parentid', blank=True, null=True, verbose_name="被评论内容")
    # 评论内容
    content = models.TextField(max_length=255, blank=False, null=False, verbose_name="评论内容")
    createtime = models.CharField(max_length=255, blank=False,
                                  null=False, verbose_name="添加时间")

    # 这个是在后台编辑音乐的时候列表显示父级评论的内容而不是整个对象
    def __str__(self):
        return self.content

    # 这个是在后台编辑电影的时候列表显示父级评论的内容而不是整个对象,同时内容展示截取长度
    def contentShort(self):
        if len(str(self.content)) > 30:
            return '{}...'.format(str(self.content)[0:30])
        else:
            return str(self.content)

    # 定义字段标题
    contentShort.short_description = "评论内容"

    # 嵌套类，主要目的是给上级类添加一些功能，或者指定一些标准
    class Meta:
        # 默认值为True,这个选项为True时Django可以对数据库表进行migrate或migrations、删除等操作
        # 如果为False的时候，不会对数据库表进行创建、删除等操作。可以用于现有表、数据库视图等，其他操作是一样的
        managed = False
        db_table = 'comment'  # 对应的数据库表
        verbose_name_plural = "评论记录"  # 这个选项是指定，模型的复数形式是什么
        verbose_name = "评论记录"  # 给模型类起一个更可读的名字

