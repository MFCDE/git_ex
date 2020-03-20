# -*- coding: utf-8 -*-
# @Time    : 2020/3/20 22:40
# @Author  : wk
from django.http import HttpResponse


def index_view(request):
    return HttpResponse('hello git')
