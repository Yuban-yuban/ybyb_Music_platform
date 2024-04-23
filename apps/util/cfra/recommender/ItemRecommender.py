# 基于项目的推荐器模块
# 预测评分公式：目标用户未评分项目与推荐项目的相似度*推荐项目评分，之和/相似度之和


class ItemRecommender(object):

    def __init__(self):
        pass

    # 获取基于项目的推荐项目
    # cUserid 目标用户
    # itemSimilarityDic 项目-项目相似度字典
    # dataModel 矩阵
    def getItemRecommender(self, cUserid, itemSimilarityDic, dataModel):
        # 项目-用户喜好字典
        itemUserPrefMatrixDic = dataModel.itemUserPrefMatrixDic
        # 用户-项目喜好字典
        userItemPrefMatrixDic = dataModel.userItemPrefMatrixDic
        # 目标用户的所有项目喜好
        cUserItemPrefMatrixDic = userItemPrefMatrixDic[cUserid]
        # 初始化推荐项目字典（字典的键是项目，值是预测评分）
        recItemDic = {}
        # 遍历所有项目
        for itemid, userTemp in itemUserPrefMatrixDic.items():
            # 需要是目标用户没有喜好的项目
            if itemid not in cUserItemPrefMatrixDic.keys():
                temp = 0
                temp1 = 0
                # 遍历目标用户的所有项目
                for itemidTemp, rating in cUserItemPrefMatrixDic.items():
                    temp += rating * itemSimilarityDic[itemidTemp][itemid]
                    temp1 += itemSimilarityDic[itemidTemp][itemid]
                recItemDic[itemid] = temp / temp1 if temp1 > 0 else 0.0
        return recItemDic

    def printPref(self,recItemDic):
        for i, val in enumerate(recItemDic):
            print("项目：%-5s  预测评分：%-.4f" % (val[0], val[1]), end="     ")
            if (i + 1) % 4 == 0:
                print("")
