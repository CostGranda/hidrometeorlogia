# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 13:09:40 2015

@author: Laura Rodríguez
"""

from netCDF4 import Dataset
import glob as gl
import os
import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.basemap import Basemap, addcyclic, shiftgrid, 
from mpl_toolkits.basemap import cm



#def reconoce_netcdf(nc_fid):
#    #Toma el archivo netcdf y determina sus propieades y variables
#    nc_vars=[var for var in nc_fid.variables]
#    nc_dims=[dim for dim in nc_fid.dimensions]
#    nc_prop=nc_fid.ncattrs()
#    return nc_vars,nc_dims,nc_prop
#    
#nc_fid=Dataset(nc_file,'r')
##Reconociendo lo que tiene adentro
#nc_vars,nc_dims,nc_prop= reconoce_netcdf(nc_fid)    
    
############################################
##############LEER BASE DE DATOS PARA MMM
############################################

#datos91_95.variables para ver las variables de la base de datos
###latitud caribe: 23,875 grados, 7,875 grados --> 391 , 455
##longitud caribe: 268,625 grados, 299,625 grados --> 1074, 1198

####BASE DE DATOS 1991-1995############

#datos1= '91y95.nc'
#datos91_95= Dataset(datos1)


#lat= datos91_95.variables['lat'][:]
#lon = datos91_95.variables['lon'][:]
#tos = datos91_95.variables['tos'][:]
    
#sst1= tos[:, 389:453, 1074:1198]



#######BASE DE DATOS 1996-2000#########

os.chdir('..')

datos2= '96_00.nc'
datos96_00 = Dataset(datos2, 'r')

tos2=datos96_00.variables['tos'][:, 391:455, 1074:1198]
#sst2= tos2[:, 391:455, 1074:1198]

plt.figure()
plt.contourf(tos2[0,:,:])

lati= datos96_00.variables['lat'][:]
longi = datos96_00.variables['lon'][:]


#Basemap()
#from mpl_toolkits.basemap import Basemap
#import matplotlib.pyplot as plt
## setup Lambert Conformal basemap.
#m = Basemap(width=12000000,height=9000000,projection='lcc',
#            resolution='c',lat_1=45.,lat_2=55,lat_0=50,lon_0=-107.)
## draw coastlines.
#m.drawcoastlines()
## draw a boundary around the map, fill the background.
## this background will end up being the ocean color, since
## the continents will be drawn on top.
#m.drawmapboundary(fill_color='aqua')
## fill continents, set lake color same as ocean color.
#m.fillcontinents(color='coral',lake_color='aqua')
#plt.show()

#######BASE DE DATOS 2001-2005###########

datos3 = '01_05.nc'
datos01_05=Dataset(datos3, 'r')

tos3= datos01_05.variables['tos'][:, 391:455, 1074:1198]
#sst3=tos3[:, 389:453, 1074:1198]

#####BASE DE DATOS 2006- 2010###
datos4 = '06_10.nc'
datos06_10=Dataset(datos4, 'r')

tos4= datos06_10.variables['tos'][:, 391:455, 1074:1198]
#sst4=tos4[:, 389:453, 1074:1198]

####BASE DE DATOS 2011-2014####
datos5 = '11_14.nc'
datos11_14=Dataset(datos5, 'r')

tos5= datos11_14.variables['tos'][:, 391:455, 1074:1198]
#sst5=tos5[:, 389:453, 1074:1198]


#####################pegar las matrices 

primera= np.vstack((tos2,tos3))
segunda= np.vstack((primera,tos4))
tercera=np.vstack((segunda, tos5))

#######################ENMASCARAR

def mask(x,y):
    flot=np.array(x,dtype=float)
    flot[flot==y]=np.nan
    flot=np.ma.array(flot,mask=np.isnan(flot))
    return flot
    
sst=mask(tercera,100000002004087734272.000)
    
#mmm= np.zeros((64,124))
#meses=[]
#maximos=[]
#
#for i in range (0,64):
#    for j in range (0,124):
#        for k in range (0,228,12):
#            for l in range (k, k+12):
#                meses.append(sst[i][j][k])
#            m= np.max(meses)
#            maximos.append(m)
#        mmm[i][j]=np.mean(maximos)
    

#u= sst[0][0][0]

mmm=np.zeros((64,124))

for i in range(0,64):
    for j in range(0,124):
        v=[]
        promedio=[]
        for k in range (0,228):
            v.append(sst[k][i][j])
        grupos=[]
        maximos=[]
        for l in range(0,19):
            anio=[]
            for m in range((12*l),(12*l)+12):
                anio.append(v[m])
            maximos.append(np.max(anio))
            grupos.append(anio)
        mmm[i][j]=np.mean(maximos)
        
mmmcent= np.zeros((64,124))    
mmmcent= mmm - 273.15
    
#######################################
##LEER BASE DE DATOS SST 2013-2014-2015
#######################################

dia= 'sst_b05kmnn_20130312.nc'
dia1 = Dataset(dia, 'r')

lat= dia1.variables['lat'][:]
lon = dia1.variables['lon'][:]
sst1 = dia1.variables['CRW_SST'][:, 1322:1642, 1772:2392]

plt.figure()
plt.contourf(sst1[0][::-1][:])

###latitud caribe: 23,875 grados, 7,875 grados --> 1322, 1642
##longitud caribe: -91,375 grados, -60,375 grados --> 1772, 2392


########################################## DATOS 2013,2014,2015 diarios
#os.chdir('..')

os.chdir('Desktop\datosdiarios')
a = gl.glob('*.nc')

sstdias = np.zeros((971,320,620), dtype=float)
time =[]
for i in range (971):
    nc_file= Dataset(a[i],'r')
    sstdias[i][::-1][:]= nc_file.variables['CRW_SST'][:,1322:1642,1772:2392]
    time.append(nc_file.variables['time'][:])        

    
    
sstdiaria=mask(sstdias,-32768.000) 

plt.figure()
plt.contourf(sstdiaria[0][:][:])
plt.show()

############################################# DATOS 2014
#os.chdir('..')
#os.chdir('datos2014')
#b = gl.glob('*.nc')
#
#sstdiaria14 = np.zeros((len(a),320,620), dtype=float)
#time =[]
#for i in range (len(a)):
#    nc_file= Dataset(b[i],'r')
#    sstdiaria14[i][:][:]= nc_file.variables['CRW_SST'][:,1322:1642,1772:2392]
#    time.append(nc_file.variables['time'][:])   
#
#
#sst2014=mask(sstdiaria14,-32768.000) 
     

##########BAJAR RESOLUCIÓN 


escalada= np.zeros((971,64,124))

    for k in range (971): 
        for h in range (0,64):
            for f in range (0,124):
                ac=0
                for i in range (h*5,5*(h+1)):
                    for j in range(f*5,5*(f+1)):
                        ac += sstdiaria[k][i][j]
                escalada[k][h][f] = ac/25
#        lista_mat.append(escalada)


####RESTA DE MATRICES 

hotspots= np.zeros((971,64,124))

for j in range (0,971):
    for h in range (0,64):
        for f in range (0,124):
            hotspots[j][h][f] = escalada[j][h][f] - mmmcent[h][f]
#            if(hotspots[j][h][f]>=1):
#                print hotspots[j][h][f]
            

####PROMEDIO DE HOTSPOTS



def prom_hot(inicio,fin):
    hot=np.zeros((64,124))
    for i in range (0,64):
        for j in range (0,124):
            ac=0        
            for k in range (inicio,fin):
                ac += hotspots[k][i][j]
            hot[i][j]= ac/(fin-inicio)
    return hot
        
        
#####2013

hot2013=prom_hot(0,295)

#####2014

hot2014=prom_hot(295,660)


#######2015
        
hot2015=prom_hot(660,971)

##################################################

def recorrer(ini,fin):
    m_dhw= np.zeros((64,124))
    for h in range (0,64):
        for f in range (0,124):
            dhw=0
            for j in range (ini,fin):
                if(hotspots[j][h][f]>=1):
                    dhw+=1
            m_dhw[h][f]=dhw
    return m_dhw

trim1= recorrer(0,81)
trim2= recorrer(81,173)
trim3= recorrer(173,264)
trim4= recorrer(264,354)
trim5= recorrer(354,446)
trim6= recorrer(446,538)
trim7= recorrer(538,629)
trim8= recorrer(629,719)
trim9= recorrer(719,811)
trim10= recorrer(811,903)
trim11= recorrer(903,971)


                
                ###-91,375 grados, -60,375 grados
#m = Basemap(projection='stere', resolution='h', area_thresh=625,lat_0=0,lon_0=-50,llcrnrlat=7.875,
#            llcrnrlon=-91.375,urcrnrlat=23.875,urcrnrlon=-60.375)
#
#m.drawcoastlines()
#m.fillcontinents(color='green')
#plt.show()



hot_2013=hot2013[:][:].squeeze()

m= Basemap(projection='lcc', lat_0=0.1,lon_0=-32, llcrnrlat=7.875, llcrnrlon=-91.375,urcrnrlat=23.875,urcrnrlon=-60.375,
           resolution='h', area_thresh= 10)

plt.figure()
m.drawcoastlines()
m.fillcontinents()          
plt.show()

#ny=hot2013.shape[0]
#nx= hot2013.shape[1]
#
#lons, lats = m.makegrid(nx, ny)
#x, y = m(lons, lats)
#clevs = [-3, -2.7, -2.4, -2.1, -1.8, -1.5, -1.2, -0.9, -0.6, -0.3, 0, 0.3, 0.6, 0.9, 1.2]

cs = m.contourf(x,y,hot2013[:][:],clevs)
m.drawparallels(np.arange(m.latmin, m.latmax, 5), labels=[1,0,0,0])
m.drawmeridians(np.arange(m.lonmin, m.lonmax, 10), labels=[0,0,0,1])

m.colorbar(cs, location='bottom', pad='10%')
plt.title("HotSpots 2013")
plt.show()

plt.savefig('hot2013')

####trimestres

plt.figure()
#a=F.add_subplot(141)
#b=F.add_subplot(142)
#c=F.add_subplot(143)
#d=F.add_subplot(144)

m.drawcoastlines()
m.fillcontinents()          
plt.show()

#ny=hot2013.shape[0]
#nx= hot2013.shape[1]
#
#lons, lats = m.makegrid(nx, ny)
#x, y = m(lons, lats)
clevs = [-10, 0, 1, 4, 8, 40]

a = m.contourf(x,y,trim4[:][:],clevs)
#b = m.contourf(x,y,trim5[:][:],clevs)
#c = m.contourf(x,y,trim6[:][:],clevs)
#d = m.contourf(x,y,trim7[:][:],clevs)

m.drawparallels(np.arange(m.latmin, m.latmax, 5), labels=[1,0,0,0])
m.drawmeridians(np.arange(m.lonmin, m.lonmax, 10), labels=[0,0,0,1])

m.colorbar(a, clevs, location='bottom',  pad='10%')


plt.title("Zonas de alerta DEF 2013-2014")
plt.show()

plt.savefig('trim4')



