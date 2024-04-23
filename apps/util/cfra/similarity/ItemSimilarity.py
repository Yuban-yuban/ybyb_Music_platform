# 项目相似度模块


class ItemSimilarity(object):

    def __init__(self):
        # 定义全局项目-项目相似度字典（字典的键是项目id，值也是一个字典（键是项目id，值是相似度））
        self.itemSimilarityDic = {}

    # 计算项目相似度
    # cUserid 当前目标用户id
    # abstractSimilarity 相似度计算模块
    # dataModel 矩阵
    def getItemSimilaritys(self,cUserid, abstractSimilarity, dataModel):
        # 项目-用户喜好字典
        itemUserPrefMatrixDic = dataModel.itemUserPrefMatrixDic
        # 用户-项目喜好字典
        userItemPrefMatrixDic = dataModel.userItemPrefMatrixDic
        # 当前用户的项目喜好字典
        cUserItemPrefMatrixDic = userItemPrefMatrixDic[cUserid]
        # 遍历所有项目
        for itemidTemp, userTemp in itemUserPrefMatrixDic.items():
            # 只计算目标用户没有喜好的项目
            if itemidTemp in cUserItemPrefMatrixDic.keys():
                continue
            # 遍历当前目标用户的所有项目
            for itemid, _ in cUserItemPrefMatrixDic.items():
                if itemid in self.itemSimilarityDic.keys() \
                        and itemidTemp in self.itemSimilarityDic[itemid].keys():
                    continue
                # 获取两个项目的相似度
                similarity = abstractSimilarity.getSimilarity \
                    (itemUserPrefMatrixDic[itemid], userTemp)
                # 保存项目相似度
                if itemid in self.itemSimilarityDic.keys():
                    self.itemSimilarityDic[itemid][itemidTemp] = similarity
                else:
                    self.itemSimilarityDic[itemid] = {itemidTemp: similarity}
                # 矩阵的对角线上的相似度是一样的
                if itemidTemp in self.itemSimilarityDic.keys():
                    self.itemSimilarityDic[itemidTemp][itemid] = similarity
                else:
                    self.itemSimilarityDic[itemidTemp] = {itemid: similarity}
        return self.itemSimilarityDic

    # 输出目标用户的喜好项目与其他项目的相似度
    def printItemSimilaritys(self,cUserItemPrefMatrixDic,itemSimilarityDic):
        for itemid, _ in cUserItemPrefMatrixDic.items():
            print("\n项目：%-5s与其他项目的相似度为：" % itemid)
            index = 0
            if itemid in itemSimilarityDic.keys() and len(itemSimilarityDic[itemid].items()) > 0:
                for itemdTemp, similarity in itemSimilarityDic[itemid].items():
                    print("项目：%-5s  相似度：%-.4f" % (itemdTemp, similarity), end="     ")
                    if (index + 1) % 5 == 0:
                        print("")
                    index += 1
