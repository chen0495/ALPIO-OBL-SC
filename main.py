# -*- coding: utf-8 -*-
# @Time    : 1/21/2022 3:18 PM
# @Author  : Chen0495
# @Email   : 1346565673@qq.com|chenweiin612@gmail.com
# @File    : mail.py
# @Software: PyCharm
import numpy as np
from matplotlib import pyplot as plt
import PIO
import Function as fun

'''定义目标函数用户可选fun1 - fun6 , 也可以自己定义自己的目标函数'''
def fun1(X):
        O=np.sum(X*X)
        return O

def fun2(X):
    O=np.sum(np.abs(X))+np.prod(np.abs(X))
    return O

def fun3(X):
    O=0
    for i in range(len(X)):
        O=O+np.square(np.sum(X[0:i+1]))   
    return O

def fun4(X):
    O=np.max(np.abs(X))
    return O

def fun5(X):
    X_len = len(X)
    O = np.sum(100 * np.square(X[1:X_len] - np.square(X[0:X_len - 1]))) + np.sum(np.square(X[0:X_len - 1] - 1))
    return O

def fun6(X):
    O=np.sum(np.square(np.abs(X+0.5)))
    return O

def Rosenbrock(X): # F1
    Y = X[1:]
    X = X[:-1]
    O = np.sum(100 * (Y - X*X)**2 + (1-X)**2)
    return O



'''主函数 '''
#设置参数
pop = 30 #种群数量
MaxIter = 1000 #最大迭代次数
dim = 10 #维度
lb = -100*np.ones([dim, 1]) #下边界
ub = 100*np.ones([dim, 1])#上边界
#适应度函数选择
fobj = fun.Step
GbestScore,GbestPositon,Curve = PIO.PIO(pop,dim,lb,ub,MaxIter,fobj)
print('最优适应度值：',GbestScore)
print('最优解：',GbestPositon)

#绘制适应度曲线
plt.figure(1)
#plt.semilogy(Curve,'r-',linewidth=2)
plt.plot(Curve,'r-')

plt.xlabel('Iteration',fontsize='medium')
plt.ylabel("Fitness",fontsize='medium')
plt.grid()
plt.title('step',fontsize='large')
plt.show()