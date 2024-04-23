# 公共视图模块
import json
import os
from django.http import JsonResponse
from django.shortcuts import render, redirect

from WebMusicCFRSPython import settings
from apps.common.models import Constant
from apps.labelrecord.models import Labelrecord
from apps.music.models import Music
from apps.playlist.models import Playlist
from apps.playlistrecord.models import Playlistrecord
from apps.user.models import User
from apps.util.util import Util


# 跳转到登录页面
def login(request):
    return render(request, "common/login.html")


# 登录
def doLogin(request):
    post = request.POST
    username = post.get('username')
    password = post.get('password')
    users = User.objects.filter(username=username, password=password)  # 查询用户
    success = 0
    message = ""
    url = ""
    data = {}
    if len(users) != 0:
        success = 1
        sessionUser = users[0]  # 当前登录用户对象
        labelrecords = Labelrecord.objects.filter(userid_id=sessionUser.id)
        if labelrecords and len(labelrecords) > 0:
            # 将登录信息保存到session中
            request.session[Constant.session_user_isLogin] = True
            request.session[Constant.session_user_id] = sessionUser.id
            request.session[Constant.session_user_username] = sessionUser.username
            request.session[Constant.session_user_header] = sessionUser.header.url
            # 登录成功跳转到首页
            url = "/"
        else:
            data["userid"] = sessionUser.id
    else:
        message = "用户名或者密码错误！"
    data["success"] = success
    data["message"] = message
    data["url"] = url
    return JsonResponse(data)


# 跳转到注册页面
def register(request):
    return render(request, "common/register.html")


# 注册
def doRegister(request):
    post = request.POST
    username = post.get('username')
    password = post.get('password')
    email = post.get('email')
    users = User.objects.filter(username=username)  # 查询用户名是否已经存在
    success = 0
    message = ""
    url = ""
    if len(users) != 0:
        success = -1
        message = "操作失败！用户名已存在！"
    else:
        user = User()
        user.username = username
        user.password = password
        user.email = email
        user.createtime = Util().getCurrentTime()
        user.header = Constant.default_user_header
        user.save()  # 保存注册的用户
        success = 1
        url = "/login"  # 跳转到用户登录页面
    return JsonResponse({"success": success, "message": message, "url": url})


# 注销
def logout(request):
    if not request.session.get(Constant.session_user_isLogin, None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/")
    del request.session[Constant.session_user_isLogin]
    del request.session[Constant.session_user_id]
    del request.session[Constant.session_user_header]
    del request.session[Constant.session_user_username]
    return redirect('/')


# 文件上传
def upload(request):
    file = request.FILES.get("file")  # 获取上传的文件对象
    print(file.name)
    fileName = file.name
    fileType = os.path.splitext(fileName)[1]  # .jpg  获取文件名后缀
    newFileName = Util().getCurrentTimeRandom() + fileType  # 产生一个随机文件名称
    print(newFileName)
    newFilePath = os.path.join(settings.MEDIA_ROOT, newFileName)  # 文件保存路径
    with open(newFilePath, "wb") as f:  # 保存文件
        for line in file:
            f.write(line)
    data = {
        "success": 1,
        "newFileName": newFileName
    }
    return JsonResponse(data)


# 音乐播放
def play(request):
    get = request.GET
    musicid = get.get("musicid")
    playlistid = get.get("playlistid")
    playlistrecords = []
    data = {}
    if musicid:
        music = Music.objects.get(id=musicid)
        playlistrecord = Playlistrecord()
        playlistrecord.musicid = music
        playlistrecords.append(playlistrecord)
    else:
        if playlistid:
            playlist = Playlist.objects.get(id=playlistid)
            data["playlist"] = playlist
            playlistrecords = Playlistrecord.objects.filter(playlistid_id=playlistid)
    data["playlistrecords"] = playlistrecords
    return render(request, "common/play.html",context=data)




