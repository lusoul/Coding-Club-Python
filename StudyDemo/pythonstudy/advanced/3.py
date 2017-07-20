#coding=utf-8

'''
自省与函数
func.__code__

作用域问题

可变参数的魔法与禁忌
'''

def func1(arg1, arg2):
    return arg1 + arg2

print(dir(func1.__code__)) #查看到func1的所有属性
print(func1.__code__.co_varnames) # ('arg1', 'arg2')
print(func1.__code__.co_filename) # /Users/lusoul/Git-Hub/Coding-Club-Python/StudyDemo/pythonstudy/advanced/3.py

import urllib
print(urllib.urlopen.__code__.co_filename)
###########################################################################################
arg = 1
def func1():
    arg = 3
func1()
print(arg) #output: 1

arg = 1
def func1():
    global arg
    arg = 3
func1()
print(arg) #output: 3

##############################################################################
## list是可变参数
myList = [1,2,3]
def func3(arg):
    arg[0] = 5
    return arg
print(func3(myList)) # output:[5,2,3]
