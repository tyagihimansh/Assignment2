# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 23:51:49 2020

@author: Himanshu Tyagi
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as int
def f(t,y):   
    return(np.vstack([y[1],-1*np.exp(-2*y[0])]))
def bcf(ya,yb):                 
    return(np.array([ya[0],yb[0]-np.log(2)]))
t_1=np.linspace(1,2,20)           
y_1=np.zeros([2,len(t_1)])       
y1=int.solve_bvp(f,bcf,t_1,y_1)
t1=np.linspace(1,2,200)          
plt.subplot(2,2,1,title='f')      
plt.plot(t1,y1.sol(t1)[0],label='f')

def g(t,y):
    return(np.vstack([y[1],((y[1]*np.cos(t))-(y[0]*np.log(y[0])))]))
def bcg(ya,yb):
    return(np.array([ya[0]-1,yb[0]-np.exp(1)]))
t_2=np.linspace(0,0.5*np.pi,20)
y_2=np.ones([2,len(t_2)])
y2=int.solve_bvp(g,bcg,t_2,y_2)
t2=np.linspace(0,0.5*np.pi,200)
plt.subplot(2,2,2,title='g')
plt.plot(t2,y2.sol(t2)[0],label='g')

def h(t,y):
    return(np.vstack((y[1],(-1/np.cos(t))*((2*(y[1]**3))+((y[0]**2)*y[1])))))
def bch(ya,yb):
    return(np.array([ya[0]-2**(-1/4),yb[0]-((12**(1/4))/2)]))
t_3=np.linspace(np.pi/4,np.pi/3,20)
y_3=np.zeros([2,len(t_3)])
y3=int.solve_bvp(h,bch,t_3,y_3)
t3=np.linspace(np.pi/4,np.pi/3,200)
plt.subplot(2,2,3,title='h')
plt.plot(t3,y3.sol(t3)[0],label='h')

def i(t,y):
    return(np.vstack([y[1],0.5-0.5*y[1]**2-(y[0]*np.sin(t/2))]))
def bci(ya,yb):
    return(np.array([ya[0]-2,yb[0]-2]))
t_4=np.linspace(0,np.pi,20)
y_4=np.zeros([2,len(t_4)])
y4=int.solve_bvp(i,bci,t_4,y_4)
t4=np.linspace(np.pi/4,np.pi/3,200)
plt.subplot(2,2,4,title='i')
plt.plot(t4,y4.sol(t4)[0],label='i')
plt.legend()
plt.show()

