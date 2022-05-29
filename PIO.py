# -*- coding: utf-8 -*-
# @Time    : 1/21/2022 3:18 PM
# @Author  : Chen0495
# @Email   : 1346565673@qq.com|chenweiin612@gmail.com
# @File    : PIO.py
# @Software: PyCharm
import numpy as np
import random
import copy
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


''' 种群初始化函数 '''


def initial(pop, dim, ub, lb):
    X = np.zeros([pop, dim])
    for i in range(pop):
        for j in range(dim):
            X[i, j] = random.random() * (ub[j] - lb[j]) + lb[j]

    return X, lb, ub


'''边界检查函数'''


def BorderCheck(X, ub, lb, pop, dim):
    for i in range(pop):
        for j in range(dim):
            if X[i, j] > ub[j]:
                X[i, j] = ub[j]
            elif X[i, j] < lb[j]:
                X[i, j] = lb[j]
    return X


'''计算适应度函数'''


def CaculateFitness(X, fun):
    pop = X.shape[0]
    fitness = np.zeros([pop, 1])
    for i in range(pop):
        fitness[i] = fun(X[i, :])
    return fitness


'''适应度排序'''


def SortFitness(Fit):
    fitness = np.sort(Fit, axis=0)
    index = np.argsort(Fit, axis=0)
    return fitness, index


'''根据适应度对位置进行排序'''


def SortPosition(X, index):
    Xnew = np.zeros(X.shape)
    for i in range(X.shape[0]):
        Xnew[i, :] = X[index[i], :]
    return Xnew



'''鸽群算法'''


def PIO(pop, dim, lb, ub, MaxIter, fun):
    
    Nc1= round(MaxIter*0.7) #地图因子
    Nc2= MaxIter - Nc1 #指南因子
    
    X, lb, ub = initial(pop, dim, ub, lb)  # 初始化种群
    Vec = np.random.random([pop,dim]) #初始速度
   
    fitness = CaculateFitness(X, fun)  # 计算适应度值
    fitness, sortIndex = SortFitness(fitness)  # 对适应度值排序
    X = SortPosition(X, sortIndex)  # 种群排序
    GbestScore = copy.copy(fitness[0])
    GbestPositon = np.zeros([1,dim])
    GbestPositon[0,:] =  copy.copy(X[0, :])
    Curve = np.zeros([MaxIter, 1])
    
    X_new = X
    VecNew = Vec
    #地图更新
    for t in range(Nc1):     
        Vec = VecNew
        for i in range(pop):
            R = random.random()
            #速度更新
            TempV = Vec[i,:] + random.random()*(GbestPositon[0,:] - X[i,:])
            #位置更新
            TempPosition = X[i,:]*(1-np.exp(-R*t)) + TempV
            #边界检查
            for j in range(dim):
                if TempPosition[j]<lb[j] or TempPosition[j]>ub[j]:
                    TempPosition[j] = lb[j] + random.random()*(ub[j] - lb[j])
                    TempV[j] = random.random()
            X_new[i,:] =  copy.copy(TempPosition)
            VecNew[i,:] =  copy.copy(TempV)
        
        X =  copy.copy(X_new)
        X = BorderCheck(X, ub, lb, pop, dim)
        fitness = CaculateFitness(X, fun)  # 计算适应度值
        fitness, sortIndex = SortFitness(fitness)  # 对适应度值排序
        X = SortPosition(X, sortIndex)  # 种群排序
        if fitness[0] <= GbestScore:  # 更新全局最优
            GbestScore =  copy.copy(fitness[0])
            GbestPositon[0,:] =  copy.copy(X[0, :])
        Curve[t] = GbestScore
    
    for t in range(Nc2):
        # 根据地标舍去后50%，并计算中心
        S = 0
        half = int(np.round(pop/2))
        for i in range(half):
            S = S + X[i,:]*fitness[i]
        
        Xcenter = S/(half*np.sum(fitness[1:half]))
        for i in range(half):
            for j in range(dim):
                Temp = X[i,j] + random.random()*(Xcenter[j] - X[i,j])
                while Temp<lb[j] or Temp>ub[j]:
                    Temp = X[i,j] + random.random()*(Xcenter[j] - X[i,j])
            X[i,:] =  copy.copy(Temp)
        
        X = BorderCheck(X, ub, lb, pop, dim)
        fitness = CaculateFitness(X, fun)  # 计算适应度值
        fitness, sortIndex = SortFitness(fitness)  # 对适应度值排序
        X = SortPosition(X, sortIndex)  # 种群排序
        if fitness[0] <= GbestScore:  # 更新全局最优
            GbestScore = fitness[0]
            GbestPositon[0,:] = X[0, :]
        Curve[t + Nc1] = GbestScore
        

    return GbestScore, GbestPositon, Curve
