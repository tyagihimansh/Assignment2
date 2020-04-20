# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 19:04:06 2020

@author: Himanshu Tyagi
"""

import numpy as np
def f(t,y):
    return y/t-(y/t)**2

h=0.1
y0=1
w0=y0
Y=[y0]
t0=1
T=[t0]
for i in range(10):
    w=w0+h*f(t0,w0)
    t0=t0+h
    w0=w
    y0=w
    T.append(t0)
    Y.append(y0)
    
b=t0
print(Y)
print(len(Y))
print(b)
import matplotlib.pyplot as plt
t=np.array(T)
y=np.array(Y)
plt.plot(t,y,'g')
plt.xlabel('t')
plt.ylabel('y(t)')

print(T,len(T))
def g(t):
    return t/(1+np.log(t))
G=[]
for i in range(11):
    g0=g(T[i])
    G.append(g0)
print(G,len(G))
plt.show()

print('Absolute error=',np.array(T)-np.array(G))
print('Relative error=',(np.array(T)-np.array(G))/np.array(G))

    
    