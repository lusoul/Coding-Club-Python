#coding=utf-8
'''
习题：
1 定义一个方法get_num(num),num参数是列表类型，判断列表里面的元素为数字类型。其他类型则报错，并且返回一个偶数列表：（注：列表里面的元素为偶数）。

2 定义一个方法get_page(url),url参数是需要获取网页内容的网址，返回网页的内容。提示（可以了解python的urllib模块）。

3 定义一个方法 func，该func引入任意多的列表参数，返回所有列表中最大的那个元素。

4 定义一个方法get_dir(f),f参数为任意一个磁盘路径，该函数返回路径下的所有文件夹组成的列表，如果没有文件夹则返回"Not dir"。
'''

#1 定义一个方法get_num(num),num参数是列表类型，判断列表里面的元素为数字类型。其他类型则报错，并且返回一个偶数列表：（注：列表里面的元素为偶数）。
def getEven(aList=[]):
    for num in aList:
        if type(num) != int: return "Type Error"
    return [num for num in aList if num % 2 == 0]
print(getEven([1,4,5,7,88,8,88,89,True]))
print(getEven([1,4,5,7,88,8,88,89]))

#2 定义一个方法get_page(url),url参数是需要获取网页内容的网址，返回网页的内容。提示（可以了解python的urllib模块）。
import urllib
def get_page(url):
    try:
        url_page = urllib.urlopen(url)
        if url_page.getcode() == 200:
            return {url_page.geturl(): url_page.read()}
    except:
        return "地址不合法"

print(get_page("http://www.google.com"))

#3 定义一个方法 func，该func引入任意多的列表参数，返回所有列表中最大的那个元素。
def getMaxInLists(*lists):
    listAll = []
    for l in lists:
        listAll.extend(l) #如果你用listAll.append(l)的话会得到[[..], [..], [...]]无法获得正确结果
    return max(listAll)
print(getMaxInLists([5,3,1], [3,5,8], [9,4,2,1,"st"]))

#4 定义一个方法get_dir(f),f参数为任意一个磁盘路径，该函数返回路径下的所有文件夹组成的列表，如果没有文件夹则返回"Not dir"。
import glob
def get_dir(f):
    return glob.glob(f + "*/")
print(get_dir("/Users/lusoul/Git-Hub/Coding-Club-Python/StudyDemo/"))

import os
print(os.listdir("/Users/lusoul/Git-Hub/Coding-Club-Python/StudyDemo/"))
print(os.path.isdir("/Users/lusoul/Git-Hub/Coding-Club-Python/StudyDemo/test.py"))