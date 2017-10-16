# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 19:49:39 2015

@author: Don Roge
"""
#Generación de números aleatorios que sigan la distribución de una serie de datos
import numpy as np
import pylab as py
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as st

#Ubicación de los datos, abrirlos, leerlos y guardarlos
Q ="C:\Users\Don Roge\Downloads\Analisis\DTT.txt"
f=np.loadtxt(Q,dtype=np.float)

#l=f[:,7]
n=len(f)

##Graficar el histograma de los datos y generar los vectores asociados
plt.figure()
plt.hist(f,bins=50)
plt.title('Histograma Serie de datos')
plt.show

F,b = np.histogram(f,10)

##Convertir datos enteros en flotantes 
for i in F:
    p = map(float, F)
    p =np.array(p)
##################################################### CREAR ALEATORIOS FORMA 1    
####################### FORMA 1
#Frecuencia relativa
P = p/n
#print P

varios=[]
def listas():
    global numal
    global na
    numal=[]
    for j in range(0, len(P)):
        na = np.random.uniform(b[j],b[j+1],round(P[j]*1001))    
        for i in na:
            numal.append(i)
    return(numal)
for k in range(0,1000):           
    varios.append(listas())
    
r=np.array(varios)

#numal=[]
#for j in range(0, len(P)):
#    na = np.random.uniform(b[j],b[j+1],round(P[j]*1000))    
#    for i in na:
#        numal.append(i)            
        
plt.figure()
plt.hist(numal,bins=50, color="g")
plt.title('Histograma Numeros Aleatorios')
plt.show

####################### FORMA 2
#A = min(f)
#B = max(f)
#interv=50
#rango = (B-A)/interv
#
#r=int(rango)
#lista=[]
#for i in range(0,interv+1):
#    lista.append(r*i)
#
#t=[]
#for i in range (0,len(lista)-1):
#    t.append(float(((f >= A+lista[i]) & (f < A+lista[i+1])).sum())/float(len(f)))    
#
#numal=[]
#for j in range(0, len(t)):
#    na = np.random.uniform(lista[j],lista[j+1],round(t[j]*10000))
#    for i in na:
#        numal.append(i)
#
#plt.figure()
#plt.hist(numal,bins=50,color='b')
#plt.title('Distribucion de numeros aleatorios')
#plt.show 

####################################################### CORRELACIONES
##################### AUTOCORRELACIONES DE LA SERIE
np.random.shuffle(f)
#Pearson para la serie
a=[]
for i in range(0,10):
    pe=st.pearsonr(f[i:],f[:3075-i])
    a.append(pe)

#Spearman para la serie 
b=[]
for i in range (0,10):
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


###################### AUTOCORRELACIONES DE LOS ALEATORIOS

MPe=np.zeros((1000,1000))
MSp=np.zeros((1000,1000))

for k in range(0, 1000):
    rand=np.concatenate((varios[0],varios[1],varios[2],varios[3],varios[4],varios[5],varios[6],varios[7],varios[8],varios[9]),1)
    np.random.shuffle(rand)
    for i in range (0,1000):
        pe=st.pearsonr(rand[i:],rand[:(len(rand)-i)])
        sp=st.spearmanr(rand[i:],rand[:(len(rand)-i)])
        MPe[k,i]=pe[0]
        MSp[k,i]=sp[0]

MatPerc=np.zeros((4,100))
for i in range(1,100):
    PercPe=np.percentile(MPe[:,i],95)
    PercPe2=np.percentile(MPe[:,i],5)
    PercSp=np.percentile(MSp[:,i],95)
    PercSp2=np.percentile(MSp[:,i],5)
   
    MatPerc[0,i]=PercPe
    MatPerc[1,i]=PercPe2
    MatPerc[2,i]=PercSp   
    MatPerc[3,i]=PercSp2
    
plt.figure()
plt.plot(pe, color="red");plt.plot(sp, color="blue")
plt.plot(MatPerc[0,:], color="green"); plt.plot(MatPerc[1,:], color="orange")
plt.plot(MatPerc[2,:], color="green", ls='--'); plt.plot(MatPerc[3,:], color="orange", ls='--')
plt.ylabel("Coeficiente de correlacion")
plt.xlabel("Rezagos")
plt.plot(pe, color="red"); #mela
plt.plot(sp, color="blue")


#usar solo los datos que necesito
m=[]
for i in range(len(peal)):
    m.append(peal[i][0])

n=[]
for i in range(len(spal)):
    n.append(spal[i][0])
                    
#PercPe=np.percentile(MPe,[5,95], axis=0)
#PercSp=np.percentile(MSp,[5,95], axis=0)
#
#plt.figure()
#plt.plot(peal, color="red");plt.plot(spal, color="blue")
#plt.plot(PercPe, color="green"); plt.plot(PercSp, color="orange")
#plt.show()
    

    
    
    
    


