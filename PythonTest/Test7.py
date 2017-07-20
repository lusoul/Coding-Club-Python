#coding=utf-8

import re

pattern = re.compile(r'(\w+) (\w+)')
sourceStr = "I say, hello LuLing"

print pattern.sub(r'world', sourceStr) #输出 world, world
print pattern.sub(r'\2 \1', sourceStr) #输出 say I, LuLing hello
'''
sub(repl, source)就是根据pattern，把source替换成repl
'''