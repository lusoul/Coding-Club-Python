import math

def computeEuclideanDistance(x1, y1, x2, y2):
    dist = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
    return dist

d_ag = computeEuclideanDistance(3, 104, 18, 90)#x和y就是打斗次数和接吻次数
d_bg = computeEuclideanDistance(2, 100, 18, 90)
d_cg = computeEuclideanDistance(1, 81, 18, 90)
d_dg = computeEuclideanDistance(101, 10, 18, 90)
d_eg = computeEuclideanDistance(99, 5, 18, 90)
d_fg = computeEuclideanDistance(98, 2, 18, 90)
'''
拿例子中的训练集数据和最后一行测试集数据
电影名称            打斗次数    接吻次数    电影类型
california man      3           104      Romance
。。。。。。
未知                18            90      Unknown =>这一条就是预测数据
'''
print("d_ag: " + str(d_ag))
print("d_bg: " + str(d_bg))
print("d_cg: " + str(d_cg))
print("d_dg: " + str(d_dg))
print("d_eg: " + str(d_eg))
print("d_fg: " + str(d_fg))
'''
d_ag: 20.518284528683193
d_bg: 18.867962264113206
d_cg: 19.235384061671343
d_dg: 115.27792503337315
d_eg: 117.41379816699569
d_fg: 118.92854997854805
'''
#可见对应的最近的3个点是a，b，c。abc都属于Romance，所以我们把未知数G点归类为romance