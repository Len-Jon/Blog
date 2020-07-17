#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
:Time:  2020/7/17 0:00
:Author:  lenjon
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.redirectToLogin),  # 跳转首页
    url(r'^index/$', views.index),  # 管理员首页

    url(r'^uploadArticle/$', views.uploadArticle),  # 上传文章
    url(r'^doUploadArticle/$', views.doUploadArticle),  # 更新文章
    url(r'^uploadImg/$', views.uploadImg),  # Markdown图片上传
    url(r'^uploadImage/$', views.uploadImage),  # rtf图片上传

    url(r'^new_markdown/$', views.new_markdown),  # 新建markdown文章
    url(r'^markdownList/$', views.markdownList),  # markdown文章列表
    url(r'^updateMarkdown/(\d+)/$', views.updateMarkdown),  # 更新markdown文章
    url(r'^deleteMarkdown/(\d+)/$', views.deleteMarkdown),  # 删除markdown文章，这个本来想复用，但是重定向到首页不太友好，因此独立出来

    url(r'^new_rtf/$', views.new_rtf),
    url(r'^rtfList/$', views.rtfList),  # markdown文章列表
    url(r'^updateRtf/(\d+)/$', views.updateRtf),  # 更新markdown文章
    url(r'^deleteRtf/(\d+)/$', views.deleteRtf),
]