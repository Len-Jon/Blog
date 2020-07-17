#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
:Time:  2020/7/17 17:14
:Author:  lenjon
"""
from django.http import HttpResponseRedirect


def redirect(request):
    return HttpResponseRedirect('/user/index')