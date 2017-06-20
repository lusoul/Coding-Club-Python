#coding=utf-8

"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.contrib import admin
from . import views #这件是新加的为了添加新的views.home进来

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$', views.home),#新添加的url映射，这的home对应views.py里面的home方法
	# #正则表达式^表示以什么开头,$表示以什么结尾
	# #比如^a1{1,3}$表示a开头,1结尾（1可以有1个或2个或3个，正确的url为a1,a11,a111
    #
	# url(r'^test/', views.test),
	# url(r'^nono$', views.helloWorld),
    #
	# url(r'^blog/topic_[\d]$', views.test),#[\d]表示文章编号
	url(r'^blog/topic_(?P<id>[\d]+)$', views.home),
]
