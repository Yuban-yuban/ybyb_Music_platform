from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render

from apps.common.models import Constant
from apps.playlist.models import Playlist
from apps.playlistrecord.models import Playlistrecord
from apps.user.models import User
from apps.util.util import Util


# 保存或者更新操作
def save(request):
    post = request.POST
    message = ""
    success = 0
    playlistid = post.get("playlistid")
    playlistname = post.get("playlistname")
    userid = request.session.get(Constant.session_user_id)
    if playlistid:
        oldPlaylist = Playlist.objects.get(id=playlistid)
        oldPlaylists = Playlist.objects.filter(playlistname=playlistname,userid_id=userid).exclude(id=playlistid)
        if oldPlaylists or len(oldPlaylists) > 0:
            message = "操作失败！歌单名称已存在！"
        else:
            oldPlaylist.playlistname = playlistname
            oldPlaylist.save()
            success = 1
    else:
        oldPlaylists = Playlist.objects.filter(playlistname=playlistname,userid_id=userid)
        if oldPlaylists or len(oldPlaylists) > 0:
            message = "操作失败！歌单名称已存在！"
        else:
            playlist = Playlist()
            playlist.playlistname = playlistname
            playlist.userid_id = userid
            playlist.createtime = Util().getCurrentTime()
            playlist.save()
            success = 1
    data = {
        "success":success,
        "message":message,
        "url":"reload"
    }
    return JsonResponse(data)


# 歌单列表
def list(request):
    page = request.POST.get("page",1)
    userid = request.session.get(Constant.session_user_id)
    playlists = Playlist.objects.filter(userid_id=userid).order_by("-id")
    paginator = Paginator(playlists, Constant.pageSize)  # 分页
    playlists = paginator.page(page)
    data = {
        "pageBean": playlists,
        "page": page,
    }
    return render(request, "playlist/list.html", context=data)


# 删除歌单
def delete(request):
    playlistid = request.POST.get("playlistid")
    userid = request.session.get(Constant.session_user_id)
    Playlist.objects.filter(userid_id=userid,id=playlistid).delete()
    data = {
        "success": 1,
        "url": "reload"
    }
    return JsonResponse(data)


# 歌单详情
def detail(request):
    page = request.POST.get("page", 1)
    playlistid = request.GET.get("playlistid",request.POST.get("playlistid"))
    playlist = Playlist.objects.get(id=playlistid)
    playlistrecords = Playlistrecord.objects.filter(playlistid_id=playlistid).order_by("-id")
    paginator = Paginator(playlistrecords, Constant.pageSize)  # 分页
    playlistrecords = paginator.page(page)
    data = {
        "playlist": playlist,
        "pageBean": playlistrecords,
        "page": page,
    }
    return render(request, "playlist/detail.html", context=data)


# 公共个人歌单
def listCommon(request):
    userid = request.GET.get("userid",request.POST.get("userid"))
    user = User.objects.get(id=userid)
    page = request.POST.get("page", 1)
    playlists = Playlist.objects.filter(userid_id=userid).order_by("-id")
    paginator = Paginator(playlists, Constant.pageSize)  # 分页
    playlists = paginator.page(page)
    data = {
        "pageBean": playlists,
        "page": page,
        "user": user,
    }
    return render(request, "playlist/listCommon.html", context=data)






