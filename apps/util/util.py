# 工具模块
import datetime
import os
from random import randint


class Util(object):

    # 获取当前时间
    def getCurrentTime(self):
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # 获取一个当前时间的随机数，用于新的文件名
    def getCurrentTimeRandom(self):
        return datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S_%f')+"_"+str(randint(1,1000000))

    # 定格文件上传格式化路径和文件名方法
    def upload_path_handler(self,instance, filename):
        fileType = os.path.splitext(filename)[1]  # .jpg  获取文件名后缀
        filename = self.getCurrentTimeRandom() + fileType  # 产生一个随机文件名称
        return "{file}".format(file=filename)  # 保存路径和格式

# print(Util().getCurrentTime())
# 2020-09-25 17:09:39

# print(Util().getCurrentTimeRandom())
