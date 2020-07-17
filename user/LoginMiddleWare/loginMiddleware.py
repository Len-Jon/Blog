#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
:Time:  2020/7/8 23:17
:Author:  lenjon
"""

from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin


class LoginCheck(MiddlewareMixin):
    def process_request(self, request):
        path = request.path_info.lstrip('/')
        if path.find('user') != -1:  # 如果url有user
            urls = {'user/login/', 'user/doLogin/'}  # 可放行url
            if path not in urls:
                ID = request.session.get('id')
                if not ID:  # 如果session中没有id，则返回登录页面
                    return HttpResponseRedirect('/user/login')
