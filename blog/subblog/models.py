# -*- coding: utf-8 -*-
# 这个就是MVC的model了
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# 一个类对应一张表
class Author(models.Model):
    name = models.CharField(max_length = 100)
    age = models.IntegerField(default = 10)

class Article(models.Model): #也就是我们的Article类必须继承于models里的Model类，这是convention
    title = models.CharField(max_length = 200) #这是定义数据库表字段
    content = models.TextField()
    url = models.URLField()
    image = models.ImageField()
    #如何把Article和Author关联起来，
    author = models.ForeignKey(Author)




