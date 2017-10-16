# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 13:34:19 2015

@author: Simon Rico
"""

import numpy as np 
from scipy import stats as st
import matplotlib.pyplot as plt
from scipy import linalg as la

###1ra matriz y llenarla con los datos de la funcion seno#
A=np.zeros((100,200))
for i in range(200):
    a=np.sin((2*np.pi*i)/199)
    A[:,i]=a
plt.figure()
plt.plot(A[0],label='f=sen(x)') 
plt.legend(loc='best' )
#Crear la lista con la distribucion normal para ambos ejes
X=np.linspace(-4,4,200) #Crea una lista entre los -4 y 4 con 200 separaciones
X1=st.norm.pdf(X,0,1) 
Y=np.linspace(-4,4,100)
Y1=st.norm.pdf(Y,0,1)
#Multiplicamos la matriz por la distribucion normal
for i in range(100):
    A[i,:]=A[i,:]*X1
for j in range(200):
    A[:,j]=A[:,j]*Y1
G=plt.figure()
a=G.add_subplot(211)
a=plt.plot(A[10])
plt.title('Fila 10')
b=G.add_subplot(212)
b=plt.plot(A[50])
plt.title('Fila50')

#Creamos la componente temporal 
A1=np.zeros((200,100,200))
for i in range(200):
    A1[i,:,:]=np.roll(A,i,axis=1)
#Grafica para mostrar el desplazamiento de la serie en el tiempo
#F=plt.figure()
#plt.suptitle('Desplazamiento temporal') 
#a=F.add_subplot(221)
#a=plt.contourf(A1[0])
#plt.title('t=0')
#b=F.add_subplot(222)
#b=plt.contourf(A1[50])
#plt.title('t=50')
#c=F.add_subplot(223)
#c=plt.contourf(A1[100])
#plt.title('t=100')
#d=F.add_subplot(224)
#d=plt.contourf(A1[150])
#plt.title('t=150')
    
#####Fourier en el espacio######
ampE=np.zeros((200,100,200), dtype=complex) #coeficiente
freqE=np.fft.fftfreq(200,1)  #numero de onda
for i in range(200):
    for j in range(100):
        ampE[i,j,:]=np.fft.fft(A1[i,j,:]) #coeficiente  
#####Fourier en el tiempo######
ampT=np.zeros((200,100,200), dtype=complex) #coeficiente #amp val abs de coefs
freqT=np.fft.fftfreq(200,1)
for i in range(100):
    for j in range(200):
        ampT[:,i,j]=np.fft.fft(ampE[:,i,j])
amplitud=np.abs(ampT) 

#Desplazar la amp segun el orden de las frec de FFT de menor a mayor
ampT1=np.zeros((200,100,200))
for i in range(200):
    ampT1[i]=np.roll(amplitud[i],100,axis=1)
#selecciono una linea de latitud 
G=np.abs(ampT1[:100,50,:])
X,Y=np.meshgrid(np.roll(freqE,100),freqT[:100])
plt.contourf(X,Y,G)
plt.colorbar()
plt.title('Amplitud 2da FFT fila 50')
plt.xlabel('Longitud de onda')
plt.ylabel('Frecuencia')

###############################################
#####################EOF#######################
##############################################
#Matriz para hacerle la correlacion
C=np.zeros((200,20000))
for i in range(200):
    C[i]=np.reshape(A1[i],(1,20000))

mat_cov=np.dot(C,C.T)
e_vals, e_vecs = la.eig (mat_cov)
sum_vals=np.sum(e_vals)
var_explicada=(e_vals/sum_vals)*100
#plt.plot(sorted(var_explicada[0:10], reverse=True))

#componentes principales
cp=np.dot(e_vecs.T,C)
#Hacer el reshape a las cp para que de de nuevo una matriz (200,100,200)
EOF=np.zeros((200,100,200))
for i in range(200):
    EOF[i]=np.reshape(cp[i],(100,200))

#Grafica de las EOF que mas varianza representan
#H=plt.figure()
#plt.suptitle('EOF representativas') 
#a=H.add_subplot(221)
#a=plt.contourf(EOF[0])
#plt.title('EOF 1')
#b=H.add_subplot(222)
#b=plt.contourf(EOF[1])
#plt.title('EOF 2')
#c=H.add_subplot(223)
#c=plt.contourf(EOF[2])
#plt.title('EOF 3')
#d=H.add_subplot(224)
#d=plt.contourf(EOF[3])
#plt.title('EOF 4')
