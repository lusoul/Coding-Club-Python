# -*- coding: utf-8 -*-

# 可变参数
def add(*num):
    print(type(num)) # <type 'tuple'>
    sum = 0
    for n in num:
        sum += n
    return sum

print(add(1,2,3,4,5))

def add2(num1, num2):
    if isinstance(num1, int) and isinstance(num2, int):
        return num1 + num2
    return "error"
print(add2(4,"s"))
assert(add2(4, 2)) == 9 # AssertionError