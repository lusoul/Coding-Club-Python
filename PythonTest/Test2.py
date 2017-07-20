#coding=utf-8

import re

pattern = re.compile(r'(\w+) (\w+)(?P<sign>.*)')
match = pattern.match("hello hanxiaoyang!")

print "m.string:", match.string #要去匹配的源字符串
print "m.re:", match.re
print "m.pos:", match.pos #从哪里开始匹配，没指定就默认0开始
print "m.endpos:", match.endpos
print "m.lastindex:", match.lastindex
print "m.lastgroup:", match.lastgroup

print "m.group(1, 2):", match.group(1, 2) #我把分组1和分组2以tuple的形式返回
print "m.groups():", match.groups() #以tuple的形式返回所有的分组
print "m.groupdict():", match.groupdict()
print "m.start(2):", match.start(2) #第2个分组起始位置
print "m.end(2):", match.end(2) #第2个分组结束位置
print "m.span(2):", match.span(2) #就是把第2个分组的开始和结束位置以元组tuple的形式返回
print "m.expand(r'\2 \1\3'):", match.expand(r'\2 \1\3')
'''
m.string: hello hanxiaoyang!
m.re: <_sre.SRE_Pattern object at 0x10e0f0690>
m.pos: 0
m.endpos: 18
m.lastindex: 3
m.lastgroup: sign
m.group(1, 2): ('hello', 'hanxiaoyang')
m.groups(): ('hello', 'hanxiaoyang', '!')
m.groupdict(): {'sign': '!'}
m.start(2): 6
m.end(2): 17
m.span(2): (6, 17)
m.expand(r' '): hanxiaoyang hello!
'''