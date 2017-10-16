# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 22:24:19 2015

@author: Don Roge
"""

import datetime
import numpy as np
import matplotlib
matplotlib.use ("template")
import matplotlib.pyplot as plt
plt.ioff ()
from scipy import linalg as la
 
from netCDF4 import Dataset
 
# Lectura de Datos
sst_filename = "C:\Users\Don Roge\Downloads\sst.mnmean.nc"
nc_obj = Dataset(sst_filename, 'r')
 
sstmean_filename = "C:\Users\Don Roge\Downloads\sst.ltm.1971-2000.nc"
ncmean_obj = Dataset(sstmean_filename, 'r')
 
mask_filename = "C:\Users\Don Roge\Downloads\lsmask.nc"
masknc_obj = Dataset(mask_filename, 'r')
 
print masknc_obj.variables
mask_values = np.array (masknc_obj.variables["mask"])
mask_values = mask_values.reshape ((mask_values.shape[1], mask_values.shape[2]))
mask_values = mask_values.astype (dtype = np.float)
mask_values[mask_values == 0.0] = np.NaN
print mask_values.shape
print mask_values
 
plt.close ('all')
plt.imshow (mask_values)
plt.savefig ("mascara.png")
 
#print nc_obj.variables
#print ncmean_obj.variables
 
sst_values = np.array (nc_obj.variables['sst'][:])
print sst_values.shape
 
sst_dates = np.array (nc_obj.variables['time'][:])
#print sst_dates
 
sst_mean_values = np.array (ncmean_obj.variables['sst'][:])
lat_mean_values = np.array (ncmean_obj.variables['lat'][:])
lon_mean_values = np.array (ncmean_obj.variables['lon'][:])
 
#print np.max (lat_mean_values)
#print np.max (lon_mean_values)
#print np.min (lat_mean_values)
#print np.min (lon_mean_values)
 
#print np.max (sst_mean_values)
#print np.min (sst_mean_values)
 
print sst_mean_values.shape
 
# Remueve ciclo anual
idx_mean = 0
for i in range (1, sst_values.shape[0]):
    sst_values[i] = sst_values[i] - sst_mean_values[idx_mean]
    sst_values[i] = sst_values[i] * mask_values
    if idx_mean >= 11:
        idx_mean = 0
    else:
        idx_mean = idx_mean + 1
sst_values = np.array (sst_values[1:])
         
# Quita el primer registro porque se omitio en el calculo
sst_values = np.array (sst_values[1:])
print sst_values.shape

vect=[]
for k in range(12):
    tempk=sst_values[k]
    for i in range(73,79): #lONGITUDES
        for j in range(125,285): #LATITUDES
            vect.append(tempk[i][j])

vect2=[]
for i in vect:
    if i!="masked":
        vect2.append(i) 
 
# Grafica sst_values
#plt.close ('all')
#plt.imshow (sst_values[0])
#plt.savefig ("sst_values.png")



