from django.http import JsonResponse
from django.shortcuts import render
from apps.common.models import Constant
from apps.labelrecord.models import Labelrecord
from apps.type.models import Type
from apps.user.models import User
from apps.util.util import Util


# 公共标签列表
def listCommon(request):
    get = request.GET
    userid = get.get("userid")
    types = Type.objects.all()
    data = {
        "userid":userid,
        "types":types
    }
    return render(request, "labelrecord/listCommon.html", context=data)


# 公共保存选择的标签
def saveCommon(request):
    post = request.POST
    userid = post.get("userid")
    typeids = post.get("typeids")
    typeidList = typeids.split(",")
    for typeid in typeidList:
        labelrecord = Labelrecord()
        labelrecord.userid_id = userid
        labelrecord.typeid_id = typeid
        labelrecord.createtime = Util().getCurrentTime()
        labelrecord.save()
        sessionUser = User.objects.get(id=userid)
        # 将登录信息保存到session中
        request.session[Constant.session_user_isLogin] = True
        request.session[Constant.session_user_id] = sessionUser.id
        request.session[Constant.session_user_username] = sessionUser.username
        request.session[Constant.session_user_header] = sessionUser.header.url
    data = {
        "success":1
    }
    return JsonResponse(data)


# 跳转到兴趣便签编辑页面
def edit(request):
    types = Type.objects.all()
    userid = request.session.get(Constant.session_user_id)
    labelrecords = Labelrecord.objects.filter(userid_id=userid)
    data = {
        "labelrecords": labelrecords,
        "types": types
    }
    return render(request, "labelrecord/edit.html", context=data)


# 修改标签
def save(request):
    post = request.POST
    userid = request.session.get(Constant.session_user_id)
    typeids = post.get("typeids")
    typeidList = typeids.split(",")
    Labelrecord.objects.filter(userid_id=userid).delete()
    for typeid in typeidList:
        labelrecord = Labelrecord()
        labelrecord.userid_id = userid
        labelrecord.typeid_id = typeid
        labelrecord.createtime = Util().getCurrentTime()
        labelrecord.save()
    data = {
        "success": 1,
        "url":"reload"
    }
    return JsonResponse(data)






