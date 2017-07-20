# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def hello(request, offset):
    return HttpResponse("<H1>Hello World: %s</H1>" % offset)

def hello(request):
    name = 'Lu Ling'
    age = 29 #用locals()就可以把所有参数以键值对的形式传递给模版了
    return render(request, 'test.html', locals())



from subblog.models import *
from datetime import date


def index(request):
    d = date.today()
    #d得到文章标题
    articles = Article.objects.all() #得到所有记录

    return render(request, 'index.html', locals())

def getArticleById(request, id):
    article = Article.objects.get(id = id)
    return render(request, 'single.html', locals())