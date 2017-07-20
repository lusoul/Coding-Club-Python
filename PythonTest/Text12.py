#coding=utf-8
import jieba.posseg as pseg

words = pseg.cut("我的名字叫陆玲，我爱我的家人，所以我要努力成为最好的自己接触AI领域")
print type(words)
for x, y in words: #因为words里面的word的类型是 Pair对象，所以可以获得key和value
    print "%s %s" % (x, y)

