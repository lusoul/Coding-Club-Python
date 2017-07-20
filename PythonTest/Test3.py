#coding=utf-8
import re

pattern = re.compile(r'H.*g')
match = pattern.search("hello, Hanxiaoyang!")

if match:
    print match.group() #如果使用pattern.match()的话没有值返回这里，只能使用search，search是匹配子串
# 输出 Hanxiaoyang
# 如果是match()就没输出，因为match()是从头开始匹配





