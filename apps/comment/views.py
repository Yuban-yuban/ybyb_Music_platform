# 前台评论视图模块
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render
from apps.comment.models import Comment
from apps.common.models import Constant
from apps.util.util import Util


# 添加评论
def doComment(request):
    post = request.POST  # 获取请求方式
    content = post.get("content")  # 获取请求内容
    musicid = post.get("musicid")  # 获取音乐主键
    userid = request.session[Constant.session_user_id]  # 从session中获取当前登录用户的id
    comment = Comment()
    comment.userid_id = userid
    comment.musicid_id = musicid
    comment.content = content
    comment.createtime = Util().getCurrentTime()
    parentid = post.get("parentid")
    if parentid:
        comment.parentid_id = parentid  # 判断是否是回复评论
    comment.save()  # 添加评论记录
    data = {  # 返回参数
        "success":1,  # 1：操作成功
        "url":"reload"  # 重新加载请求的页面
    }
    return JsonResponse(data)


# 评论列表
def list(request):
    page = request.POST.get("page", 1)  # 获取请求的页码，如果不存在就请求第一页
    userid = request.session[Constant.session_user_id]
    records = Comment.objects.filter(userid_id=userid).order_by("-id")  # 查找当前用户的评论记录，id降序
    paginator = Paginator(records, Constant.pageSize)
    records = paginator.page(page)
    data = {  # 返回参数
        "pageBean": records,
        "page": page,
    }
    return render(request, "comment/list.html", context=data)


# 评论详情
def detail(request):
    commentid = request.GET.get("commentid")
    comment = Comment.objects.get(id=commentid)
    data = {
        "comment": comment,
    }
    return render(request, "comment/detail.html", context=data)


# 跳转到评论编辑页面
def edit(request):
    commentid = request.GET.get("commentid")
    comment = Comment.objects.get(id=commentid)
    data = {
        "comment": comment,
    }
    return render(request, "comment/edit.html", context=data)


# 更新评论
def doEdit(request):
    commentid = request.POST.get("commentid")
    content = request.POST.get("content")  # 获取请求内容
    comment = Comment.objects.get(id=commentid)
    comment.content = content
    comment.createtime = Util().getCurrentTime()
    comment.save()
    data = {  # 返回参数
        "success": 1,  # 1：操作成功
        "url": "reload"  # 重新加载请求的页面
    }
    return JsonResponse(data)


# 删除评论
def delete(request):
    commentid = request.POST.get("commentid")
    userid = request.session.get(Constant.session_user_id)
    Comment.objects.filter(userid_id=userid,id=commentid).delete()
    data = {
        "success": 1,
        "url": "reload"
    }
    return JsonResponse(data)



