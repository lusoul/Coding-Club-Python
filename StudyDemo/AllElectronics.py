# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from sklearn.feature_extraction import DictVectorizer #sklearn对数据输入格式有一定要求,它只支持Integer，我们要转换会利用到DictVectorizer
import csv #我们会把原始数据存在csv文件里面, 这个包python自带我们不需要安装
from sklearn import preprocessing
from sklearn import tree #因为用到decision tree所以需要import它
from sklearn.externals.six import StringIO

#接下来看如何用python和机器学习的库来运用Decision Tree算法
allElectronicsFile = open("/Users/lusoul/Git-Hub/Coding-Club-Python/StudyDemo/AllElectronics.csv", "r")
reader = csv.reader(allElectronicsFile)
#headers = reader.next() #这个是python2里面用到，python3不支持
headers = next(reader)#这是python3支持的写法
#print(list(reader))
#print(headers)

# 主要分3步走：

# （1）sklearn对Decision Tree的实现已经实现好了，但它对输入数据格式上有基本要求，不能直接用excel里面的raw data，所以我们需要进行预处理
# sklearn要求我们所有的特征值（属性age，income，student，credit_rating的值）以及类标记（class_buys_computer），他们的值必须都要是数值型的值，而不能是raw data中类别的值String，所以需要进行转换
# 比如age属性下有 老，中，轻 三种类型的值，我们要搭建一个矩阵，用0，1来代表这3个值
# 例如AllElectronics.csv第一行数据的age是youth，它不是中年或老年，那么
# youth:1, middle_aged: 0, senior: 0
# 然后income有high,medium,low，我们转成0，1
# high: 1, medium: 0, low: 0
# 依次类推得到
# youth, middle_aged, senior, high, medium, low, yes, no, fair, excellent, buy(这个是类标记，no为0，yes为1)
#   1         0         0      1      0      0    0   1    1       0        0
# 以上格式才满足sklearn文档的数据格式
featureList = [] #装取不算分类，特征值的information
labelList = [] #装取分类值

for row in reader: #reader此时Object含有所有元素，因为开始next了一次所以从第一行开始
    labelList.append(row[len(row) - 1])
    rowDict = {}
    for i in range(1, len(row) - 1):
        rowDict[headers[i]] = row[i] #相当于map.put(key, value)
    featureList.append(rowDict)
    
#print(featureList)
#print(labelList)
#我们为什么要建立list类型？因为python给我提供了一个模块叫DictVectorizer，如果一个list里面有dictionary类型的话，我们可以调用以下方法直接转成0，1的dummy variable,所以以上步骤要生成包含dict的list
vec = DictVectorizer()
dummyX = vec.fit_transform(featureList).toarray()
print("dummyX:" + str(dummyX))
print(vec.get_feature_names)
print("labellist: " + str(labelList))
# vectorize class label
label = preprocessing.LabelBinarizer()
dummyY = label.fit_transform(labelList)
print("dummyY: " + str(dummyY))

# （2）处理完之后我们直接用sklearn里面自带的tree的分类器DecisionTreeClassifier进行模型的创建
# 此时dummyX和dummyY都符合了sklearn里面的格式
# using decision tree for classification
clf = tree.DecisionTreeClassifier(criterion = "entropy")#clf是分类起。决策树选取属性作为节点的度量方法是信息熵，ID3算法，如果你不指明这里它默认使用CART算法
clf = clf.fit(dummyX, dummyY) #建模，构建出决策树 
print("clf: " + str(clf))

# （3）之后我们就可以可视化的看建好的decision tree，并且来进行预测
# visualize model
with open("allElectronicsInformationGainOri.dot", "w") as f:
    f = tree.export_graphviz(clf, feature_names = vec.get_feature_names(), out_file = f)

oneRowX = dummyX[0, :]
print("oneRowX: " + str(oneRowX))

newRowX = oneRowX

newRowX[0] = 1
newRowX[2] = 0
print("newRowX: " + str(newRowX))

predictedY = clf.predict(newRowX)
print("predictedY: " + str(predictedY))

