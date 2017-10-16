# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 12:11:02 2015

@author: mamenac
"""

import numpy as np
import matplotlib.pylab as plt


##p(x,y) dependiente 

x = np.random.normal(0,1,1000)
z = np.random.normal(0,1,1000)

B=1
C=0.5
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
        h[i,:]=mat[i,:]/1000
        

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
plt.savefig('informacionmutuafinal.png')

    
#==================================================================
###SEGUNDA PARTE

from netCDF4 import Dataset 

Tmen= '/OISST_MonthClim_1982-2011.nc'
datos= Dataset(Tmen, mode='r')
var= [var for var in datos.variables]

print datos.variables['interpolated_sst']
