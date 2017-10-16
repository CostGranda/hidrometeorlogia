# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 14:37:39 2015

@author: Laura Rodríguez
"""

import random as rnd

datos = open("vlr.txt", "r")
#print(datos)
listadatos= []

for linea in datos:
    linea = linea[:-1] #desde el prinvipio hasta una menos para que no salga /n
    listadatos.append(float(linea)) #los convirte a reales para oder operar 


ndatos=len(listadatos)

#print(type(ndatos))
#print(listadatos)

boot= [] #lista bootstrapping
listaboot=[] #donde van a ir cada bootstrap

for k in range(10):
    for i in range(ndatos):
        pos_ale = rnd.randint(0,ndatos-1)
        boot.append(listadatos[pos_ale])
    listaboot.append(boot)
    
print("\nLISTA DE BOOTS\n")
print(listaboot)