# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 16:54:30 2017

@author: larom
"""
from datetime import date

def calcularFecha(fecha='29/6/2017'):
    """
    Recibe la fecha en formato 'd/m/y' y le resta la fecha mínima (1/1/1998) de los datos.
    Si se llama sin argumentos toma por defecto la última fecha permitida.
    Retorna el día de tipo entero.
    """
    FECHA_MIN = date(1998,1,1)
    # Al hacer el split los elementos son de tipo string
    fecha_str = fecha.split('/')
    # Convierte a enteros todos los elementos de la lista
    fecha_int = list(map(int, fecha_str)) 
    # Se envián en orden año, mes y día
    dias = date(fecha_int[2], fecha_int[1], fecha_int[0]) - FECHA_MIN
    return dias.days
