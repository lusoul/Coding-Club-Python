#coding=utf-8
import jieba
import time

jieba.enable_parallel(4)
lines = open("NBA.txt").read()
t1 = time.time()
words = "/".join(jieba.cut(lines))
t2 = time.time()
time_cost = t2 - t1
print "并行分词速度为: %s bytes/second" % (len(lines) / time_cost)

jieba.disable_parallel()
lines = open("NBA.txt").read()
t1 = time.time()
words = "/".join(jieba.cut(lines))
t2 = time.time()
time_cost = t2 - t1
print "非并行速度为: %s bytes/second" % (len(lines) / time_cost)