#coding=utf-8
from gensim import corpora, models, similarities
from collections import Iterable
'''
步骤：
'''
# 1. 读取语料库（语料库其实就是一个file而已）, 进行分词
# 假设我们语料库LDA_test.txt里面有9篇文字，每一行就是一篇文章。我们是运用会把一篇文字通过regex压缩到一行
stop_list = set("for a of the and to in".split(" ")) # set(['a','and','for','of','to','in','the'])
lines = ""
with open("./LDA_test.txt", "r") as f:
    lines = f.readlines()
print lines
# 以下是转成gensim支持的输入格式
texts = [[word for word in line.strip().lower().split(" ") if word not in stop_list] for line in lines]
print "\ngensim支持的输入格式texts: "
print texts

# 2. 构建字典
dictionary = corpora.Dictionary(texts)
# print dictionary
# print isinstance(dictionary, Iterable)

# 3. 通过字典将每行一篇文字转换成index形式（tokenize）
corpus = [dictionary.doc2bow(text) for text in texts]
print "\ntokenize后将单词转换成index和frequency的格式corpus: "
print corpus

# 4. 计算每个单词在自己文章中的TF-IDF值（就是term frequency词的出现频率概率分布值）
corpus_tfidf = models.TfidfModel(corpus)[corpus]
# print corpus_tfidf
# print isinstance(corpus_tfidf, Iterable)
print "\n每个单词在自己文章中的TF-IDF值: "
for c in corpus_tfidf:
    print c

# 5. 创建LDA模型
# 设置主题个数，也就是分类个数
topic_num = 2
# 训练模型
lda = models.LdaModel(corpus=corpus_tfidf, num_topics=topic_num, id2word=dictionary, alpha='auto', eta='auto', minimum_probability=0.001)
# 你也可以直接lda = models.LdaModel(corpus)，但是我们这里使用TF-IDF来训练模型
print
# 输出 (topic_id, topic_probablity)
for a in lda.get_document_topics(corpus_tfidf): #这个方法一直没搞懂，官方解释是输出指定文章的bow在该主题下的概率分布，指定文章的bow就是下面的注释
    print a
# t = ["luling"]
# bow = dictionary.doc2bow(t)
# print "get_document_topics", lda.get_document_topics(bow)

# 打印每个主题中，每个词出现的概率：
for topic_id in range(topic_num):
    print '\nTopic', topic_id
    print(lda.show_topic(topic_id))