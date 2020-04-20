# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 16:15:03 2020

@author: Himanshu Tyagi
"""

##eular method for solving ODE
import math
import numpy as np
def f(x,y):
    return -9*y

h=0.01
y0=math.e
Y=[y0]
x0=0
for i in range(100):
    w0=y0
    w=w0+h*f(x0,w0)
    x0=x0+h
    y0=w
    Y.append(y0)
    
b=x0
print(Y)
print(len(Y))
print(b)
import matplotlib.pyplot as plt
x=np.linspace(0,b,len(Y))
y=np.array(Y)
plt.plot(x,y,'g')
plt.show()


