# -*- coding: utf-8 -*-

myList = [1,2,3,4]
print(list(map(lambda x: x * x, myList))) #输出[1,4,9,16] lambda x: x * x的第一个x是参数，后面两个x*x是返回值

import dj