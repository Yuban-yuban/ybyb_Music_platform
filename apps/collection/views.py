# 前台收藏视图模块
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render

from apps.collection.models import Collection
from apps.common.models import Constant
from apps.music.models import Music
from apps.user.models import User
from apps.util.util import Util


# 添加/取消收藏
def save(request):
    post = request.POST  # 获取请求方式
    musicid = post.get("musicid")  # 获取请求参数音乐主键
    userid = request.session[Constant.session_user_id]  # 从session中获取当前登录用户的id
    collection = Collection.objects.filter(musicid=musicid,userid=userid)  # 查找收藏记录
    if len(collection) > 0:
        collection.delete()  # 如果存在收藏记录，那么删除
    else:
        collection = Collection()
        collection.userid_id = userid
        collection.musicid_id = musicid
        collection.createtime = Util().getCurrentTime()
        collection.save()  # 添加收藏记录
    data = {  # 返回参数
        "success":1,  # 1：操作成功
        "url":"reload"  # 重新加载请求的页面
    }
    return JsonResponse(data)


# 收藏列表
def list(request):
    page = request.POST.get("page", 1)  # 获取请求的页码，如果不存在就请求第一页
    userid = request.session[Constant.session_user_id]
    collections = Collection.objects.filter(userid_id=userid).order_by("-id")  # 查找当前用户的收藏记录，id降序
    paginator = Paginator(collections, Constant.pageSize)
    collections = paginator.page(page)
    data = {  # 返回参数
        "pageBean": collections,
        "page": page,
    }
    return render(request, "collection/list.html", context=data)
