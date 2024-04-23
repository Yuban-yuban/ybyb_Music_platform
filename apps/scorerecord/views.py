from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render

from apps.common.models import Constant
from apps.scorerecord.models import Scorerecord
from apps.util.util import Util


# 添加评分
def save(request):
    post = request.POST
    musicid = post.get("musicid")
    score = post.get("score")
    userid = request.session[Constant.session_user_id]
    oldScorerecord = Scorerecord.objects.filter(musicid_id=musicid,userid_id=userid)
    scorerecod = Scorerecord()
    if oldScorerecord and len(oldScorerecord) > 0:
        scorerecod = oldScorerecord[0]
    else:
        scorerecod.userid_id = userid
        scorerecod.musicid_id = musicid
        scorerecod.createtime = Util().getCurrentTime()
    scorerecod.score = score
    scorerecod.save()
    data = {  # 返回参数
        "success": 1,  # 1：操作成功
        "url": "reload"  # 重新加载请求的页面
    }
    return JsonResponse(data)


# 评分列表
def list(request):
    page = request.POST.get("page", 1)  # 获取请求的页码，如果不存在就请求第一页
    userid = request.session[Constant.session_user_id]
    scorerecords = Scorerecord.objects.filter(userid_id=userid).order_by("-id")
    paginator = Paginator(scorerecords, Constant.pageSize)
    scorerecords = paginator.page(page)
    data = {  # 返回参数
        "pageBean": scorerecords,
        "page": page,
    }
    return render(request, "scorerecord/list.html", context=data)
