#coding=utf-8

import os, time, random, jieba, sklearn
from sklearn.naive_bayes import MultinomialNB
import numpy as np
import pylab as pl # 用pip安装 matplotlib以后，这个库也就有了
import matplotlib.pyplot as plt #绘图工具

# 粗暴的词统计
def make_word_set(words_file):
    words_set = set()
    with open(words_file, 'r') as f:
        for line in f.readlines(): # readlines()返回的是list类型,所以可以直接for循环
            word = line.strip().decode("utf-8")
            if len(word) > 0 and word not in words_set:
                words_set.add(word)

    return words_set

# 文本处理，也就是样本生成过程
def text_processing(folder_path, test_size = 0.2): #test_size也就是训练集占80%，测试集占20%
    folder_list = os.listdir(folder_path) #该路径下的所有文件和文件夹
    data_list = [] # 所有单词
    class_list = [] # 类别，因为一个文本file属于一个folder，我们把folder名字直接作为类别就好

    #遍历文件夹
    for folder in folder_list:
        new_folder_path = os.path.join(folder_path, folder) # join就是将两个拼接起来，比如folder_path为".", folder为"hello", join后就是"./hello"
        files = os.listdir(new_folder_path)
        #读取文件
        j = 1
        for file in files:
            if j > 100: #怕内存爆炸，只取100个样本文件，你可以注释掉取完
                break
            with open(os.path.join(new_folder_path, file), 'r') as f:
                raw = f.read()

            #拿到的内容用jieba进行分词
            jieba.enable_parallel(4) #开启并行分词模式，参数为线程个数，不支持windows
            word_cut = jieba.cut(raw, cut_all = False) #cut_all为True就是全模式，为False就是精确模式，默认是精确模式。全模式就是"清华大学 华大"，精确模式就只有一个"清华大学"
            #以上cut返回可迭代的generator
            word_list = list(word_cut) #generator转成list，每个次unicode格式
            jieba.disable_parallel() # 关闭并行分词模式

            data_list.append(word_list)
            class_list.append(folder.decode('utf-8'))#类别
            j += 1

        # 粗暴的划分训练集和测试集
        data_class_list = zip(data_list, class_list)
        random.shuffle(data_class_list)
        index = int(len(data_class_list) * test_size) + 1
        train_list = data_class_list[index:]
        test_list = data_class_list[:index]
        train_data_list, train_class_list = zip(*train_list)
        test_data_list, test_class_list = zip(*test_list)





