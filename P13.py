# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 00:49:53 2020

@author: Himanshu Tyagi
"""
import numpy as np
import matplotlib.pyplot as plt
def f(w,y,t):
    return 2*w/t-2*y/(t*t)+t*np.log(t)
w=np.zeros(1000); y=np.zeros(1000); t=np.zeros(1000)
y_sol=np.zeros(1000)
y[0]=1; w[0]=0; t[0]=1
h=0.001
y_sol[0]=0
j=1
for i in range(1001,2000):
    w[j]=w[j-1]+h*f(w[j-1],y[j-1],i/1000)
    y[j]=y[j-1]+h*w[j-1]
    t[j]=i/1000
    y_sol[j]=7*t[j]/4+(t[j]**3)*np.log(t[j])/2-3*t[j]**3/4
    j=j+1
plt.plot(t,y,'.',label='Euler')
plt.plot(t,y_sol,label='Analytical')
plt.axis([1, 2, 0, 1.2])
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.show()