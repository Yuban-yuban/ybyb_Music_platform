from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render

from apps.common.models import Constant
from apps.playrecord.models import Playrecord
from apps.util.util import Util


# 添加音乐播放记录
def save(request):
    musicid = request.POST.get("musicid")
    userid = request.session.get(Constant.session_user_id)
    playrecord = Playrecord()
    playrecord.userid_id = userid
    playrecord.musicid_id = musicid
    playrecord.createtime = Util().getCurrentTime()
    playrecord.save()
    data = {
        "success": 1,
    }
    return JsonResponse(data)


# 音乐播放记录列表
def list(request):
    page = request.POST.get("page",1)
    userid = request.session.get(Constant.session_user_id)
    playrecords = Playrecord.objects.filter(userid_id=userid).order_by("-id")
    paginator = Paginator(playrecords, Constant.pageSize)  # 分页
    playrecords = paginator.page(page)
    data = {
        "pageBean": playrecords,
        "page": page,
    }
    return render(request, "playrecord/list.html", context=data)


