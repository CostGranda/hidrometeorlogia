# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 13:11:37 2015

@author: Laura Rodríguez
"""

import matplotlib.pyplot as plt
import numpy as np 

def LCG(seed, n, a=1664525, c=1013904223, m=2**32):
    numbers = []
    for i in range(n):
        seed = (a * seed + c) % m
        numbers.append(seed/m)

    return (numbers)

#print (LCG(2,100))


u1 = LCG(2,100)
#print(u1)
#
#plt.figure()
#plt.hist(u1, bins=50)
#
#
u2 = LCG(2,500)
#
#plt.figure()
#plt.hist(u2, color="magenta", bins=50)
#
#
u3 = LCG(2,1000)
#
#plt.figure()
#plt.hist(u3, color="green", bins=50)
#
u4 = LCG(2,10000)
#
#plt.figure()
#plt.hist(u4, color="red", bins=50)


#a1 = np.array([u4])
#p1 = np.percentile(a1, 90)
#print (p1)







#
def normal(m):
    n1 = np.array(m)
    x = []
    for i in range(0, len(n1), 2):
        x.append(np.sqrt(-2*np.log(n1[i]))*np.cos(2*np.pi*n1[i+1]))
        x.append(np.sqrt(-2*np.log(n1[i]))*np.sin(2*np.pi*n1[i+1]))
    return x 

nor1 = normal(u1)
nor2 = normal(u2)
nor3 = normal(u3)
nor4 = normal(u4)

#plt.figure()
#plt.hist(nor1, bins=50)
#
#plt.figure()
#plt.hist(nor2, bins=50, color="magenta")
#
#plt.figure()
#plt.hist(nor3, bins=50, color="green")
#
#plt.figure()
#plt.hist(nor4, bins=50, color="red")

        
a1 = np.array([nor1])
p1 = np.percentile(a1, [10,20,30,40,50,60,70,80,90])
print (p1)

a2 = np.array([nor2])
p2 = np.percentile(a2, [10,20,30,40,50,60,70,80,90])
print(p2)

a3 = np.array([nor3])
p3 = np.percentile(a3, [10,20,30,40,50,60,70,80,90])
print(p3)

a4 = np.array([nor4])
p4 = np.percentile(a4, [10,20,30,40,50,60,70,80,90])
print(p4)



    
    
    
    
    
    
    
    
    