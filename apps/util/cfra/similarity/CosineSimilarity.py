# 余弦相似度算法模块
# 继承AbstractSimilarity抽象模块
# 余弦算法（计算两个向量的夹角的余弦值）
# 公式：用户A的项目评分*用户B的项目评分之和/（用户A的项目评分的平方之和的开方+用户A的项目评分的平和之和的开方）
from apps.util.cfra.similarity.AbstractSimilarity import AbstractSimilarity
from math import sqrt


class CosineSimilarity(AbstractSimilarity):

    def __init__(self):
        pass

    # 获取两个字典的相似度，字典的键是用户id或者项目id，值是评分
    def getSimilarity(self, dic1, dic2):
        temp = 0
        temp2 = 0
        temp3 = 0
        distance = 0.0
        for itemid, rating in dic1.items():
            if itemid in dic2.keys():
                temp += rating * dic2[itemid]
                temp2 += pow(rating, 2)
                temp3 += pow(dic2[itemid], 2)
        if temp2 != 0.0 and temp3 != 0.0:
            distance = temp / (sqrt(temp2) * sqrt(temp3))
        return distance

