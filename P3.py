# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 21:13:17 2020

@author: Himanshu Tyagi
"""

##Runge-Kuttta Method
##Given equation  y''-2y'+y=x.exp(x)-x
## say y'=u with at x=0 , y=0 and u=0
## so equations d/dx(u1)=u2 and u'=2*u-y+x*exp(x)-x and 0<=x<=1
import numpy as np

def f(x,y,u):
    return 2*u-y+x*np.exp(x)-x
h=0.01
#initial conditions
u0=0
y0=0
x0=0
Y=[y0]
X=[x0]
for i in range(100):
    m1=u0
    k1=f(x0,y0,u0)
    m2=u0+k1*h/2
    k2=f(x0+h/2,y0+h*m1/2,m2)
    m3=u0+k2*h/2
    k3=f(x0+h/2,y0+m2*h/2,m3)
    m4=u0+k3*h
    k4=f(x0+h,y0+m3*h,m4)
    y=y0+(m1+2*(m2+m3)+m4)*h/6
    u=u0+(k1+2*(k2+k3)+k4)*h/6
    u0=u
    y0=y
    x0=x0+h
    Y.append(y)
    X.append(x0)
import matplotlib.pyplot as plot    
x=np.array(X)
y=np.array(Y)
plot.plot(x,y)
plot.xlabel('x')
plot.ylabel('y(x)')
plot.show()    