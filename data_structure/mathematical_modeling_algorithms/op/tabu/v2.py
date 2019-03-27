# -*- coding=utf-8 -*-
"""
    2019/3/12 16:13
    author:young
"""
import datetime
import random







import random
import datetime
city = []
eg= ''
for line in open("tsp.txt"):
    place,lon,lat = line.strip().split(" ")
    city.extend([(place,(lon,lat))]) #导入城市的坐标


def printtravel(vec):
    print(city[0],city[vec[0]])
    for i in range(len(vec)-1):
        print(city[vec[i]],city[vec[i+1]])
        print(city[vec[i+1]],city[0]) #打印结果函数
        eg=[i for i in range(1,29)] #一个例子 printtravel(eg)















def costroad(road):
    cost = ((float(city[0][1][0])-float(city[road[0]][1][0]))**2+(float(city[0][1][1])-float(city[road[0]][1][1]))**2)**0.5
    for i in range(len(road)-1):
        cost = cost+((float(city[road[i+1]][1][0])-float(city[road[i]][1][0]))**2+(float(city[road[i+1]][1][1])-float(city[road[i]][1][1]))**2)**0.5
    cost=cost+((float(city[road[-1]][1][0])-float(city[0][1][0]))**2+(float(city[-1][1][1])-float(city[0][1][1]))**2)**0.5
    return(cost) #计算所求解的距离，这里为了简单，视作二位平面上的点，使用了欧式距离


costroad(eg) #计算上例中的总路程







def tabusearch(diedaitimes, cacu_time, tabu_length, origin_times, costf, printf):
    s1 = datetime.datetime.now()  # 获取运行前的时间
    print("The program now is executing...")

    def pan_move(move_step, tabu_move):  # 判断移动是否在禁忌区域中，如果是返回True和该点索引，否则返回False和0
        if move_step in tabu_move:
            index = tabu_move.index(move_step)
            return (True, index)
        else:
            return (False, 0)

    def pan_cost(cost, tabu_cost, t):  # 判断该移动是否比禁忌区域中该移动小，如果小则返回True，否则返回False
        if cost < tabu_cost[t]:
            return (True)
        else:
            return (False)

    def add_tabu(cost, move, tabu_cost, tabu_move,
                 t):  # 为禁忌区域添加移动和成本，若超过T则剔除最先进入的禁忌
        tabu_cost.append(cost)
        tabu_move.append(move)
        if len(tabu_cost) > t:
            del tabu_cost[0]
        if len(tabu_move) > t:
            del tabu_move[0]
        return (tabu_cost, tabu_move)

    def cacu(vec, t):  # 为每一个初始解计算t次
        vec_set = []
        m_set = []
        cost_set = []
        h = []
        for i in range(t):
            v, m, c, h = move(vec, h)
            vec_set.append(v)
            m_set.append(m)
            cost_set.append(c)
        return (vec_set, m_set, cost_set)

    def cacu_tiqu(v1, m1, c1):  # 从上述t次筛选最小的解向量，移动和成本
        t = c1.index(min(c1))
        v_max = v1[t]
        m_max = m1[t]
        c_max = c1[t]
        return (v_max, m_max, c_max)

    def move(vec, h):  # 输出移动后的向量，和成本
        i = 1
        while i == 1:
            m = random.sample(vec, 2)
            m.sort()
            if m not in h:
                h.append(m)
                vec_copy = vec[:]
                vec_copy[vec_copy.index(m[0])] = m[1]
                vec_copy[vec_copy.index(m[1])] = m[0]
                cost = costf(vec_copy)
                i = 0
                return (vec_copy, m, cost, h)

    finall_road = []
    finall_cost = []
    for t1 in range(origin_times):
        road = [i for i in range(1, 29)]
        random.shuffle(road)
        tabu_cost = []
        tabu_move = []
        for t in range(diedaitimes):
            i = 0
            while i == 0:
                v1, m1, c1 = cacu(road, cacu_time)
                v_m, m_m, c_m = cacu_tiqu(v1, m1, c1)
                key1 = pan_move(m_m, tabu_move)
                if key1[0]:
                    if pan_cost(c_m, tabu_cost, key1[1]):
                        road = v_m
                        finall_road.append(road)
                        finall_cost.append(c_m)
                        tabu_cost, tabu_move = add_tabu(c_m, m_m, tabu_cost, tabu_move, tabu_length)
                        i = 1
                    else:
                        v1.remove(v_m)
                        m1.remove(m_m)
                        c1.remove(c_m)
                        if len(v1) == 0:
                            i = 1
                        else:
                            tabu_cost, tabu_move = add_tabu(c_m, m_m, tabu_cost, tabu_move, tabu_length)
                            road = v_m
                            finall_road.append(road)
                            finall_cost.append(c_m)
                            i = 1
                        index = finall_cost.index(min(finall_cost))
                        s2 = datetime.datetime.now()
                        print("Successfully execute!,the program has executed for " + str(
                            (s2 - s1).seconds) + " seconds!")
                        return (finall_road[index], min(finall_cost), printf(finall_road[index]))
