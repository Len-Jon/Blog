#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
:Time:  2020/7/17 19:44
:Author:  lenjon
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.redirectTo),
    url(r'^login/$', views.login),  # 登陆页面
    url(r'^doLogin/$', views.doLogin),  # 登陆请求
    url(r'^logout/$', views.logout),  # 登出请求
    # url(r'^register/$', views.register),  # 注册
    # # url(r'^doRegister/$', views.doRegister),  # 实现注册
    url(r'^index/$', views.index),
    url(r'^userList/$', views.userList),
    url(r'^monitor/(\d+)/$', views.monitor),
]
