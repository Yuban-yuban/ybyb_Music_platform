from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render

from apps.common.models import Constant
from apps.playlist.models import Playlist
from apps.playlistrecord.models import Playlistrecord
from apps.user.models import User
from apps.util.util import Util


# 向歌单中添加音乐
def save(request):
    message = ""
    success = 0
    post = request.POST
    musicid = post.get("musicid")
    playlistid = post.get("playlistid")
    oldPlaylistrecord = Playlistrecord.objects.filter(playlistid_id=playlistid,musicid_id=musicid)
    if oldPlaylistrecord:
        message = "操作失败！该歌单中已存在该音乐！"
    else:
        playlistrecord = Playlistrecord()
        playlistrecord.playlistid_id = playlistid
        playlistrecord.musicid_id = musicid
        playlistrecord.createtime = Util().getCurrentTime()
        playlistrecord.save()
        success = 1
    data = {
        "success": success,
        "message": message,
        "url": "reload"
    }
    return JsonResponse(data)


# 删除歌单中的音乐
def delete(request):
    playlistid = request.POST.get("playlistid")
    playlistrecordid = request.POST.get("playlistrecordid")
    Playlistrecord.objects.filter(playlistid_id=playlistid,id=playlistrecordid).delete()
    data = {
        "success": 1,
        "url": "reload"
    }
    return JsonResponse(data)


# 公共歌单详情
def listCommon(request):
    userid = request.GET.get("userid", request.POST.get("userid"))
    playlistid = request.POST.get("playlistid",request.GET.get("playlistid"))
    user = User.objects.get(id=userid)
    playlist = Playlist.objects.get(id=playlistid)
    page = request.POST.get("page", 1)
    playlistrecords = Playlistrecord.objects.filter(playlistid_id=playlistid).order_by("-id")
    paginator = Paginator(playlistrecords, Constant.pageSize)  # 分页
    playlists = paginator.page(page)
    data = {
        "pageBean": playlists,
        "page": page,
        "user": user,
        "playlist": playlist,
    }
    return render(request, "playlistrecord/listCommon.html", context=data)


