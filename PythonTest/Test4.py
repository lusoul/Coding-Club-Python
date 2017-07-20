#coding=utf-8

import re
pattern = re.compile(r'hello.*\!')
match = pattern.match("Dear hello, Luling! How are you")

if match:
    print match.group()