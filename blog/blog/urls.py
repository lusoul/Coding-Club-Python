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
# from . import views #这件是新加的为了添加新的views.home进来
# from . import whyViews #由此可见views.py这个文件的名字是可以自定义的

from subblog import views as sviews

from django.conf import settings
from django.conf.urls.static import static

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
	# url(r'^blog/topic_(?P<id>[\d]+)$', views.home),
    # url(r'^hello/', whyViews.whyViewsFunc)
    # url(r'^hello/', whyViewsFunc)

    # url(r'^subblog/$', views.hello),
    # url(r'^subblog/(\d+)/$', views.hello), #小括号(\d+)括起来就是网址传参的方式,你可以用这种方式写更清晰(?P<offset>\d+)因为你指定了offset应该为hello方法的参数
    url(r'^hello/$', sviews.hello),

    url(r'^$', sviews.index),
    url(r'^article/(?P<id>\d+)/$', sviews.getArticleById),


] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

