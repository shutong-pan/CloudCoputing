# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 14:52:19 2021

@author: tongtong
"""

import numpy as np
import matplotlib.pyplot as plt

alpha = 5 #步长
x = 1

def myf(x):#函数
    y = np.sqrt((5+4*np.cos(x))/4)+ np.sqrt((5-4*np.cos(x))/4)
    return y

x1=[]
x1.append(1)
y1=[]


def myparf(x):#偏导
    return(
        -4*np.sin(x)/np.sqrt(5+4*np.cos(x))+4*np.sin(x)/np.sqrt(5-4*np.cos(x))
    )


for i in range(0, 100):
    x = x - alpha *myparf(x)
    print("第 %d次迭代 : x = %f, y = %f" % (i+1 ,x ,myf(x)))
    x1.append(x)
    y1.append(myf(x))

#画图
plt.plot(x1,label ="x")
plt.plot(y1,label ="y")
plt.legend(loc='upper right')
plt.show()
