from django.core.paginator import Paginator
from django.shortcuts import render


# 前台首页
from apps.common.models import Constant
from apps.music.models import Music
from apps.scorerecord.models import Scorerecord
from apps.type.models import Type
from apps.util.cfra.ItemCF import ItemCF
from apps.util.cfra.UserCF import UserCF
from apps.util.cfra.SvdCF import SvdCF
from apps.util.cfra.model.DataModel import DataModel


def index(request):
    types = Type.objects.all()  # 所有音乐类型
    musics = Music.objects.all().order_by("-id")  # 获取所有音乐，id降序排列
    paginator = Paginator(musics,8)  # 分页
    musics = paginator.page(1)
    data = {  # 返回参数
        "types": types,
        "musics": musics,
    }

    # 判断用户是否登录
    if request.session.get(Constant.session_user_isLogin, None):
        print('asdasd')
        # 用户已登录
        # 当前登录用户id
        cUserid = request.session.get(Constant.session_user_id)
        # cUserid = request.user.id
        # 所有评分记录
        records = Scorerecord.objects.all()
        # 构建用户项目评分矩阵
        dataModel = setDataModel(records)
        # 基于用户推荐
        userCf = UserCF()
        # 调用推荐算法
        recommenderItemFinalDicBasedUser = userCf.recommend(dataModel, int(cUserid))
        # 查找推荐结果
        userCfMusics = getRecommendMusics(recommenderItemFinalDicBasedUser)
        data["userCfMusics"] = userCfMusics
        print(data["userCfMusics"])

        #================================================================
        #基于SVD推荐
        svdCf = SvdCF()
        # 调用推荐算法
        recommenderItemFinalDicBasedSvd = svdCf.recommend(dataModel, int(cUserid))
        # 查找推荐结果
        svdCfMusics = getRecommendMusics(recommenderItemFinalDicBasedSvd)
        data["svdCfMusics"] = svdCfMusics
        #=================================================================

        # 基于项目推荐
        itemCF = ItemCF()
        # 调用推荐算法
        recommenderItemFinalDicBasedItem = itemCF.recommend(dataModel, int(cUserid))
        # 查找推荐结果
        itemCfMusics = getRecommendMusics(recommenderItemFinalDicBasedItem)
        data["itemCfMusics"] = itemCfMusics
        #print(data)

    else:
        # 用户没有登录，进行热点推荐
        # 根据被收藏数量，降序推荐
        sql = " select m.id,m.musicname,m.image,m.typeid,count(c.musicid) from music as m " \
              "     join collection as c " \
              "     on m.id = c.musicid " \
              "     group by c.musicid " \
              "     order by count(c.musicid) desc limit 0,4"
        hotMusics = Music.objects.raw(sql)
        data["hotMusics"] = hotMusics

    return render(request,"index/index.html",context=data)


# 构建用户-项目评分矩阵
def setDataModel(records):
    dataModel = DataModel()
    for record in records:
        # 构建用户-项目评分字典
        dataModel.setUserItemValue(record.userid_id, record.musicid_id, float(record.score))
        # 构建项目-用户评分字典
        dataModel.setItemUserValue(record.musicid_id, record.userid_id, float(record.score))
    return dataModel


# 查找推荐结果
def getRecommendMusics(recommenderItemFinalDic):
    # 查找推荐结果
    if (recommenderItemFinalDic is not None) and (len(recommenderItemFinalDic) > 0):
        cfMusicidsList = list()
        for cfMusicid, pre in recommenderItemFinalDic:
            cfMusicidsList.append(int(cfMusicid))
        # 查询推荐的音乐数据
        return Music.objects.filter(id__in=cfMusicidsList)
    else:
        return None

