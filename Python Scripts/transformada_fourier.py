# -*- coding: utf-8 -*-
"""
Created on Mon Oct 05 12:31:59 2015

@author: Laura Rodríguez
"""

##TRANSFORMADA DE FOURIER (Rápida)

import numpy as np
import matplotlib.pyplot as plt

dt=0.1 ##paso de tiempo, cada cuanto están tomados los datos
t= np.arange(0,30,dt) #30 seg cada 0.2 seg

A1=3; A2=2
w1=3 ; w2=5

f = A1*np.sin(w1*t)+A2*np.cos(w2*t)

##graficar la fn
plt.figure()
plt.plot(t,f,'r-', linewidth=2, label=u'$F=%ssin(%st)+%scos(%st)$' %(A1,w1,A2,w2))
plt.xlabel(u'tiempo [s]')
plt.ylabel(u'función evaluada')
plt.legend(loc='best')
plt.show()


##trasnformada rápida de fourier 

A=np.fft.fft(f)
fr=np.fft.fftfreq(len(t), dt)

print A ##parte real y parte compleja (j) 
#lenA=300 longitud de los datos -> voy a tener tantos coef de fourier como datos tengo 
print fr
#lenf= 300 tantas freuencas como datos tengo 

fr.max()
#frec max = 1/(2*dt) --> frecuencia de nyquist 

#para graficar 
amplitud=np.abs(A)
potencia=np.abs(A)**2
total=np.sum(amplitud)
var=amplitud*100/total #varianza, qué porcentaje de varianza explica cada uno (relativas)

print amplitud
print var
print potencia

#grafica frec vs amplitud
plt.figure()
plt.plot(fr[:len(t)/2-1], amplitud[:len(t)/2-1]) #parte real
plt.plot(fr[len(t)/2:], amplitud[len(t)/2]) #parte imaginaria

#frec vs varianza
plt.plot(fr[:len(t)/2-1], 2*var[:len/2:]) #parte real





##filtrado -> para esocger una sola frecuencia

for i in range (len(fr)):
    if abs(fr[i])>0.67:
        A[i]=0
a_fil=np.abs(A)


##graf espectro filtrado 
plt.plot(fr[:len(t)/2-1], a_fil[:len(t)/2-1])




##transf inversa de fourier
fteo=A1*np.sin(w1*t)
fteo2=A2*np.cos(w2*t)

ff=np.fft.ifft(A)

        
        
        













