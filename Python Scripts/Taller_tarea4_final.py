# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 12:11:02 2015

@author: mamenac
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy as scipy
import pandas as pnd


##p(x,y) dependiente 

x = np.random.normal(0,1,1000)
z = np.random.normal(0,1,1000)

B=1
C=0.5
K=np.sqrt((B**2)+(C**2))

y = ((B*x)+(C*z))/K

plt.figure()
plt.hist2d(x,y,bins=20)
plt.show()


#escalada p(x,y) 
hi=np.histogram2d(x,y,20)

h=np.zeros((20,20))
mat=hi[0]

for i in range (0,20):
        h[i,:]=mat[i,:]/1000

#####TRANSPONER LA MATRIZ 

h1= np.zeros((20,20))
for i in range (0,20):
    for j in range(0,20):
        h1[i,j]=h[i,-1-j]
        
ht= np.matrix.transpose(h1)

#histograma de escalada p(x,y)        
plt.figure()
plt.imshow(h, interpolation='None')
plt.title("Histograma dependiente con B=1 y C=0,5")
plt.colorbar()
plt.show()
plt.savefig('histogramadependiente.png')


### f(x)g(y) INDEPENDIENTE 

Fx=np.histogram(x,20)
Gy=np.histogram(y,20)

Fxx= Fx[0]
Gyy=Gy[0]

indep= Fxx*Gyy

F,b = np.histogram(x,20)
for i in F:
    p = map(float, F)
    p =np.array(p)

P = p/len(x)

F1,b = np.histogram(y,20)
for i in F1:
    p1 = map(float, F1)
    p1 =np.array(p1)

P1 = p1/len(y)


Mt= np.zeros((20,20))
for i in range (0,20):
    for j in range (0,20):
        Mt[i,j]=P[i]*P1[j]
        
#plt.figure()       
#plt.imshow(Mt,interpolation='None')
plt.colorbar()
plt.show()
plt.savefig('histogramaindependiente.png')

#plt.contourf() ##graficar matrices de una vez al derecho 

###distribución escalada 

esc= np.zeros((20,20))
for i in range (0,20):
    for j in range (0,20):
        esc[i,j]=mat[i,j]/indep[i]



#plt.figure()
#plt.imshow(esc, interpolation='None')
plt.colorbar()

plt.savefig('escalado.png')



#información mutua

X=np.random.normal(0.0,1.0,size=1000)
Z=np.random.normal(0.0,1.0,size=1000)
B=1.0
C=1.0
K=np.sqrt(B**2.0+C**2.0)

Y=(B*X+C*Z)/K


Bi=20
def mutualinformation (X,Y,bins=Bi):
    pxy,b1,b2=np.histogram2d(X,Y,bins=Bi)
    fx=np.histogram(X, bins=Bi)[0]; fx=fx.astype(float)
    gy=np.histogram(Y, bins=Bi)[0]; gy=gy.astype(float)
    pxy=pxy/pxy.sum();fx=fx/fx.sum()
    gy=gy/gy.sum()    
    val=0
    for posX, i in enumerate (fx):
        for posY, j in enumerate (gy):
            v=pxy[posX,posY]*np.log2(pxy[posX,posY]/(i*j))
            if np.isfinite(v):
                val+=v
    return val
val=mutualinformation(X,Y,Bi)


#Información mutua

mutual=[]
c=[]
for C in np.arange(0.0,3.0,0.1):
    k=np.sqrt(B**2.0+C**2.0)
    Y=(B*X+C*Z)/K        
    mutual.append(mutualinformation(X,Y,Bi))
    c.append(C)

plt. figure()
plt.plot(c,mutual)
plt.show
plt.savefig('informacionmutua.png')

############# Con la serie
campoviento= "68_Vientos_2013.txt"
x=np.loadtxt(campoviento, dtype="string")
o=x[:,2]
y=x[:,3]
z=x[:,4]
o =np.float64(o)

start = pnd.datetime(2013, 02, 01, 15, 15) 
end = pnd.datetime(2013, 12, 31, 23, 59)
rng = pnd.date_range(start, end, freq="min")

tss=pnd.DataFrame(data={"velocidad": o },index=rng,dtype=float)

tss= tss[tss!=-999.0]
mediahoraria=tss["velocidad"].resample("H", how="mean") 

has=0
des=0
nor=np.zeros(len(mediahoraria))
index=[]
for r in range(24):
    has+=len(mediahoraria.at_time(str(r)+":00:00"))
    cd=mediahoraria.at_time(str(r)+":00:00")
    nor[des:has]=(cd-cd.mean())/cd.std()
    index.extend(cd.index.tolist())
    des=has
tss2=pnd.DataFrame(nor,index=index,columns=['velocidad']).sort_index() 
tss2=tss2.dropna()

### Rezagos

x1=tss2.values
x1=np.concatenate(x1)
mutual=[]
rez=[]
for i in range (0,20):  
    val=mutualinformation(x1[i:len(x1)],x1[:len(x1)-i],Bi)
    rez.append(i)
    mutual.append(val)

plt. figure()
plt.plot(rez,mutual)
plt.show
plt.savefig('informacionmutuaserie.png')

mut= np.array(mutual)
rezagos=np.array(rez)

###### GRAFICAS 


##p(x,y) dependiente 

x = x1
z = np.random.normal(0,1,7731)

B=1
C=1 #rezagos
K=np.sqrt((B**2)+(C**2))

y = ((B*x)+(C*z))/K

plt.figure()
plt.hist2d(x,y,bins=20)
plt.colorbar()
plt.show()


#escalada p(x,y) 
hi=np.histogram2d(x,y,20)

h=np.zeros((20,20))
mat=hi[0]

for i in range (0,20):
        h[i,:]=mat[i,:]/7731
        

#####TRANSPONER LA MATRIZ 

#h1= np.zeros((20,20))
#for i in range (0,20):
#    for j in range(0,20):
#        h1[i,j]=h[i,-1-j]
#        
#ht= np.matrix.transpose(h1)

#histograma de escalada p(x,y)        
#plt.figure()
#plt.imshow(h, interpolation='None')
plt.colorbar()
plt.show()
plt.savefig('histogramadependienteserie_10.png')



### f(x)g(y) INDEPENDIENTE 

Fx=np.histogram(x,20)
Gy=np.histogram(y,20)

Fxx= Fx[0]
Gyy=Gy[0]

indep= Fxx*Gyy

F,b = np.histogram(x,20)
for i in F:
    p = map(float, F)
    p =np.array(p)

P = p/len(x)

F1,b = np.histogram(y,20)
for i in F1:
    p1 = map(float, F1)
    p1 =np.array(p1)

P1 = p1/len(y)


Mt= np.zeros((20,20))
for i in range (0,20):
    for j in range (0,20):
        Mt[i,j]=P[i]*P1[j]
        
#plt.figure()       
#plt.imshow(Mt,interpolation='None')
plt.colorbar()
plt.show()
plt.savefig('histogramaindependienteserie_10.png')

#plt.contourf() ##graficar matrices de una vez al derecho 

###distribución escalada 

from matplotlib import ticker


esc= np.zeros((20,20))
for i in range (0,20):
    for j in range (0,20):
        esc[i,j]=mat[i,j]/indep[i]



#plt.figure()
#plt.imshow(esc, interpolation='None')
#plt.contourf(esc,locator = ticker.LogLocator())
plt.colorbar()
plt.show()
plt.savefig('escaladoserie_1.png')















