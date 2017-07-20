#coding=utf-8
'''
习题：
1.定义一个方法 func，该func可以引入任意多的整型参数，结果返回其中最大与最小的值。
2.定义一个方法func，该func可以引入任意多的字符串参数，结果返回（长度）最长的字符串。
3.定义一个方法get_doc(module)，module参数为该脚本中导入或定义的模块对象，该函数返回module的帮助文档。
例 print get_doc(urllib),则会输出urllib这个模块的帮助文档。
4.定义一个方法get_text(f),f参数为任意一个文件的磁盘路径，该函数返回f文件的内容。
5.定义一个方法get_dir(folder),folder参数为任意一个文件夹，该函数返回folder文件夹的文件列表。提示（可以了解python的glob模块）
'''

# 1.定义一个方法 func，该func可以引入任意多的整型参数，结果返回其中最大与最小的值。
def getMinAndMax(*nums):
    return max(nums), min(nums)

ret = getMinAndMax(2,5,2,1,1,10,8,32,29,20,1,-9,32,22,-8)
print(type(ret)) #<type 'tuple'>
print(ret[0]) #32
print(ret[1]) #-9

# 2. 定义一个方法func，该func可以引入任意多的字符串参数，结果返回（长度）最长的字符串。
def getLongestString(*strs):
    max = 0
    ret = ""
    for s in strs:
        if len(s) >= max:
            max = len(s)
            ret = s
    return ret
print(getLongestString("hello", "welcome", "world"))

# 3. 定义一个方法get_doc(module)，module参数为该脚本中导入或定义的模块对象，该函数返回module的帮助文档。
# 例 print get_doc(urllib),则会输出urllib这个模块的帮助文档。
def get_doc(modlue):
    help(modlue)
print(get_doc("urllib"))

# 4.定义一个方法get_text(f),f参数为任意一个文件的磁盘路径，该函数返回f文件的内容。
import csv
from collections import Iterable
def get_text(f):
    with open(f, "r") as myFile:
        lines = csv.reader(myFile) # lines is Iterable
        ret = list(lines)
        # for line in lines: #line是list
        #     ret += line
    return ret

print(get_text("/Users/lusoul/Git-Hub/Coding-Club-Python/StudyDemo/AllElectronics.csv"))

# 5.定义一个方法get_dir(folder),folder参数为任意一个文件夹，该函数返回folder文件夹的文件列表。提示（可以了解python的glob模块）
import glob
def get_dir(folder):
    return glob.glob(folder + "*") #glob.glob()方法里面参数是pathname，你需要指定specific内容比如/path/?.jsp或/path/*，这里题目要求显示所有，所以用*
print(get_dir("/Users/lusoul/Git-Hub/Coding-Club-Python/StudyDemo/"))
