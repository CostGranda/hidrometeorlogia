# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:15:46 2015

@author: Laura Rodríguez
"""

import random as rnd

lista = []

for i in range(3):
    x = []
    for j in range(4):
        x.append(rnd.randint(1,10))
    lista.append(x)

print(lista)

y = []

for i in range(5):
    x = []
    for j in range(1):
        x.append(r.randint(1,6))
    y.append(x)