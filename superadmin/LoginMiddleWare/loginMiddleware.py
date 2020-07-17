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
        if path.find('admin') == 0:  # 如果url有user开头
            urls = {'admin/login/', 'admin/doLogin/'}  # 可放行url
            if path not in urls:
                ID = request.session.get('super_id')
                if not ID:  # 如果session中没有id，则返回登录页面
                    return HttpResponseRedirect('/admin/login')
