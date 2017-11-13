# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 21:44:03 2017

@author: larom
"""

from mpl_toolkits.basemap import Basemap
from netCDF4 import Dataset
import matplotlib.pyplot as plt
from openpyxl import load_workbook
from datetime import timedelta, datetime
import numpy as np
from calculos import calcularFecha 

libro = load_workbook('C:\\Users\\larom\\Google Drive\\MAESTRIA RRHH\\HIDROMETEOROLOGIA\\Registros DAPARD\\Ficha de Reporte_Emergencias_2014_Final.xlsx')
hoja = libro.get_sheet_by_name('coordenadas')

def fechas():
    hoja = libro.get_sheet_by_name('fechas')
    seleccion = hoja['A1:B54']
    misda = []
    for linea in seleccion:
        for columna in linea:
            misda.append(str(columna.value))
    
    for i in range(1,len(misda)+1,2):
        anio = misda[i][:4]
        mes = misda[i][4:6]
        dia = misda[i][6:]
        misda[i] = '/'.join((dia, mes, anio))
        
    return misda
    


def coordMunicipios():   
    municipios = {}
    seleccion = hoja['A1:B125']    
    for linea in seleccion:
        (municipio, coordenada) =  linea
        municipios[municipio.value] = coordenada.value.split(', ')
        variable = list(map(float, municipios[municipio.value]))
        variable = list(map(lambda x: x/0.25, variable))
        variable[0] = int(1440 + variable[0])
        variable[1] = int(variable[1] + 200)
        variable[2] = int(1440 + variable[2])
        variable[3] = int(variable[3] + 200)
        municipios[municipio.value] = variable

    return municipios



# Open dataset
dataset = Dataset('http://apdrc.soest.hawaii.edu:80/dods/public_data/satellite_product/TRMM/TRMM_PR/3B42_daily/v7')
#La lat/lon empieza en 0, uno menos del de la tabla de la página.
# Longitud: 77.13W = 1132, 74.63W = 1146, avanzan de a .25
# Latitud: 8.92N = 236, 5,32N  = 222

#matriz = np.zeros((1155,400,1440))
#data = dataset.variables['hqprecipitation'][calcularFecha('1/1/2014'):calcularFecha('1/3/2017'),0:400,0:1440]

tamano = {'size': '16'}


def precipitacion(municipio='San Pedro De Urabá', fecha='21/5/2014'):
    prom = []
    coordenadas = coordMunicipios()
    west = coordenadas[municipio][0]
    south = coordenadas[municipio][1]
    east = coordenadas[municipio][2]
    north = coordenadas[municipio][3]
    print(west,south,east,north)
    final = calcularFecha(fecha)
    inicial = final - 10
    print(final,inicial)
    for dia in range(inicial, final+1):
        datos=dataset.variables['hqprecipitation'][dia,south-1:north+1,west-1:east+1]
        #datos = matriz[dia,south:north,west:east]
        prom.append(datos.mean())
    print(prom)
    fechaIni = datetime.strptime(fecha, '%d/%m/%Y') - timedelta(days=10)
    fecha = datetime.strptime(fecha, '%d/%m/%Y')
    plt.figure(figsize=(10,5))
    plt.title('Precipitación promedio acumulada en {}\n desde {} hasta {}'.format(
            municipio, fechaIni.date(), fecha.date()), tamano)
    plt.xlabel('Días', tamano)
    plt.ylabel('mm', tamano)
    ejex = list(range(11))
    plt.xlim(0,10)
    plt.xticks(ejex,[(fechaIni + timedelta(days=i)).date() for i in range(0,11)])
    plt.gcf().autofmt_xdate()
    plt.plot(ejex,prom, 'o-')
    
   

misda = fechas()
co = 0
for i in range(0,5,2):
    co += 1
    print("VUELTA: {}, MUNICIPIO: {}, FECHA: {}".format(co, misda[i], misda[i+1]))
    precipitacion(misda[i],misda[i+1])


#plt.figure()
#
###6.216667, -75.566667
#m = Basemap(projection='cyl', resolution='h', lat_0=6.216667, lon_0=-75.566667, llcrnrlat=5.38,llcrnrlon=282.745,urcrnrlat=8.88,urcrnrlon=286.245)
#
#m.drawcoastlines()
#m.drawstates()
##m.drawparallels(np.arange(m.latmin, m.latmax, 0.5), labels=[1,0,0,0])
##m.drawmeridians(np.arange(m.lonmin, m.lonmax, 0.5), labels=[0,0,0,1])
#
#ny = data.shape[0]; nx = data.shape[1]
#lons, lats = m.makegrid(nx, ny)
#x, y = m(lons, lats)
#
#cs = m.contourf(x,y,data, cmap = plt.get_cmap('RdYlGn_r'))
#cbar = m.colorbar(cs,location='bottom', pad='5%')
#cbar.set_label('mm')
#plt.title('Precipitación')
##plt.savefig('C:\\Users\\larom\\Documents\\GitHub\\hidrometeorlogia\\hola.png')
#plt.show()

