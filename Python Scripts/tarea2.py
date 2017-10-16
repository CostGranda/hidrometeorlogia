# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 12:43:10 2015

@author: user
"""
import numpy as np
import pylab as pb
import matplotlib.pyplot as plt
import random as rd


dire=open("vlr.txt", "r") #llamar los datos 
x=[]
for linea in dire:
    linea = linea[:-1]  #borra \n
    x.append(float(linea)) #for para llenar una lista vacía con los datos 

ndatos=len(x)

print(plt.hist(x)) #histograma de las precipitaciones 



def Histcopy(bins,x,ndatos):
    rango=np.arange(bins+1)
    rang=[]
    y=((max(x)-min(x))/rango[-1])
    for i in range(len(rango)):
        rang.append(min(x)+(y*i))
        
    fre=[]
    pro=[]
    for i in range(len(rang)-1):
        fre.append(((rang[i] <= x) & (x < rang[i+1])).sum())
        pro.append(float(((rang[i] <= x) & (x < rang[i+1])).sum())/float(len(x)))
    w=[]    
    min1=rd.uniform(754,0.001) #dato mínimo de las precipitaciones
    max1=rd.uniform(2177,100) #dato máximo 
    r=((max1-min1)/len(pro))
    rang=[]
    for i in range(len(pro)+1):
        rang.append(min1+(r*i))
    for i in range(len(pro)):
        if (ndatos*pro[i]-int(ndatos*pro[i]))<0.5:
            k=int(ndatos*pro[i])
        else:
            k=int(ndatos*pro[i])+1
        for q in range(k):
            w.append(rd.uniform(rang[i],rang[i+1]))
    plt.hist(w,bins=len(pro))
#    plt.title('Serie aleatoria de '+str(ndatos)+' datos')
    return w

h= Histcopy(10,x,ndatos) #se llama a la función histocopy para que se ejecute 
plt.hist(h) #histograma de los numeros aleatorios 