# 用户邻居模块
import operator
from apps.util.cfra.common.Constant import Constant


class UserNeighborhood(object):

    def __init__(self):
        pass

    # 获取目标用户的邻居
    # userSimilarityDic 目标用户与其他用户的相似度字典
    def getUserNeighborhoods(self, userSimilarityDic):
        # 按照相似度降序输出目标用户的邻居，返回的对象是列表
        neighborhoods = sorted(userSimilarityDic.items(), key=operator.itemgetter(1), reverse=True);
        return neighborhoods

    # 获取目标用户的最近邻居
    # userSimilarityDic 目标用户与其他用户的相似度字典
    def getKUserNeighborhoods(self, userSimilarityDic):
        # return self.getUserNeighborhoods(userSimilarityDic)[:Constant.knn]
        userNeighborhoodsTemp = self.getUserNeighborhoods(userSimilarityDic)[:Constant.knn]
        return [(key,value) for key,value in userNeighborhoodsTemp if value > 0]

    # 输出目标用户的最近邻居
    def printKUserNeighborhoods(self,kNUserNeighborhood):
        for i, val in enumerate(kNUserNeighborhood):
            print("用户：%-5s  相似度：%-.4f" % (val[0], val[1]), end="     ")
            if (i + 1) % 4 == 0:
                print("")
