#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
:Time:  2020/7/17 0:00
:Author:  lenjon
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^login/$', views.login),  # 登陆页面
    # url(r'^doLogin/$', views.doLogin),  # 登陆请求
    # url(r'^logout/$', views.logout),  # 登出请求


    url(r'^admin/$', views.redirectToLogin),  # 跳转首页
    url(r'^admin/index/$', views.index),  # 管理员首页

    url(r'^admin/uploadArticle/$', views.uploadArticle),  # 上传文章
    url(r'^admin/doUploadArticle/$', views.doUploadArticle),  # 更新文章
    url(r'^admin/uploadImg/$', views.uploadImg),  # Markdown图片上传
    url(r'^admin/uploadImage/$', views.uploadImage),  # rtf图片上传

    url(r'^admin/new_markdown/$', views.new_markdown),  # 新建markdown文章
    url(r'^admin/markdownList/$', views.markdownList),  # markdown文章列表
    url(r'^admin/updateMarkdown/(\d+)/$', views.updateMarkdown),  # 更新markdown文章
    url(r'^admin/deleteMarkdown/(\d+)/$', views.deleteMarkdown),  # 删除markdown文章，这个本来想复用，但是重定向到首页不太友好，因此独立出来

    url(r'^admin/new_rtf/$', views.new_rtf),
    url(r'^admin/rtfList/$', views.rtfList),  # markdown文章列表
    url(r'^admin/updateRtf/(\d+)/$', views.updateRtf),  # 更新markdown文章
    url(r'^admin/deleteRtf/(\d+)/$', views.deleteRtf),
]