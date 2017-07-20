#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

# 我们直接自己实现KNN
import csv  # 读取数据用的
import random
import math
import operator

# 我们要把一部分数据分为训练集，一部分测试集，所以需要split参数
def loadDataset(filename, split, trainingSet=[], testSet=[]):
    with open(filename, 'rb') as csvfile:
        lines = csv.reader(csvfile)
        next(lines)  # 去掉第一行非数据行
        dataset = list(lines)
        for x in range(len(dataset) - 1):
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
            if random.random() < split:  # 我们任意生成一个数，如果小于split就归类到训练集中
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])


# 这里的参数每个点的纬度就可以是3，4个纬度，不一定就是2个纬度x，y了
def euclideanDistance(instance1, instance2, length):  # length表示纬度
    distance = 0
    for x in range(length):
        distance += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)


# 返回最近的k个邻居。从trainingSet中选出K个离testInstance最近的点s
def getNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance) - 1
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x], dist))

    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors


# 得到了最近的k个邻居以后根据少数服从多数的投票法则来决定给要预测的实例归为哪一类
def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    # 以距离排序
    sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)  # reverse表示按降序方式排列
    return sortedVotes[0][0]


# 以上就完成了所有KNN算法模块


# 预测所有值和实际值比较的准确率accuracy是多少
def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:  # 如果预测正确，就让correct+1
            correct += 1

    return (correct / float(len(testSet))) * 100.0  # 我们预测的正确个数／总的个数看我们正确率是多少


def main():
    # prepare data
    trainingSet = []
    testSet = []
    split = 0.67  # 也就是1/3的概率是测试集，2/3的概率是训练集
    # 下面的路径 r 有特殊用法，r表示raw，就是你传入的路径可能有\n之类的字符，r这里就表示把你传入的字符串当作原始字符串对待，不考虑\n等转义字符
    loadDataset(r'/Users/lusoul/Git-Hub/Coding-Club-Python/StudyDemo/algorithm/knn/iris.data.txt', split, trainingSet,
                testSet)
    print("Train set: " + repr(len(trainingSet)))
    print("Test set: " + repr(len(testSet)))

    # generate predictions
    predictions = []
    k = 3  # 取最近的3个邻居
    for x in range(len(testSet)):
        neighbors = getNeighbors(trainingSet, testSet[x], k)
        result = getResponse(neighbors)
        predictions.append(result)
        print("> predicted = " + repr(result) + ", actual = " + repr(testSet[x][-1]))
    accuracy = getAccuracy(testSet, predictions)
    print("Accuracy: " + repr(accuracy) + "%")


main()
