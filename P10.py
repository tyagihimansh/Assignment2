# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 17:46:25 2020

@author: Himanshu Tyagi
"""


import numpy as np
##using t as x
def f(x,y):
    return 1/(y**2+x**2)
h=0.1
#initial conditions
y0=1
x0=0
x1=0
x2=0
y1=y0
y2=y0
Y=[y0]
X=[x0]
h_max=0.9
h_min=0.09
req_tol=1e-4

    ##RK4 method

while x1<=3.5e6 or x2<=3.5e6:
        if h<h_min:
            h=h_min
        elif h>h_max:
            h=h_max
        else:
            pass
        #for step h
        for i in range(1):    
            k1=f(x0,y0)    
            k2=f(x0+h/2,y0+h*k1/2)
            k3=f(x0+h/2,y0+k2*h/2)
            k4=f(x0+h,y0+k3*h)
            y_s=y0+(k1+2*(k2+k3)+k4)*h/6
            x0=x0+h
            y0=y_s
        ##for step 2*h    
        k11=f(x1,y1)    
        k21=f(x1+h,y1+h*k11)
        k31=f(x1+h,y1+k21*h)
        k41=f(x1+2*h,y1+k31*h*2)
        y_d=y1+(k11+2*(k21+k31)+k41)*h/6
        x1=x1+h
        y1=y_d
        tol=np.abs(y_s-y_d)
        h_opt=h*((30*h*req_tol)/tol)**0.25
        if h_opt>h:
            Y.append(y_d)
        else:
            h=h_opt
            k1=f(x2,y2)    
            k2=f(x2+h/2,y2+h*k1/2)
            k3=f(x2+h/2,y2+k2*h/2)
            k4=f(x2+h,y2+k3*h)
            y_s=y0+(k1+2*(k2+k3)+k4)*h/6
            x2=x2+h
            y2=y_s
            Y.append(y_d)

print("value at 3.5e6=",Y[len(Y)-1])