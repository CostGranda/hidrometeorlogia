# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 23:04:52 2015

@author: Laura Rodríguez
"""
x = [1,2,3,4,5]

y = []
def gaussiana(lst):
    
    for i in lst:
        lst.append((i *(i+1))/2)
    
    return lst 
print (gaussiana(x)) 


 