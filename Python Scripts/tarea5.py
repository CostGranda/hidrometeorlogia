# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 18:03:25 2015

@author: Laura Rodríguez
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg as la


dt= 0.1
t=np.arange(0,50,dt)


A=2
B=5
C=2
D=9
E=2
F=7
G=1
H=8
n=np.random.normal(0,1,500)
m=np.random.normal(0,1,500)

f1= A*t
f2=B*np.sin(C*t)
f3=D*np.cos(E*t)
f4=F*n

f=f1+f2+f3+f4

g1= -G*A*t
g2= -B*np.sin(C*t)
g3= D*np.cos(E*t)
g4= H*m

g= g1+g2+g3+g4

plt.figure()
plt.plot(t,f3)
plt.show()
#plt.savefig('ruidoG.png')


#========================
#transformada de Fourier
#========================
A=np.fft.fft(f3)
fr=np.fft.fftfreq(len(t),dt)
#print A
#print fr


amplitud=np.abs(A)
potencia=np.abs(A)**2
total=np.sum(potencia)
var=potencia*100/total


#print var
#print potencia
#print amplitud

###gráfica de la frecuencia vs amplitud
plt.figure()
plt.plot(fr[:len(t)/2-1], amplitud[:len(t)/2-1], 'g-', linewidth = 2, label = u'Amplitud positiva')  # Dibujamos los valores de las parejas ordenadas con una línea contínua
#plt.plot(fr[len(t)/2:], amplitud[len(t)/2:], 'b-', linewidth = 2, label = u'Amplitud negativa')
plt.title(u'Transformada Rápida de Fourier')  # Colocamos el título del gráfico
plt.xlabel(u'frecuencia [Hz]')  # Colocamos la etiqueta en el eje x
plt.ylabel('Amplitud')  # Colocamos la etiqueta en el eje y
plt.legend(loc='best')
#Guardar la imagen
#plt.savefig('fft_G.png')
plt.show()

####gráfica de la frecuencia vs potencia
plt.figure()
plt.plot(fr[:len(t)/2-1], potencia[:len(t)/2-1], 'k-', linewidth = 2, label = u'Potencia positiva')  # Dibujamos los valores de las parejas ordenadas con una línea contínua
# plt.plot(fr[len(t)/2:], potencia[len(t)/2:], 'r-', linewidth = 2, label = u'Potencia negativa')
# plt.title('Potencia espectral' )  # Colocamos el título del gráfico
plt.xlabel(u'frecuencia [Hz]')  # Colocamos la etiqueta en el eje x
plt.ylabel(u'Potencia espectral')  # Colocamos la etiqueta en el eje y
#Guardar la imagen
# plt.savefig('fft(Potencia).png')
plt.show()
#

####gráfica de la frecuencia vs varianza
plt.figure()
# plt.plot(fr[:len(t)/2-1], var[:len(t)/2-1], 'g-', linewidth = 2, label = u'varianza')  # Dibujamos los valores de las parejas ordenadas con una línea contínua
# plt.plot(fr[len(t)/2:], var[len(t)/2:], 'g-', linewidth = 2, label = u'varianza')
plt.plot(fr[:len(t)/2-1], 2*var[:len(t)/2-1], 'g-', linewidth = 2, label = u'varianza')  # Dibujamos los valores de las parejas ordenadas con una línea contínua

plt.title('Porcentaje de varianza explicado' )  # Colocamos el título del gráfico
plt.xlabel(u'frecuencia [Hz]')  # Colocamos la etiqueta en el eje x
plt.ylabel(u'porcentaje de varianza')  # Colocamos la etiqueta en el eje y
#Guardar la imagen
# plt.savefig('fft(Varianza).png')
plt.show()









#################################
#########EOF#####################
#################################

plt.figure()
plt.scatter(f, g)
plt.show()


R=np.vstack((f,g))
RT= R.T
matriz_cov=np.dot (R, RT)
e_vals, e_vecs = la.eig(matriz_cov)

plt.figure()
plt.plot(e_vecs[0,:], 'b', label= 'EOF 1')
plt.figure()
plt.plot(e_vecs[1,:], 'r', label= 'EOF 2')
#plt.figure()
#plt.plot(e_vecs[1,:], 'r', label= 'EOF 2')
plt.legend(loc='upper right')
plt.title('Vectores propios')
plt.show()


###varianza explicada
suma_vals=np.sum(e_vals)
var_exp=(e_vals/suma_vals)*100
plt.figure()
plt.plot(var_exp, 'o')


########## componentes principales
cp=np.dot(e_vecs.T,R)
plt.figure()
plt.plot(cp[0]), plt.plot(cp[1])
plt.figure()
plt.contourf(cp)

#plt.plot(cp[:,1])
plt.show()
