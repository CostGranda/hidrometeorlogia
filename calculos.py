# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 16:54:30 2017

@author: larom
"""
from datetime import date

def calcularFecha(fecha):
    """Recibe la fecha en formato d/m/y"""
    FECHA_MAX = date(2017,6,29)
    FECHA_MIN = date(1998,1,1)
    fecha_str = fecha.split('/')
    fecha_int = list(map(int, fecha_str))
    dias = date(fecha_int[2],fecha_int[1],fecha_int[0])-FECHA_MIN
    return dias.days
