# 基于项目的协同过滤推荐算法实现模块
import operator
from apps.util.cfra.common.Constant import Constant
from apps.util.cfra.model.DataModel import DataModel
from apps.util.cfra.recommender.ItemRecommender import ItemRecommender
from apps.util.cfra.similarity.CosineSimilarity import CosineSimilarity
from apps.util.cfra.similarity.ItemSimilarity import ItemSimilarity


class ItemCF(object):

    def __init__(self):
        pass

    # 推荐方法
    def recommend(self, dataModel, cUserid):
        print("基于项目的协同过滤推荐算法开始")

        #############################################
        # 获取项目id列表
        itemIDsList = dataModel.itemIDsList
        # 降序排列
        itemIDsList = sorted(itemIDsList,reverse=False)
        print("项目数量：%d"%len(itemIDsList))
        # 输出项目id列表
        dataModel.printItemIds(itemIDsList)

        # 获取用户id列表
        userIDsList = dataModel.userIDsList
        # 升序排列
        userIDsList = sorted(userIDsList,reverse=False)
        print("\n用户数量：%d"%len(userIDsList))
        # 输出用户id列表
        dataModel.printUserIds(userIDsList)
        ##################################################
        
        if len(dataModel.userIDsList) == 0:
            print("\n暂无评分数据！")
            print("\n基于项目的协同过滤推荐算法结束")
            return None

        # 判断当前用户是否有评分数据
        if cUserid not in dataModel.userItemPrefMatrixDic.keys():
            print("\n当前用户 %s 暂无评分数据！" % cUserid)
            print("\n基于项目的协同过滤推荐算法结束")
            return None

        # 实例化余弦相似度算法
        cosineSimilarity = CosineSimilarity()
        # 实例化项目相似度
        itemSimilarity = ItemSimilarity()
        print("\n计算项目之间的相似度...")
        # 计算项目之间的相似度
        itemSimilarityDic = itemSimilarity.getItemSimilaritys(cUserid, cosineSimilarity, dataModel)
        # 用户-项目喜好矩阵
        userItemPrefMatrixDic = dataModel.userItemPrefMatrixDic
        # 获取当前目标用户喜好的项目
        cUserItemPrefMatrixDic = userItemPrefMatrixDic[cUserid]
        # 输出目标用户的喜好项目与其他项目的相似度
        itemSimilarity.printItemSimilaritys(cUserItemPrefMatrixDic,itemSimilarityDic)

        # 实例化项目推荐对象
        itemRecommender = ItemRecommender()
        # 推荐
        recItemDic = itemRecommender.getItemRecommender(cUserid, itemSimilarityDic, dataModel)
        # 计算当前用户前N个推荐项目的预测喜好
        recItemDic = sorted(recItemDic.items(), key=operator.itemgetter(1), reverse=True)[0:Constant.cfCount]
        print("\n用户：%-5s的前%d个推荐项目为："%(cUserid,Constant.cfCount))
        # 输出当前用户前N个推荐项目的预测喜好
        itemRecommender.printPref(recItemDic)

        print("\n基于项目的协同过滤推荐算法结束")
        return recItemDic



