
# coding: utf-8

# In[19]:

import matplotlib.pyplot as plt
import random as r
# para no abrir ventana con la gráfica
get_ipython().magic('matplotlib inline')


# In[138]:

def LCG(seed, n, a=1664525, c=1013904223, m=2**16):
    numbers = []
    for i in range(n):
        seed = (a * seed + c) % m
        numbers.append(seed/m)

    return (numbers)


# In[140]:

u = LCG(5, 100) #asigno a u la lista de números aleatorios uniformes 

plt.figure()
plt.hist(u)

plt.show()


# In[141]:

# n = Cantidad de numeros
# semilla = valor inicial y no se incluye en la lista generada

def LCG(semilla, n, a=5, b=7, c=16):
    numbers = []
    for i in range(n):
        semilla = (a * semilla + b) % c
        numbers.append(semilla/c)

    return numbers

#se llama a la funcion con 1 de semilla y que genere 10 numeros
LCG(2, 10)


# In[143]:

g = []
num = 10000
for i in range(num):
    g.append(r.gauss(0,1))
#10000 iteraciones = 10000 números aleatorios gaussianos con media=0 y desviaciín estandar=1


# In[144]:

plt.hist(g)

plt.show()


# In[ ]:



