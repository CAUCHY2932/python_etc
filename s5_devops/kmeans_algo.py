# coding:utf-8

def kmeans(dataSet, k, distmeas=distEclud, createCent=randCent):
    """
    该算法创建k个质心，然后将每个点分配到最近的质心，再重新计算质心
    这个过程重复数次，直到数据点的簇不再改变位置
    运行结果，多次运行结果可能不一样，因为随机质心的影响，
    但总的结果是对的，因为数据足够相似，但可能会陷入局部最小值
    :param:
    :return:
    """
    m = shape(dataSet)[0]
    
    pass