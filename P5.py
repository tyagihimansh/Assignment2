# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 10:54:23 2020

@author: Himanshu Tyagi
"""

##Shooting Method for solving ODE 
##x''[t]=-10 and x'[t]=u
import numpy as np

def f(t,x,u):
    return -10
h=0.01
##initial conditions

for u0 in np.linspace(46.05,55.05,10):
    
    x0=0
    t0=0
    X=[x0]
    for i in range(1001):
        m1=u0
        k1=f(t0,x0,u0)
        m2=u0+k1*h/2
        k2=f(t0+h/2,x0+h*m1/2,m2)
        m3=u0+k2*h/2
        k3=f(t0+h/2,x0+m2*h/2,m3)
        m4=u0+k3*h
        k4=f(t0+h,x0+m3*h,m4)
        x=x0+(m1+2*(m2+m3)+m4)*h/6
        u=u0+(k1+2*(k2+k3)+k4)*h/6
        u0=u
        x0=x
        t0=t0+h
        X.append(x)
    
    t=np.linspace(0,t0,len(X))
    x=np.array(X)
    import matplotlib.pyplot as plot
    if X[1001]==-4.485412041788095e-12:
         plot.plot(t,x,'tab:red')  ##Red curve will be the exact solution Numerically
         plot.xlabel('t')
         plot.ylabel('x(t)')
    else:
        
         plot.plot(t,x,'tab:gray')
         plot.xlabel('t')
         plot.ylabel('x(t)')
##In this case we can't find the solution using argmin as it returns only first occurrence.
    print(X[1001])
plot.grid()
plot.show()    