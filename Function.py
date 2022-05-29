# -*- coding: utf-8 -*-
# @Time    : 1/21/2022 3:18 PM
# @Author  : Chen0495
# @Email   : 1346565673@qq.com|chenweiin612@gmail.com
# @File    : Function.py
# @Software: PyCharm

import numpy as np
import math

'''基础函数'''
def fun1(X):
    O = np.sum(X * X)
    return O


def fun2(X):
    O = np.sum(np.abs(X)) + np.prod(np.abs(X))
    return O


def fun3(X):
    O = 0
    for i in range(len(X)):
        O = O + np.square(np.sum(X[0:i + 1]))
    return O


def fun4(X):
    O = np.max(np.abs(X))
    return O


def fun5(X):
    X_len = len(X)
    O = np.sum(100 * np.square(X[1:X_len] - np.square(X[0:X_len - 1]))) + np.sum(np.square(X[0:X_len - 1] - 1))
    return O


def fun6(X):
    O = np.sum(np.square(np.abs(X + 0.5)))
    return O


def Sphere(X): # F1
    O = np.sum(X * X)
    return O

def Rosenbrock(X): # F2
    Y = X[1:]
    X = X[:-1]
    O = np.sum(100 * (Y - X*X)**2 + (1-X)**2)
    return O

def Step(X): # F3
    O = np.sum((X+0.5) * (X+0.5))
    return O

def Levy(X): # F4
    O = np.sin(X[0]*math.pi)+np.sum(((X[:-1]-1)**2) * (1+10*(np.sin(math.pi*X[:-1]+1)**2)))+((X[-1]-1)**2)*(1+(np.sin(math.pi*X[-1]+1)**2))
    return O

def Alpine(X): # F5
    O = np.sum(np.abs(X*np.sin(X)+0.1*X))
    return O

def Griewank(X): # F6
    O = np.sum(X*X)/4000 - np.prod(np.cos(X / (np.sqrt(np.arange(1, len(X)+1))))) + 1
    return O

def Schwefel(X): # F7
    O = np.sum(X**2)/4000 - np.prod(np.abs(X))
    return O

def Cross_In_Tray(X): # F8
    fact1 = np.sin(X[0]) * np.sin(X[1])
    fact2 = np.exp(np.abs(100 - np.sqrt(X[0] ** 2 + X[1] ** 2) / np.pi))
    res = -0.0001 * (np.abs(fact1 * fact2) + 1) ** 0.1
    return res

def Shubert(x):
    h1 = 0
    h2 = 0
    for i in range(1, 6):
        h1 += i * np.cos((i + 1) * x[0] + i)
        h2 += i * np.cos((i + 1) * x[1] + i)
    return h1 * h2

def Drop_Wave(X):
    O1 = 1+math.cos(12*math.sqrt(X[0]**2+X[1]**2))
    O2 = 0.5*math.sqrt(X[0]**2+X[1]**2)+2
    return -(O1/O2)

def sigmoid(x,k,b=500): # sigmoid
    y = 1+np.power(math.e,-b*(x-k))
    return x/y

def maxf(x1,x2,b=500): # 推理过程辅助函数
    y = 1+np.power(math.e,-b*(x1-x2))
    o1 = x1/y
    y = 1+np.power(math.e,-b*(x2-x1))
    o2 = x2/y
    return x1+x2

def FPN(x,mp): # 推理过程函数,x为参数w、\mu、k,mp为输入库所
    # x[0:5]-w
    # x[5:10]-\mu
    # x[10:15]-k
    # mp[0:4]-p1、p2、p4、p5
    x1 = x[5]*sigmoid(mp[0],x[10])
    x2 = x[6]*sigmoid(mp[1],x[11])
    mp3 = maxf(x1,x2)
    x3 = mp3*x[6]+mp[2]*x[5]
    mp6 = x[7]*sigmoid(x3,x[12])
    mp7 = x[8]*sigmoid(mp3,x[13])
    x4 = mp[3]*x[2]+mp6*x[3]+mp7*x[4]
    mp8 = x[9]*sigmoid(x4,x[14])
    return mp8
    
def FNs(x,c,rl):# 适应度函数，c为样本mp数组，rl为结果数组
    sum = 0.
    for i in range(100):
        sum = sum + ((FPN(x,c[i])-rl[i])**2)
    return sum
    