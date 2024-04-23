# 基于用户的协同过滤推荐算法实现模块
import operator
from apps.util.cfra.common.Constant import Constant
from apps.util.cfra.model.DataModel import DataModel
from apps.util.cfra.neighborhood.UserNeighborhood import UserNeighborhood
from apps.util.cfra.recommender.UserRecommender import UserRecommender
from apps.util.cfra.similarity.CosineSimilarity import CosineSimilarity
from apps.util.cfra.similarity.UserSimilarity import UserSimilarity


class UserCF(object):

    def __init__(self):
        pass

    # 推荐方法
    def recommend(self, dataModel, cUserid):
        print("基于用户的协同过滤推荐算法开始")
        # 获取用户id列表
        userIDsList = dataModel.userIDsList

        if len(userIDsList) == 0:
            print("\n暂无评分数据！")
            print("\n基于用户的协同过滤推荐算法结束")
            return None

        # 升序排列
        userIDsList = sorted(userIDsList, reverse=False)
        print("用户数量：%d" % len(userIDsList))
        # 输出用户id列表
        dataModel.printUserIds(userIDsList)

        # 获取项目id列表
        itemIDsList = dataModel.itemIDsList
        # 降序排列
        itemIDsList = sorted(itemIDsList, reverse=False)
        print("\n项目数量：%d" % len(itemIDsList))
        # 输出项目id列表
        dataModel.printItemIds(itemIDsList)

        # 打印用户项目喜好矩阵
        dataModel.printUserItemPrefMatrix(userIDsList,dataModel.userItemPrefMatrixDic)

        # 判断当前用户是否有评分数据
        if cUserid not in dataModel.userItemPrefMatrixDic.keys():
            print("\n当前用户 %s 暂无评分数据！" % cUserid)
            print("\n基于用户的协同过滤推荐算法结束")
            return None

        # 实例化余弦相似度算法
        cosineSimilarity = CosineSimilarity()

        # 实例化用户相似度
        userSimilarity = UserSimilarity()

        # 计算目标用户与其他用户的相似度
        userSimilarityDic = userSimilarity.getUserSimilaritys(cUserid, cosineSimilarity, dataModel)
        # 先根据用户id升序
        userSimilarityDicTemp = sorted(userSimilarityDic.items(), key=operator.itemgetter(0), reverse=False)
        print("\n用户：%-5s与其他用户的相似度为：" % cUserid)
        # 输出目标用户的相似度
        userSimilarity.printUserSimilaritys(userSimilarityDicTemp)

        # 实例化用户邻居对象
        userNeighborhood = UserNeighborhood()
        # 获取目标用户的最近邻居
        kNUserNeighborhood = userNeighborhood.getKUserNeighborhoods(userSimilarityDic)
        print("\n用户：%-5s的前%d个最近邻居为：" % (cUserid, Constant.knn))
        # 输出目标用户的最近邻居
        userNeighborhood.printKUserNeighborhoods(kNUserNeighborhood)

        # 实例化用户推荐对象
        userRecommender = UserRecommender()
        # 推荐
        recommenderItemFinalDic = userRecommender.getUserRecommender(cUserid, dict(kNUserNeighborhood), dataModel)
        print("\n用户：%-5s的前%d个推荐项目为：" % (cUserid, Constant.cfCount))

        recommenderItemFinalDic = sorted(recommenderItemFinalDic.items(), key=operator.itemgetter(1), reverse=True)
        recommenderItemFinalDic = recommenderItemFinalDic[0:Constant.cfCount]
        # 打印预测评分
        userRecommender.printPref(recommenderItemFinalDic)

        print("\n基于用户的协同过滤推荐算法结束")
        return recommenderItemFinalDic
