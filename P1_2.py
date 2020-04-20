# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 17:38:23 2020

@author: Himanshu Tyagi
"""

import numpy as np
def g(x,y):
    return -20*(y-x)**2+2*x
y0_1=1/3
h=0.01
x0=0
Z=[y0_1]
for i in range(100):
    w0=y0_1
    w=w0+h*g(x0,w0)
    x0=x0+h
    y0_1=w
    Z.append(y0_1)
print(Z)
import matplotlib.pyplot as plt
b=x0
x=np.linspace(0,b,len(Z))
y1=np.array(Z)
plt.plot(x,y1,'b')
plt.show()