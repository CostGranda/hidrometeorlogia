# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 10:46:11 2015

@author: Laura Rodríguez
"""

import numpy as np
import pylab as py
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as st

#LLamar los datos 
Q = "DTT.txt"
f=np.loadtxt(Q,dtype=np.float)

n=len(f)

##Graficar el histograma de los datos y generar los vectores asociados
plt.figure()
plt.hist(f,bins=50)
plt.title('Histograma Serie de datos')
plt.show


F,b = np.histogram(f,50)

##Convertir datos enteros en flotantes 
for i in F:
    p = map(float, F)
    p =np.array(p)
    
##Generación de aleatorios y sus autocorrelaciones 
#Frecuencia relativa
P = p/n

MPe=np.zeros((1000,1000))
MSp=np.zeros((1000,1000))

r = []
for k in range(0, 1000):
    numal=[]
    for j in range(0, len(P)):
        na = np.random.uniform(b[j],b[j+1],round(P[j]*1001))    
        for i in na:
            numal.append(i)
    lista = np.random.shuffle(numal)
    r.append(lista)
    for l in range (0,1000):
        pe=st.pearsonr(numal[l:], len(numal[:-l]))
        sp=st.spearmanr(numal[l:], len(numal[:-l]))
        MPe[k,l]=pe[0]
        MSp[k,l]=sp[0]










##################### AUTOCORRELACIONES DE LA SERIE
np.random.shuffle(f)
#Pearson para la serie
a=[]
for i in range(0,100):
    pe=st.pearsonr(f[i:],f[:3075-i])
    a.append(pe)

#Spearman para la serie 
b=[]
for i in range (0,100):
    sp=st.spearmanr(f[i:],f[:3075-i])
    b.append(sp)

#a1=np.reshape(a,(10,2))

#usar solo los datos que necesito
g=[]
for i in range(len(a)):
    g.append(a[i][0])

h=[]
for i in range(len(b)):
    h.append(b[i][0])

plt.figure()
plt.plot(g, color="r");plt.plot(h, color="b")
plt.title("Autocorrelograma serie de datos SST")
plt.xlabel("Rezagos")
plt.ylabel("Correlacion")
plt.show()
plt.legend("PS")