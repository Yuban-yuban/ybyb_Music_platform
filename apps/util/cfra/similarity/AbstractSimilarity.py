# 相似度算法基础抽象模块

import abc


class AbstractSimilarity(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def getSimilarity(self,dic1,dic2):
        pass
