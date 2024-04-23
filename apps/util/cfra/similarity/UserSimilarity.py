# 用户相似度模块


class UserSimilarity(object):

    def __init__(self):
        pass

    # 得到目标用户与其他用户的相似度
    # cUserid 目标用户id
    # abstractSimilarity 相似度算法模块
    # dataModel 矩阵
    def getUserSimilaritys(self, cUserid, abstractSimilarity, dataModel):
        # 获取用户-项目喜好字典
        userItemPrefMatrixDic = dataModel.userItemPrefMatrixDic
        # 定义目标用户与其他用户的相似度字典
        userSimilarityDic = {}
        # 遍历所有用户
        for userid, items in userItemPrefMatrixDic.items():
            # 相同的用户不计算相似度
            if cUserid != userid:
                # 计算目标用户与其他某个用户的相似度
                similarity = abstractSimilarity.getSimilarity \
                    (userItemPrefMatrixDic[cUserid], items)
                # 将相似度保存到目标用户与其他用户的相似度字典
                userSimilarityDic[userid] = similarity
        return userSimilarityDic

    # 输出用户相似度
    def printUserSimilaritys(self,userSimilarityDic):
        for i, val in enumerate(userSimilarityDic):
            print("用户：%-5s  相似度：%-.4f" % (val[0], val[1]), end="     ")
            if (i + 1) % 5 == 0:
                print("")
