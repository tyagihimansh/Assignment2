# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 21:09:10 2020

@author: Himanshu Tyagi
"""
import numpy as np
def f1(t,u1,u2,u3):
    return u1+2*u2-2*u3+np.exp(-t)
def f2(t,u1,u2,u3):    
    return u2+u3-2*np.exp(-t)
def f3(t,u1,u2,u3):
    return u1+2*u2+np.exp(-t)
u10=3; u20=-1; u30=1
U1=[u10]; U2=[u20]; U3=[u30]
t0=0
T=[t0]

h=0.1
for i in  range(1000):
    if t0<=1:
        k110= f1(t0,u10,u20,u30)
        k120= f2(t0,u10,u20,u30)
        k130= f3(t0,u10,u20,u30)
        k210=f1(t0+h/2,u10+h*k110/2,u20+h*k120/2,u30+h*k130/2)
        k220=f2(t0+h/2,u10+h*k110/2,u20+h*k120/2,u30+h*k130/2)
        k230=f3(t0+h/2,u10+h*k110/2,u20+h*k120/2,u30+h*k130/2)
        k310=f1(t0+h/2,u10+h*k210/2,u20+h*k220/2,u30+h*k230/2)
        k320=f2(t0+h/2,u10+h*k210/2,u20+h*k220/2,u30+h*k230/2)
        k330=f3(t0+h/2,u10+h*k210/2,u20+h*k220/2,u30+h*k230/2)
        k410=f1(t0+h,u10+h*k310,u20+h*k320,u30+h*k330)
        k420=f2(t0+h,u10+h*k310,u20+h*k320,u30+h*k330)
        k430=f3(t0+h,u10+h*k310,u20+h*k320,u30+h*k330)
        u11=u10+h*(k110+(k210+k310)*2+k410)/6
        u21=u20+h*(k120+(k220+k320)*2+k420)/6
        u31=u30+h*(k130+(k230+k330)*2+k430)/6
        u10=u11
        u20=u21
        u30=u31
        t0=t0+h
        U1.append(u11) ;U2.append(u21); U3.append(u31); T.append(t0)
    else:
        break
u_1=np.array(U1); u_2=np.array(U2); u_3=np.array(U3); t=np.array(T)
import matplotlib.pyplot as plt
plt.plot(t,u_1,label='u1')
plt.plot(t,u_2,label='u2')
plt.plot(t,u_3,label='u3')
plt.legend()
plt.xlabel('t')
plt.ylabel('U')
plt.show()
