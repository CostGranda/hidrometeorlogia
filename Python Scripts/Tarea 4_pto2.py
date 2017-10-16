# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 15:36:31 2015

@author: laura
"""

import datetime as dt  
import numpy as np
from netCDF4 import Dataset  
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap, addcyclic, shiftgrid

#Funciones que se van a utilizar
def reconoce_netcdf(nc_fid):
    #Toma el archivo netcdf y determina sus propieades y variables
    nc_vars=[var for var in nc_fid.variables]
    nc_dims=[dim for dim in nc_fid.dimensions]
    nc_prop=nc_fid.ncattrs()
    return nc_vars,nc_dims,nc_prop
def plot_variable(var,capa,lats,lons,ruta=None,levels=None):
	fig = plt.figure(facecolor='w',edgecolor='w')
	fig.subplots_adjust(left=0., right=1., bottom=0., top=0.9) #margenes del plot
	m = Basemap(projection='merc', llcrnrlat=-70, urcrnrlat=70,llcrnrlon=-180, urcrnrlon=180, resolution='c',lat_ts=20) #lon_0=0) #Propieades del plot como mapa
	m.drawcoastlines() #Dibuja las costas
	m.drawmapboundary() #Dibuja los limites
	# Hace que el plot sea continuo
	vel_cyclic, lons_cyclic = addcyclic(var[0,capa,:,:], lons)
	# Pone al grid entre 180 y -180
	vel_cyclic, lons_cyclic = shiftgrid(180., vel_cyclic, lons_cyclic, start=False)
	# Crea vectores de lat y lon para Basemap
	lon2d, lat2d = np.meshgrid(lons_cyclic, lats)
	# Transforms lat/lon into plotting coordinates for projection
	x, y = m(lon2d, lat2d)
	# Ploteamos la velocidad del viento con 15 intervalos de colores
	cs = m.contourf(x, y, vel_cyclic, 
		12, 
		cmap=plt.cm.Spectral_r,
		vmin=-25,vmax=75,
		levels=levels)
	#Orientacion de la barra de colores y nombre
	cbar = plt.colorbar(cs, orientation='horizontal', shrink=0.5)
	cbar.set_label("[%s]" % (nc_fid.variables['ua'].units))	
	if ruta==None:
		plt.show()
	else:
		plt.savefig(ruta,bbox_inches='tight')
	return cs.levels
 
#lectura del archivo netcdf Temperatura
nc_file='/home/laura/Analisis_datos/temp_aire/cru_tmp_clim_1991-2000.nc'
nc_fid=Dataset(nc_file,'r')
#Reconociendo lo que tiene adentro
nc_vars,nc_dims,nc_prop=reconoce_netcdf(nc_fid)

#Lectura de propieades principales
lats=nc_fid.variables['latitude'][:]
lons=nc_fid.variables['longitude'][:]
time=nc_fid.variables['time'][:]
temp=nc_fid.variables['tmp'][:]

#Juntando todo en un vector (Espacio+Tiempo)

tempi_vect=[]
for k in range(12):
    tempk=temp[k]
    for i in range(200,230):
        for j in range(169,210):
            tempi_vect.append(tempk[i][j])
        


#lectura del archivo netcdf Cobertura de nubes
nc_file='/home/laura/Analisis_datos/temp_aire/cru_cld_clim_1991-2000.nc'
nc_fid2=Dataset(nc_file,'r')
#Reconociendo lo que tiene adentro
nc_vars2,nc_dims2,nc_prop2=reconoce_netcdf(nc_fid2)

#Lectura de propieades principales
lats2=nc_fid2.variables['latitude'][:]
lons2=nc_fid2.variables['longitude'][:]
time2=nc_fid2.variables['time'][:]
cloud=nc_fid2.variables['cld'][:]

#Juntando todo en un vector (Espacio+Tiempo)
cloudi_vect=[]
for k in range(12):
    cloudk=cloud[k]
    for i in range(200,230):
        for j in range(169,210):
            cloudi_vect.append(cloudk[i][j])
            
#Borrando los datos enmascarados            
tempi_vect2=[]
for i in tempi_vect:
    if i!="masked":
        tempi_vect2.append(i) #Datos que finalmente se van a utilizar de temp

cloudi_vect2=[]
for i in cloudi_vect:
    if i!="masked":
        cloudi_vect2.append(i)#Datos que finalmente se van a utilizar de cloud
          


plt.figure("Histograma conjunto")
plt.xlabel("temperatura")
plt.ylabel("Porcentaje nubosidad")
Matconj,fx,fy,plot=plt.hist2d(tempi_vect2,cloudi_vect2,bins=50)
plt.figure("Temperatura")
fx,temp,p=plt.hist(tempi_vect2,bins=50)
plt.figure("Nubosidad")
fy,cloud,p1=plt.hist(cloudi_vect2,bins=50)
fdpx=fx/len(tempi_vect2)
fdpy=fy/len(cloudi_vect2)

indep=np.zeros((50,50)) #histograma independiente
for i in range(50):
    for j in range(50):
        indep[i][j]=fdpx[i]*fdpy[j]

plt.figure("Independiente")
plt.imshow(indep)    

#informacion mutua
Matconj2=Matconj/len(tempi_vect2)

vectorI=[]
for i in range(50):
    for j in range(50):
        I=Matconj2[i][j]*np.log2(Matconj2[i][j]/indep[i][j])
        vectorI.append(I)

IM=np.nansum(vectorI)

    
IM_rezag=[]
#Informacion mutua con rezagos
n=len(tempi_vect2)        
cloud_r=[] #valores rezagados
rezago=1
temperatura_corto=tempi_vect2
#up=len(temp)-1 #Ultima posicion
for k in range(10):#numero rezagos
    for j in range(rezago,n):
        cloud_r.append(cloudi_vect2[j])
        
   
    temperatura_corto=temperatura_corto[0:-1]
   
    Matconjr,fx,fy,plot=plt.hist2d(temperatura_corto,cloud_r,bins=50)
    fx,temp,p=plt.hist(temperatura_corto,bins=50)
    fy,clouddata,p1=plt.hist(cloud_r,bins=50)
    fdpx=fx/len(temperatura_corto)
    fdpy=fy/len(cloud_r)
    
    indep_r=np.zeros((50,50)) #histograma independiente
    for i in range(50):
        for j in range(50):
            indep_r[i][j]=fdpx[i]*fdpy[j]
    
    #informacion mutua
    Matconj2_r=Matconjr/len(temp)
    vectori=[]
    for i in range(50):
        for j in range(50):
            I=Matconj2_r[i][j]*np.log2(Matconj2_r[i][j]/indep_r[i][j])
            vectori.append(I)
            IM=np.nansum(vectorI)
    IM_rezag.append(IM)
     
    
    cloud_r=[]
    rezago+=1
#    up-=1   



#plt.figure("Informacion mutua")
#plt.plot(t, vectorI)
#plt.title("Informacion Mutua")
#plt.xlabel("C")
#plt.ylabel("IM")
