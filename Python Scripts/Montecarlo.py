# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 19:14:52 2015

@author: SARY
"""

import numpy as np
import matplotlib.pylab as plt
import scipy.stats as st

data = np.genfromtxt('Datos_Radiacion_Horizontal.txt')
date = data[:,0:3]
radiation = data[:,3]
print radiation
print date
y = np.array(radiation)
print y

#rezagos columnas
#filas lista

r= []
f,b = np.histogram(y, bins=60)
pcorrmont = np.zeros((1000, 1000))

for k in range(1000):
    lista = []
    for i in range(len(f)):
        na = np.random.uniform(b[i],b[i+1],f[i])
        for j in na:        
            lista.append(j)
            vecmont = np.random.shuffle(lista)
    r.append(vecmont)
    for l in range (1, 1000):
        corrmont[k, l], pv = st.spearmanr(lista[l:], lista[:-l])
        
for k in range(1000):
    lista = []
    for i in range(len(f)):
        na = np.random.uniform(b[i],b[i+1],f[i])
        for j in na:        
            lista.append(j)
            vecmont = np.random.shuffle(lista)
    r.append(vecmont)
    for l in range (1, 1000):
        pcorrmont[k, l], pv = st.pearsonr(lista[l:], lista[:-l])
    
pp95m=[]
for l in range(1, 1000):
    pp95 = np.percentile(pcorrmont[:,l:], 95)
    pp95m.append(p95)    
    print pp95m
    
m1=np.zeros(1000)
m1[0] = 1.
for j in range (1, 1000):
        m1[j], pv = st.pearsonr(y[j:], y[:-j])
        
        
plt.plot(m0, color='g')
plt.plot(m1, color='b')
plt.plot(p5m, color='g')
plt.plot(p95m, color='g')
plt.plot(pp5m, color='b')
plt.plot(pp95m, color='b')
plt.title('Autocorrelograma Montecarlo')  # Colocamos el título del gráfico
plt.xlabel('LAG')  # Colocamos la etiqueta en el eje x
plt.ylabel('Coeficiente de Correlacion')

plt.legend( ('Spearman', 'Pearson'), loc = 'upper right')