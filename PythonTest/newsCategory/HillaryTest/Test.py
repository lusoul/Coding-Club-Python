#coding=utf-8
import numpy
import pandas
import re

dataFrame = pandas.read_csv("./HillaryEmails.csv")
# 源文件有很多Nan的值，直接扔掉
dataFrame = dataFrame[["Id", "ExtractedBodyText"]].dropna()


def clean_email_text(text):
    text = text.replace("\n", " ") #新行，我们是不需要的
    text = re.sub(r"-", " ", text)
    text = re.sub(r"\d+/\d+/\d+", "", text)
    text = re.sub(r"[0-2]?[0-9]:[0-6][0-9]", "", text)
    text = re.sub(r"[\w]+@[\.\w]+", "", text)
    text = re.sub(r"/[a-zA-Z]*[:\//\]*[A-Za-z0-9\-_]+\.+[A-Za-z0-9\.\/%&=\?\-_]+/i", "", text)  # 网址，没意义

    pure_text = ""
    for letter in text:
        if letter.isalpha() or letter == " ":
            pure_text += letter

    text = " ".join(word for word in pure_text.split() if len(word) > 1) #没太懂这句话，把单词用空格分隔每个字母？
    return text


docs = dataFrame["ExtractedBodyText"]
docs = docs.apply(lambda s : clean_email_text(s))
print docs.head(1).values


docList = docs.values


from gensim import corpora, models, similarities
import gensim

stoplist = ['very', 'ourselves', 'am', 'doesn', 'through', 'me', 'against', 'up', 'just', 'her', 'ours',
            'couldn', 'because', 'is', 'isn', 'it', 'only', 'in', 'such', 'too', 'mustn', 'under', 'their',
            'if', 'to', 'my', 'himself', 'after', 'why', 'while', 'can', 'each', 'itself', 'his', 'all', 'once',
            'herself', 'more', 'our', 'they', 'hasn', 'on', 'ma', 'them', 'its', 'where', 'did', 'll', 'you',
            'didn', 'nor', 'as', 'now', 'before', 'those', 'yours', 'from', 'who', 'was', 'm', 'been', 'will',
            'into', 'same', 'how', 'some', 'of', 'out', 'with', 's', 'being', 't', 'mightn', 'she', 'again', 'be',
            'by', 'shan', 'have', 'yourselves', 'needn', 'and', 'are', 'o', 'these', 'further', 'most', 'yourself',
            'having', 'aren', 'here', 'he', 'were', 'but', 'this', 'myself', 'own', 'we', 'so', 'i', 'does', 'both',
            'when', 'between', 'd', 'had', 'the', 'y', 'has', 'down', 'off', 'than', 'haven', 'whom', 'wouldn',
            'should', 've', 'over', 'themselves', 'few', 'then', 'hadn', 'what', 'until', 'won', 'no', 'about',
            'any', 'that', 'for', 'shouldn', 'don', 'do', 'there', 'doing', 'an', 'or', 'ain', 'hers', 'wasn',
            'weren', 'above', 'a', 'at', 'your', 'theirs', 'below', 'other', 'not', 're', 'him', 'during', 'which']

texts = [[word for word in doc.lower().split() if word not in stoplist] for doc in docList]
print texts[0]

dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]

# # LDA就是你把训练集进行分类，你自己不知道这个类别是什么，你参数指定了num_topics=20就会把数据分成20类
lda = gensim.models.ldamodel.LdaModel(corpus = corpus, id2word = dictionary, num_topics = 20)
# print lda.print_topic(10, topn = 5) #查看编号为10的类别的top 5的单词是什么
# print lda.print_topic(0, topn = 5) #查看编号为10的类别的top 5的单词是什么
# print lda.print_topic(19, topn = 5) #查看编号为10的类别的top 5的单词是什么


'''
predict data from here
'''
print "begin to test set"
texts = []
with open("./homework.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        text = []
        if line == '\n':
            continue
        else :
             text.append(clean_email_text(line))
             texts.append(text)

ret = []
for text in texts:
    ret.append(text[0].lower().split(" "))
print ret

myDict = corpora.Dictionary(ret)
myBow = [myDict.doc2bow(val) for val in ret]

print lda.get_document_topics(myBow)