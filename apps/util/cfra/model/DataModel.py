# 构建用户-项目喜好矩阵/项目-用户喜好矩阵模块

import random
from apps.util.cfra.common.Constant import Constant


class DataModel(object):

    def __init__(self):
        self.userIDsList = []  # 所有用户id列表
        self.itemIDsList = []  # 所有项目id列表
        self.userItemPrefMatrixDic = {}  # 用户-项目喜好矩阵
        self.itemUserPrefMatrixDic = {}  # 项目-用户喜好矩阵

    # 构建用户-项目喜好字典（字典的键是用户id，值也是字典（键是项目id，值是评分等））
    def setUserItemValue(self, userid, itemid, value):
        if userid in self.userItemPrefMatrixDic.keys():
            self.userItemPrefMatrixDic[userid][itemid] = value
        else:
            self.userItemPrefMatrixDic[userid] = {itemid:value}
            self.userIDsList.append(userid)

    # 构建项目-用户喜好字典（字典的键的项目id，值也是字典（键是用户id，值是评分等））
    def setItemUserValue(self,itemid,userid,value):
        if itemid in self.itemUserPrefMatrixDic.keys():
            self.itemUserPrefMatrixDic[itemid][userid] = value
        else:
            self.itemUserPrefMatrixDic[itemid] = {userid:value}
            self.itemIDsList.append(itemid)

    # 划分测试集和训练集
    # dataModel 矩阵
    # rate 比例（0-1）
    def splitDataModel(self, dataModel):
        trainDataModel = DataModel()
        testDataModel = DataModel()
        userItemPrefMatrixDicTemp = dataModel.userItemPrefMatrixDic
        for userid,items in userItemPrefMatrixDicTemp.items():
            for itemid,rating in items.items():
                if random.random() < Constant.trainRate:
                    trainDataModel.setUserItemValue(userid,itemid,rating)
                    trainDataModel.setItemUserValue(itemid,userid,rating)
                else:
                    testDataModel.setUserItemValue(userid, itemid, rating)
                    testDataModel.setItemUserValue(itemid, userid, rating)
        return trainDataModel,testDataModel

    # 打印输出用户id
    def printUserIds(self, userIDsList):
        for i, val in enumerate(userIDsList):
            print("%-5s" % val, end=" ")
            if (i + 1) % 20 == 0:
                print("")

    # 打印输出项目id
    def printItemIds(self, itemIDsList):
        for i, val in enumerate(itemIDsList):
            print("%-5s" % val, end=" ")
            if (i + 1) % 20 == 0:
                print("")

    # 打印用户项目喜好矩阵
    def printUserItemPrefMatrix(self,userIDsList,userItemPrefMatrixDic):
        prefCount = 0
        print("\n")
        for i, val in enumerate(userIDsList):
            print("用户 %s 的喜好："%val)
            values = userItemPrefMatrixDic[val]
            print(values)
            prefCount+= len(values)
        print("喜好数据数量：%s"%prefCount)

