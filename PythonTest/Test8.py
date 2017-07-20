#coding=utf-8

import re

# s = "they're my friends, where's your friends'sdfjwer"
# print s.title()
# pattern = re.compile(r"'[a-zA-Z]+")
# match = pattern.findall(s.title())
# print match[0].lower()

s = "你好"
s2 = "我吗"
s3 = "你好"
mySet = set()
mySet.add(s.strip().decode("utf-8"))
mySet.add(s2.strip().decode("utf-8"))
mySet.add(s3.strip().decode("utf-8"))

print mySet

