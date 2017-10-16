# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 12:21:25 2015

@author: Laura Rodríguez
"""

import numpy
print ("hola mundo")

lista = ["ana", 2, 2, 1, "juan"]
print(lista[0][1])

a = "juan"
b = "carolina"
print (a+b)

a = 2
b = 3
print (a/b)

lista.append("mundo") #anexa "mundo" al final de la lista
print (lista)

lista.remove("ana")
print (lista)
lista.remove(lista[3])
print(lista)


if lista[1] <= 2: 
    lista.append("tenemos un dos")
else:
    lista.append("no tenemos un dos")

    
print(lista)



#for i in range(5):
    #print(i)
    #print(lista[i])


#x=2
#while x<=100:
    #x=x+1
    #print (x)
    
    
c = numpy.arange(1,5,2)
c1 = range(5)


#variables ->  loops (iteraciones), condicionales, operadores matemáticos 
#tipos de variables: enteras (10), flotantes(10.1), complejas(10i), caracteres('hola'), lógicas(false,true, banderas)
#numpy incluye vectores(arrays) 
#matplotlib, 
#pylab-> versión resumida de matplotlib 
#A[-1] es la última entrada






