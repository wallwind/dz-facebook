# coding=utf-8
"""Uclite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from Online import views
# from django.contrib import admin

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^favicon.ico$', views.uclite_not_found_page),
    url(r'^uclite/monitor/$', views.uclite_monitor_view),
    url(r'^uclite/?$', views.uclite_list_page_view),  # 首页
    url(r'^uclite/s_list/?$', views.uclite_simple_list_page_view),  # 精简列表页
    url(r'^uclite/content/?$', views.uclite_content_view),  # 正文页
    url(r'^uclite/content_append/?$', views.uclite_content_append_view),  # 正文页内容追加
    url(r'^uclite/content_list/?$', views.uclite_content_list_cmd_view),  # 正文页列表追加
    url(r'^uclite/list_([^/]*)/?$', views.uclite_list_cmd_view),  # 列表页操作
    url(r'^uclite/feedback_([^/]*)/?$', views.uclite_feedback_view),  # feedback页面,取值:feedback_index和feedback_detail
    url(r'^uclite/result_feedback/?$', views.uclite_feedback_result_view),  # feedback的响应内容
    url(r'^uclite/time_line/?$', views.facebook_stories),  # 首页
    url(r'^uclite/fb_login/?$', views.facebook_login),  # 登录
    url(r'^uclite/fb_like/?$', views.facebook_like),     # 点赞
    url(r'^uclite/time_line_more/?$', views.facebook_stories_more),  # 更多
    url(r'^uclite/fb_share/?$', views.facebook_share),  # 分享
    url(r'^uclite/fb_add_friend/?$', views.facebook_add_friend),  # 加好友
    url(r'^uclite/fb_fan_like/?$', views.facebook_fan_like),  # 卡片内点赞
    url(r'^uclite/fb_friend_xout/?$', views.facebook_friend_xout),  # 关闭好友卡片
    url(r'^uclite/fb_test/?$', views.facebook_test),  # 测试
    url(r'^uclite/fb_test_stories/?$', views.facebook_test_stories),  # 测试

]
