# 基于用户的推荐器模块
# 预测评分公式：目标用户的平均评分+（（最近邻用户的评分-目标用户的平均评分）*用户相似度/(用户相似度之和)）


class UserRecommender(object):

    def __init__(self):
        pass

    # 获取目标用户的推荐项目
    # cUserid 目标用户id
    # kNUserNeighborhood 最近邻居字典
    # dataModel 矩阵
    def getUserRecommender(self,cUserid,kNUserNeighborhood,dataModel):
        # 获取用户-项目喜好字典
        userItemPrefMatrixDic = dataModel.userItemPrefMatrixDic
        # 目标用户的评分之和
        sumRating = 0.0
        # 遍历目标用户的所有评分
        for _, rating in userItemPrefMatrixDic[cUserid].items():
            sumRating += rating
        # 目标用户的平均评分
        avgRating = sumRating / len(userItemPrefMatrixDic[cUserid].items())
        # 定义目标用户的推荐项目字典（字典的值是项目id，键是字典类型（键是用户id，值是评分））
        recommenderItemDic = {}
        # 遍历目标用户的最近邻居
        for userid, _ in kNUserNeighborhood.items():
            # 遍历最近邻用户的所有评分
            for itemid, rating in userItemPrefMatrixDic[userid].items():
                # 这里的判断是只计算和目标用户有共同评分的项目
                if itemid not in userItemPrefMatrixDic[cUserid].keys():
                    if itemid not in recommenderItemDic.keys():
                        recommenderItemDic[itemid] = {userid:rating}
                    else:
                        recommenderItemDic[itemid][userid] = rating
        # 定义目标用户的最终推荐项目字典（字典的值是项目id，键是预测评分）
        recommenderItemFinalDic = {}
        # 遍历目标用户的推荐项目字典
        for itemid, users in recommenderItemDic.items():
            # 至少有两个用户推荐才能计算预测评分
            if len(users) > 1:
                temp1 = 0.0
                temp2 = 0.0
                # 遍历推荐的用户
                for userid, rating in users.items():
                    temp1 += kNUserNeighborhood[userid] * (rating - avgRating)
                    temp2 += kNUserNeighborhood[userid]
                # 预测值
                prefValue = avgRating + temp1 / temp2
                recommenderItemFinalDic[itemid] = prefValue
        return recommenderItemFinalDic

    # 打印预测评分
    def printPref(self,recommenderItemFinalDic):
        for i, val in enumerate(recommenderItemFinalDic):
            print("项目：%-5s  预测评分：%-.4f" % (val[0], val[1]), end="     ")
            if (i + 1) % 4 == 0:
                print("")