# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 08:21:14 2013

@author: cmcuervol®
"""



import numpy as np
import matplotlib.pyplot as plt

dt=0.1
t=np.arange(0,30,dt)

A1 = 3; A2 = 2
w1 = 3; w2 = 5

f = A1*np.sin(w1*t)+A2*np.cos(w2*t)

##gráfica de la función
plt.figure()
plt.plot(t, f, 'r-', linewidth = 2, label = u'f=$%ssin(%st)+%scos(%st)$' %(A1,w1,A2,w2))  # Dibujamos los valores de las parejas ordenadas con una línea contínua
# plt.title('f=3*sin(3*t)+2*cos(5*t)' )  # Colocamos el título del gráfico
plt.xlabel(u'tiempo [s]')  # Colocamos la etiqueta en el eje x
plt.ylabel(u'función evaluada')  # Colocamos la etiqueta en el eje y
plt.legend(loc='best')
#Guardar la imagen
# plt.savefig('f(t).png')
plt.show()

#========================
#transformada de Fourier
#========================
A=np.fft.fft(f)
fr=np.fft.fftfreq(len(t),dt)
print A
print fr


amplitud=np.abs(A)
potencia=np.abs(A)**2
total=np.sum(potencia)
var=potencia*100/total


print var
print potencia
print amplitud

###gráfica de la frecuencia vs amplitud
plt.figure()
plt.plot(fr[:len(t)/2-1], amplitud[:len(t)/2-1], 'g-', linewidth = 2, label = u'Amplitud positiva')  # Dibujamos los valores de las parejas ordenadas con una línea contínua
plt.plot(fr[len(t)/2:], amplitud[len(t)/2:], 'b-', linewidth = 2, label = u'Amplitud negativa')
plt.title('Amplitud de la fft' )  # Colocamos el título del gráfico
plt.xlabel(u'frecuencia [Hz]')  # Colocamos la etiqueta en el eje x
plt.ylabel('Amplitud')  # Colocamos la etiqueta en el eje y
plt.legend(loc='best')
#Guardar la imagen
# plt.savefig('fft(Amplitud).png')
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




#=============================
#filtrado de la función
#=============================

for i in range(len(fr)):
    if abs(fr[i])>0.67:
        A[i]=0
a_fil=np.abs(A)

# gráfica del esprectro filtrado
plt.figure()
plt.plot(fr[:len(t)/2-1], a_fil[:len(t)/2-1], 'g-', linewidth = 2, label = u'Amplitud real')  # Dibujamos los valores de las parejas ordenadas con una línea contínua
plt.plot(fr[len(t)/2:], a_fil[len(t)/2:], 'b-', linewidth = 2, label = u'Amplitud negativa')
plt.title('Amplitud de la fft filtrada' )  # Colocamos el título del gráfico
plt.xlabel(u'frecuencia [Hz]')  # Colocamos la etiqueta en el eje x
plt.ylabel('Amplitud')  # Colocamos la etiqueta en el eje y
plt.legend(loc='best')
#Guardar la imagen
# plt.savefig('fft(Amp_filt).png')
plt.show()

#================================
#transformada inversa de Fourier
#================================

fteo= A1*np.sin(w1*t)
ff=np.fft.ifft(A)

print len(ff)
print len(t)
print ff

##gráfica de las funciones
plt.figure()
plt.plot(t, f, 'r-', linewidth = 2, label = u'f=$%ssin(%st)+%scos(%st)$' %(A1,w1,A2,w2))  # Dibujamos los valores de las parejas ordenadas con una línea contínua
plt.plot(t, ff.real, 'b-', linewidth = 2, label = u'Función filtrada $f=3sin(3t)$')
plt.plot(t, fteo, 'g-', linewidth = 2, label = u'Función teorica f=$%ssin(%st)' %(A1,w1))
# plt.title('f=3*sin(3*t)+2*cos(5*t) y función filtrada' )  # Colocamos el título del gráfico
plt.xlabel(u'tiempo [s]')  # Colocamos la etiqueta en el eje x
plt.ylabel(u'función evaluada')  # Colocamos la etiqueta en el eje y
plt.legend(loc='best')
#Guardar la imagen
# plt.savefig('f(t_filt).png')
plt.show()



