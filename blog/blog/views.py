#coding=utf-8
from django.http import HttpResponse

def home(request, id): #因为我在urls.py里面写了blog.views.home，所以我这里需要定义home()方法
	# print(dir(request)) #dir()方法是显示object的属性和方法
	# print(request.environ) #可以显示基本的环境参数比如python版本浏览器信息等
	# return HttpResponse('Hey, my world!')
	return HttpResponse('id is %s' % id)

def test(request):
	return HttpResponse('<H1>this is test views page</H1>')

def helloWorld(request):
	return HttpResponse('<h1>No No系洗肥猪</h1>')
