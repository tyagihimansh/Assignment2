# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 23:16:45 2020

@author: Himanshu Tyagi
"""

import numpy as np
from scipy import integrate as int
import matplotlib.pyplot as plot
def f(t,y):
    return t*np.exp(3*t)-2*y
def g(t,y):
    return 1-(t-y)**2
def h(t,y):
    return 1+y/t
def i(t,y):
    return np.cos(2*t)+np.sin(3*t)    

solf = int.solve_ivp(f,(0,1),[0],t_eval=np.linspace(0,1,100))
solg = int.solve_ivp(g,(2,3),np.array([0]),t_eval=np.linspace(2,3,100))
solh = int.solve_ivp(h,(1,2),[2],t_eval=np.linspace(1,2,100))
soli = int.solve_ivp(i,(0,1),[1],t_eval=np.linspace(0,1,100))

f=solf.y
tf=solf.t
g=solg.y
tg=solg.t
h=solh.y
th=solh.t
i=soli.y
ti=soli.t
plot.xlabel('x')
plot.ylabel('f')
plot.plot(tf,f[0],'tab:green');plot.show()
plot.xlabel('x')
plot.ylabel('g')
plot.plot(tg,g[0],'tab:blue');plot.show()
plot.xlabel('x')
plot.ylabel('h')
plot.plot(th,h[0],'r');plot.show()
plot.xlabel('x')
plot.ylabel('i')
plot.plot(ti,i[0],'tab:orange');plot.show()