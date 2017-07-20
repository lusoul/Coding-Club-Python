#coding=utf-8

import jieba

source = "代开发票。增值税发票，正规发票。"
retObj = jieba.cut(source)
ret = set()
for item in retObj:
    ret.add(item)

for i in ret:
    print i
