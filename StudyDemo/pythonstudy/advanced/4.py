#coding=utf-8

# lambda 参数: 返回值
d = lambda x : x + 1
print(d(3)) #output: 4 lambda就是一个小函数

d2 = lambda x : x + 1 if x > 0 else "error"
print(d2(2)) # 3
print(d2(-2)) # error

g = lambda x : [(x, i) for i in range(x)] #lambda也可以使用列表生成式
print(g(10)) # [(10, 0), (10, 1), (10, 2), (10, 3), (10, 4), (10, 5), (10, 6), (10, 7), (10, 8), (10, 9)]

myList = [1,2,3,4,5]
g = filter(lambda x : x > 3, myList)
print(g) # [4,5]


def func2(*kargs, **kwargs):
    return kargs
print func2(2,3,4,5,[1,2,3,4],{1:2, 5:8})

def func3(**kwargs):
    return kwargs
print func3({9:9, 5:8})