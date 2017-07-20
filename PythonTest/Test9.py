#coding=utf-8

import jieba

# seg_list = jieba.cut("我在学习自然语言", cut_all = True)
# print seg_list
# print type(seg_list)
# for s in seg_list:
#     print s
print "/".join(jieba.cut("陆灵毕业于海南大学,并在IIT读完计算机硕士学位,现今通过自己的努力成功入职FLAG公司之一-amazon", HMM=False))
# jieba.add_word("毕")
# jieba.add_word("业")
jieba.suggest_freq(('毕','业'), True)
print "/".join(jieba.cut("陆灵毕业于海南大学,并在IIT读完计算机硕士学位,现今通过自己的努力成功入职FLAG公司之一-amazon", HMM=False))


lines = open("myDict", "r").read()
print "/".join(lines)