#coding=utf-8

import re
pattern = re.compile(r'\d+')
sourceStr = "one11two2Three3231four4"
ret = pattern.findall(sourceStr)
print ret # ['11', '2', '3231', '4']