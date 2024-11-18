#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 13:58:53 2020
@author: thkam
"""

import numpy as np
from scipy import special
import matplotlib.pyplot as plt
 
def qfunction(x):
    return 0.5*special.erfc(x/np.sqrt(2))
def A1(x):
    return np.exp(-(x**2)/2)
def A2(x):
    return (0.25*np.exp(-x**2)+0.25*np.exp(-(x**2)/2))
def A3(x):
    return (0.0833*np.exp(-(x**2)/2)+0.25*np.exp(-(2*(x**2))/3))

x = np.linspace(2.0, 7.0, 100)
#this is new code
t= np.linspace(2.0, 7.0, 1000)
c1=np.absolute(A1(t)-qfunction(t))
c2=np.absolute(A2(t)-qfunction(t))
c3=np.absolute(A3(t)-qfunction(t))
g=np.absolute(qfunction(t))
I1=np.trapz(c1/g, t)
I2=np.trapz(c2/g, t)
I3=np.trapz(c3/g, t)

#this is new code


Q = qfunction(x)
Q1= A1(x)
Q2=A2(x)
Q3=A3(x)

plt.close('all')
plt.figure(1)
plt.semilogy(x, Q, label='Q')
plt.semilogy(x, Q1, linestyle='dashed', label='Q1')
plt.xlabel('x')
plt.ylabel('Q')
plt.legend()
plt.show()
plt.figure(2)
plt.semilogy(x, Q, label='Q')
plt.semilogy(x, Q2, linestyle='dashed', label='Q2')
plt.xlabel('x')
plt.ylabel('Q')
plt.legend()
plt.show()
plt.figure(3)
plt.semilogy(x, Q, label='Q')
plt.semilogy(x, Q3, linestyle='dashed', label='Q3')
plt.xlabel('x')
plt.ylabel('Q')
plt.legend()
plt.show()

print(I1)
print(I2)
print(I3)


