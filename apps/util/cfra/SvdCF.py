# 基于项目的协同过滤推荐算法实现模块
import operator
from apps.util.cfra.common.Constant import Constant
from apps.util.cfra.model.DataModel import DataModel
from apps.util.cfra.recommender.ItemRecommender import ItemRecommender
from apps.util.cfra.similarity.CosineSimilarity import CosineSimilarity
from apps.util.cfra.similarity.ItemSimilarity import ItemSimilarity
import pandas as pd


class SvdCF(object):

    def __init__(self):
        pass

    # 推荐方法
    def recommend(self, dataModel, cUserid):
        print("基于奇异值分解的推荐算法开始")

        #############################################
        print(dataModel.userItemPrefMatrixDic)
        print(type(dataModel.userItemPrefMatrixDic))
        print(type(dataModel))
        #############################################
        # 假设这是输入的字典A
        # 字典A的结构示例：{用户id1: {项目id1: 评分1, 项目id2: 评分2}, 用户id2: {项目id1: 评分3, 项目id3: 评分4}, ...}
        # 示例数据
        A = dataModel.userItemPrefMatrixDic
        # 提取所有的用户id和项目id
        user_ids = sorted(A.keys())
        item_ids = sorted(set().union(*[set(B.keys()) for B in A.values()]))

        # 创建一个连续的整数序列作为新的用户id和项目id
        new_user_ids = list(range(1, max(user_ids) + 1))
        new_item_ids = list(range(1, max(item_ids) + 1))

        # 创建一个以新用户id为列索引，新项目id为行索引的DataFrame，初始值为0，数据类型为float
        df = pd.DataFrame(0.0, index=new_item_ids, columns=new_user_ids, dtype=float)

        # 填充评分
        for user_id, ratings in A.items():
            for item_id, rating in ratings.items():
                df.at[item_id, user_id] = float(rating)  # 确保评分被转换为浮点型

        # 输出最终的DataFrame
        print(df)
        # 交换行和列索引，即行变成原来的列，列变成原来的行
        df_transposed = df.T

        # 打印转置后的DataFrame
        print(df_transposed)

        import numpy as np

        # 将DataFrame转换为ndarray
        ndarray_matrix = df_transposed.values

        # 只取中间的评分值，即去除行和列的索引
        # 假设您想要去除的是第一行和第一列（通常是索引列和行）
        # 如果您想要去除的是其他行和列，请相应地调整切片

        # 打印转换后的ndarray
        print(ndarray_matrix)

        '''
        def excel_to_Matrix(path):
            # 读excel数据转为矩阵函数
            data = xlrd.open_workbook(path)
            table = data.sheets()[0]
            # 获取excel中第一个sheet表
            nrows = table.nrows
            # 行数
            ncols = table.ncols
            # 列数
            datamatrix = np.zeros((nrows, ncols))
            for x in range(ncols):
                cols = table.col_values(x)
                cols1 = np.matrix(cols)
                # 把list转换为矩阵进行矩阵操作
                datamatrix[:, x] = cols1
                # 把数据进行存储
            return datamatrix
        '''

        sourceData = ndarray_matrix

        def cosSim(vector_1, vector_2):
            dotProd = float(np.dot(vector_1.T, vector_2))
            normProd = np.linalg.norm(vector_1) * np.linalg.norm(vector_2)
            return 0.5 + 0.5 * (dotProd / normProd)

        def estimateScore(sourceData, sourceDataRC, userIndex, itemIndex):
            n = np.shape(sourceData)[1]
            # 获取菜品总数
            scoreMutipleCosSimSum = 0
            # 加权相似度之和
            cosSimSum = 0
            # itemIndex菜品与其他菜品两两相似度之和
            for i in range(n):
                userScore = sourceData[userIndex, i]
                if userScore == 0 or i == itemIndex:
                    continue
                weight = cosSim(sourceDataRC[:, i], sourceDataRC[:, itemIndex])
                # 利用SVD后的矩阵
                # itemIndex与第i个菜品的相似度
                cosSimSum = float(cosSimSum + weight)
                scoreMutipleCosSimSum = scoreMutipleCosSimSum + userScore * weight
            if cosSimSum == 0:
                return 0
            return scoreMutipleCosSimSum / cosSimSum

        U, sigma, VT = np.linalg.svd(sourceData)
        sigmaSum = 0
        k_num = 0

        for k in range(len(sigma)):
            sigmaSum = sigmaSum + sigma[k] * sigma[k]
            if float(sigmaSum) / float(np.sum(sigma ** 2)) > 0.9:
                k_num = k + 1
                break
        sigma_k = np.mat(np.eye(3) * sigma[:3])
        sourceDataRC = sigma_k * U.T[:3, :] * sourceData

        n = np.shape(sourceData)[1]
        userIndex = 26
        for i in range(n):
            userScore = sourceData[userIndex, i]
            if userScore != 0:
                continue
            print("index:{},score:{}".format(i, estimateScore(sourceData, sourceDataRC, userIndex, i)))

        # 假设我们想要输出前5个评分最高的项目
        top_n = 4

        # 创建一个列表来存储项目ID和对应的估计评分
        item_scores = []

        # 遍历所有项目，计算估计评分
        for i in range(n):
            if sourceData[userIndex, i] == 0:  # 检查用户是否未评分
                score = estimateScore(sourceData, sourceDataRC, userIndex, i)
                # 确保预估评分不是nan值
                if not np.isnan(score):
                    item_scores.append((i, score))

        # 根据估计评分对项目进行排序
        item_scores.sort(key=lambda x: x[1], reverse=True)

        # 输出指定数量的评分最高的项目ID和评分
        print("Top {} recommended items for user {}:".format(top_n, userIndex))
        for rank, (item_id, score) in enumerate(item_scores[:top_n]):
            print("Rank {}: Item ID={}, Score={}".format(rank + 1, item_id, score))
            print(item_scores[rank])

        item_scores.sort(key=lambda x: x[1], reverse=True)

        # 提取前top_n个评分最高的项目
        top_items = item_scores[:top_n]

        # 创建一个列表套元组的格式来存储项目ID和评分
        recommended_items = [(item_id+1, score) for item_id, score in top_items]

        # 输出推荐项目的列表套元组格式
        print("Recommended items and scores:")
        print(recommended_items)
        return recommended_items
        '''
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
        print(type(recItemDic))
        print(recItemDic)
        return recItemDic
        '''



