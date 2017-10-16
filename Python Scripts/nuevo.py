# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 12:58:30 2015

@author: Laura Rodríguez
"""
import numpy as np
import pylab as py
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as st

#LLamar los datos 
Q = "DTT.txt"
y=np.loadtxt(Q,dtype=np.float)

n=len(y)


F,b = np.histogram(y,50)
 
for i in F:
    p = map(float, F)
    p =np.array(p)

P = p/n

pcorrmont = np.zeros((1000, 1000))
corrmont = np.zeros((1000,1000))

r=[]
for k in range(1000):
    lista = []
    for j in range(len(F)):
        na = np.random.uniform(b[j],b[j+1],round(P[j]*1000))
        for i in na:        
            lista.append(i)
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