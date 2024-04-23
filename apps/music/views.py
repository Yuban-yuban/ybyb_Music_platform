from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import render

from apps.collection.models import Collection
from apps.comment.models import Comment
from apps.common.models import Constant
from apps.music.models import Music
from apps.playlist.models import Playlist
from apps.scorerecord.models import Scorerecord
from apps.type.models import Type


# 音乐详情
def detail(request):
    # 通过get请求获取音乐id，是其他页面跳转到音乐详情页面
    # 通过post请求获取音乐id，是在音乐详情页面中的收藏、评分、评论、分页请求中获取
    musicid = request.GET.get("musicid", request.POST.get("musicid"))
    # 查找当前音乐
    music = Music.objects.get(id=musicid)
    # 当前音乐的评论数量
    commentCount = Comment.objects.filter(musicid=musicid).aggregate(count=Count("id"))
    data = {  # 返回参数
        "music": music,
        "commentCount": commentCount,
    }
    if commentCount["count"] > 0:  # 如果当前音乐有评论
        page = request.POST.get("page", 1)  # 获取请求的页码
        comments = Comment.objects.filter(musicid=musicid).order_by("-id")  # 查询评论，id降序
        paginator = Paginator(comments, Constant.pageSize)
        comments = paginator.page(page)
        data["pageBean"] = comments
        data["page"] = page
    # 判断游客是否登录
    if Constant.session_user_isLogin in request.session \
            and request.session[Constant.session_user_isLogin]:
        userid = request.session[Constant.session_user_id]
        # 获取登录用户是否对当前音乐收藏
        collection = Collection.objects.filter(userid=userid, musicid=musicid)
        if len(collection) > 0:
            data["collection"] = collection[0]
        # 歌单
        playlists = Playlist.objects.filter(userid_id=userid)
        data["playlists"] = playlists
        # 评分
        scorerecord = Scorerecord.objects.filter(userid=userid, musicid=musicid)
        if len(scorerecord) > 0:
            data["scorerecord"] = scorerecord[0]
    return render(request,"music/detail.html",context=data)


# 音乐列表
def list(request):
    page = request.POST.get("page",1)
    musicname = request.POST.get("musicname","")  # 搜索关键字
    typeid = request.POST.get("typeid","")  # 音乐类型主键
    types = Type.objects.all()
    musics = None
    if musicname == "":
        if typeid == "":
            musics = Music.objects.all().order_by("-id")
        else:
            typeid = int(typeid)
            musics = Music.objects.filter(typeid_id=typeid).order_by("-id")
    else:
        if typeid == "":
            musics = Music.objects.filter(musicname__icontains=musicname).order_by("-id")
        else:
            typeid = int(typeid)
            musics = Music.objects.filter(musicname__icontains=musicname,typeid_id=typeid).order_by("-id")
    paginator = Paginator(musics, Constant.pageSize)  # 分页
    musics = paginator.page(page)
    data = {
        "pageBean": musics,
        "types":types,
        "musicname":musicname,
        "typeid":typeid,
        "page":page,
    }
    return render(request, "music/list.html", context=data)


