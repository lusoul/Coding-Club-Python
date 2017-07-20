#coding=utf-8
import jieba

jieba.load_userdict("myDict")
jieba.load_userdict("myDict2")
ret_list = jieba.cut("微软CEO纳德拉我的梦想我做主你的梦想你做主,让亚马逊CEO杰夫贝佐斯我来让我们一起飞你觉得可以吗可是我觉得很好呀，苹果CEO库克也许非常好的呢")
print "\\".join(ret_list)








