# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 19:20:29 2020

@author: Himanshu Tyagi
"""

##Relaxation Method for solving BVP
##x''[t]=-10 and x[0]=0, x[10]=0
##in relaxation method x(t)=0.5*[x(t-h)+x(t+h)]+0.5*10*h**2
import numpy as np
import matplotlib.pyplot as plot
x=np.zeros(100)
tf=10
h=tf/100
for i in range(10001):
    x[1:-1]=0.5*(x[2:]+x[:-2])+0.5*10*h**2
    t=np.linspace(0,10,len(x))
    if i==10000:
        plot.plot(t,x,'tab:red')
    else:
        pass
    if i==5000 or i==7000 or i==8000 or i==6000:
        plot.plot(t,x,'tab:gray')
    else:
        pass
print(x)        
    
plot.grid()
plot.show()    
    
        