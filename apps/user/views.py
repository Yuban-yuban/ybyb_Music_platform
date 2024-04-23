from django.http import JsonResponse
from django.shortcuts import render, redirect

from WebMusicCFRSPython import settings
from apps.common.models import Constant
from apps.user.models import User


# 用户详情
def detailCommon(request):
    userid = request.GET.get("userid")
    user = User.objects.get(id=userid)
    data = {
        "user":user,
    }
    return render(request,"user/detailCommon.html",context=data)


# 跳转到用户编辑页面
def edit(request):
    user = User.objects.get(id=request.session[Constant.session_user_id])
    data = {
        "user": user,
    }
    return render(request, "user/edit.html", context=data)


# 保存用户修改的数据
def doEdit(request):
    post = request.POST
    email = post.get("email")
    header = post.get("header")
    success = User.objects.filter(id=request.session[Constant.session_user_id])\
        .update(email=email,header=header)
    url = ""
    if success > 0:
        url = "reload"
        request.session[Constant.session_user_header] = settings.MEDIA_URL+header
    data = {
        "success":success,
        "url":url,
    }
    return JsonResponse(data)


# 跳转到修改密码页面
def password(request):
    return render(request,"user/password.html")


# 修改密码
def doPassword(request):
    post = request.POST
    oldPassword = post.get("oldPassword")
    password = post.get("password")
    user = User.objects.get(id=request.session[Constant.session_user_id])
    success = 0
    url = ""
    message = ""
    if user.password == oldPassword:
        success = User.objects.filter(id=user.id).update(password=password)
        if success > 0:
            url = "/login"
            request.session.flush()
    else:
        message = "原密码不正确！"
    data = {
        "success":success,
        "url":url,
        "message":message,
    }
    return JsonResponse(data)




