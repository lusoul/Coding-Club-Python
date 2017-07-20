#coding=utf-8

import re

pattern = re.compile(r'\d+')
sourceStr = "one1two2three33four4"
ret = pattern.split(sourceStr)
print ret #输出 ['one', 'two', 'three', 'four', '']

