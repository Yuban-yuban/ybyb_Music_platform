from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from WebMusicCFRSPython import settings

urlpatterns = [
    path('',include('apps.common.urls')),  # 公共模块功能路由，前台登录、注册、注销、文件上传等
    path('',include('apps.index.urls')),  # 前台首页
    path('index/',include('apps.index.urls')),  # 前台首页
    path('music/',include('apps.music.urls')),  # 前台商品
    path('user/',include('apps.user.urls')),  # 前台用户
    path('collection/',include('apps.collection.urls')),  # 前台收藏
    path('playlist/',include('apps.playlist.urls')),  # 前台评论
    path('playlistrecord/',include('apps.playlistrecord.urls')),  # 前台评论
    path('comment/',include('apps.comment.urls')),  # 前台评论
    path('labelrecord/',include('apps.labelrecord.urls')),  # 前台购物车
    path('playrecord/',include('apps.playrecord.urls')),  # 前台订单
    # path('orderitem/',include('apps.orderitem.urls')),  # 前台订单详情
    path('scorerecord/',include('apps.scorerecord.urls')),  # 前台评分记录

    path('admin/', admin.site.urls),
]

# 设置图片路由访问规则: 访问 media 的接口会自动访问到本项目目录下的头像文件夹下的静态资源
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "在线音乐推荐系统后台管理"  # 后台登录页面登录form框标题，后台页面头部标题
admin.site.site_title = "在线音乐推荐系统后台管理"  # 后台网页的title
admin.site.index_title = "首页"  # 后台首页显示
