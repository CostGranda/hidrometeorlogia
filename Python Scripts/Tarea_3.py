# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 17:12:45 2015

@author: Don Roge
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import scipy.stats.stats as st
from netCDF4 import Dataset

caudal="Datos_T3.txt"
Q=np.loadtxt(caudal,dtype=np.float)

#Retirar ciclo anual -Derivada

c=[]
for t in range(0,len(Q)):
    y=Q[t]-Q[t-1]
    c.append(y)

for i in c:
    ca = map(float, c)
    ca =np.array(c)
    

    
#Correlaciones 
#Pearson para la serie
a=[]
for i in range(0,20):
    pe=st.pearsonr(ca[i:],ca[:1827-i])
    a.append(pe)

#Spearman para la serie 
b=[]
for i in range (0,20):
    sp1=st.spearmanr(ca[i:],ca[:1827-i])
    b.append(sp1)

#los datos que sirven
g=[]
for i in range(len(a)):
    g.append(a[i][0])

h=[]
for i in range(len(b)):
    h.append(b[i][0])

plt.figure()
plt.plot(g, color="r");plt.plot(h, color="b")
plt.title("Autocorrelograma serie de datos Caudales")
plt.xlabel("Rezagos")
plt.ylabel("Correlacion")
plt.show()
plt.legend("PS")
plt.savefig('autocorrelograma')

plt.figure()
plt.hist(Q,bins=10)
plt.title('Histograma Serie de datos')
plt.show

######################Ahora con los números aleatorios
F,b = np.histogram(Q,10)

##Convertir datos enteros en flotantes 
for i in F:
    p = map(float, F)
    p =np.array(p)

P = p/len(Q)

#######################Solo me esta corriendo una vez la correlación

MPe=np.zeros((1000,100))
MSp=np.zeros((1000,100))

numal=[]
for k in range(0, 1000):
    for j in range(0, len(P)):
        na = np.random.uniform(b[j],b[j+1],round(P[j]*1000))    
    numal.append(na)

for i in numal:
    num = map(float, numal)
    num =np.concatenate(num)
    np.random.shuffle(num)

    for m in range (0,100):
        pe=st.pearsonr(num[m:],num[:len(num)-m])
        MPe[k][m]=pe[0]
        sp1=st.spearmanr(num[m:],num[:len(num)-m])
        MSp[k][m]=sp1[0]
        
autosp=[]
for j in range (0,1000):
    v1=[]
    for i in range (0,100):  
        v= st.spearmanr(num[i:],num[:len(num)-i])
        v1.append(v[0])
    np.random.shuffle(num)
    autosp.append(v1)


matsp= np.zeros((1000,100))
for i in range (1000):
    matsp[i][:]=autosp[i]



autope=[]
for j in range (0,1000):
    v2=[]
    for i in range (0,100):  
        c= st.pearsonr(num[i:],num[:len(num)-i])
        v2.append(c[0])
    np.random.shuffle(num)
    autope.append(v2)


matpe= np.zeros((1000,100))
for k in range (1000):
    matpe[k][:]=autope[k]

#plt.figure()
#plt.hist(numal,bins=10, color="g")
#plt.title('Histograma Numeros Aleatorios')
#plt.show
        
Mperc=np.zeros((4,100))
for n in range(1,100):
    psp=np.percentile(matsp[:,n],95)
    psp2=np.percentile(matsp[:,n],5)
    ppe=np.percentile(matpe[:,n],95)
    ppe2=np.percentile(matpe[:,n],5)
   
    Mperc[0,n]=psp
    Mperc[1,n]=psp2
    Mperc[2,n]=ppe   
    Mperc[3,n]=ppe2

plt.figure()
plt.plot(g, "r");plt.plot(h, "b");plt.plot(Mperc[0,:], "g"); plt.plot(Mperc[1,:], "m")
plt.title("Autocorrelograma serie de datos Caudales")
plt.xlabel("Rezagos")
plt.ylabel("Correlacion")
plt.show()
plt.legend("PS")
plt.show()
plt.savefig('autocosp')

plt.figure()
plt.plot(g, "r");plt.plot(h, "b");plt.plot(Mperc[2,:], "g"); plt.plot(Mperc[3,:], "m")
plt.title("Autocorrelograma serie de datos Caudales")
plt.xlabel("Rezagos")
plt.ylabel("Correlacion")
plt.show()
plt.legend("PS")
plt.show()
plt.savefig('autocope')



############################### BOOTSTRAPING

boot=[]

for g in range (len(Q)):
    u=Q[g]
    boot.append(u)
boot=np.array(boot)

H=np.zeros((1000,100))
D=np.zeros((1000,100))
q1=np.zeros((len(Q),1))

for k in range (1000):
    S=np.random.random_integers(0,high=1826, size=1827)
    
    for j in range (0,1827):
        q1[j][0]=boot[S[j]]
    for i in range (0,100):
        b=st.pearsonr(q1[i:], q1[:len(Q)-i])
        c=st.spearmanr(q1[i:], q1[:len(Q)-i])
        H[k][i]=b[0]
        D[k][i]=c[0]
        


Mpercentiles=np.zeros((4,100))
for z in range(1,100):
    l=np.percentile(H[:,z],95)
    l1=np.percentile(H[:,z],5)
    n=np.percentile(D[:,z],95)
    n1=np.percentile(D[:,z],5)
   
    Mpercentiles[0,z]=l
    Mpercentiles[1,z]=l1
    Mpercentiles[2,z]=n   
    Mpercentiles[3,z]=n1

plt.figure()
plt.plot(g, "r");plt.plot(h, "b");plt.plot(Mpercentiles[0,:], "g"); plt.plot(Mpercentiles[1,:], "m")
plt.title("Autocorrelograma serie de datos Caudales")
plt.xlabel("Rezagos")
plt.ylabel("Correlacion")
plt.show()
plt.legend("PS")
plt.show()
plt.savefig('bootpearson')

plt.figure()
plt.plot(g, "r");plt.plot(h, "b");plt.plot(Mperc[2,:], "g"); plt.plot(Mperc[3,:], "m")
plt.title("Autocorrelograma serie de datos Caudales")
plt.xlabel("Rezagos")
plt.ylabel("Correlacion")
plt.show()
plt.legend("PS")
plt.show()
plt.savefig('bootspearman')



    
    
    
