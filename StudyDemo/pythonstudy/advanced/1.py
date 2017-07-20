# -*- coding: utf-8 -*-

def func1():
    print "12345"
    # return None =>默认就是返回一个None,写不写都无所谓

print(func1())
'''
输出
12345
None
'''

test = func1()
print type(test)
print test == None
'''
12345
<type 'NoneType'>
True
'''

