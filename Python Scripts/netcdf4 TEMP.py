from netCDF4 import Dataset
import matplotlib as plt

import scipy.stats as st

import numpy as np
import datetime as dt  
import numpy as np
from netCDF4 import Dataset  
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap, addcyclic, shiftgrid

#my_example_nc_file = "C:\Users\Don Roge\Downloads\OISST_MonthClim_1982-2011.nc"
#fh = Dataset(my_example_nc_file, mode='r')
#
#print(fh.variables)
# #ver variables en el archivo
#
#sst = fh.variaIbles[u'interpolated_sst'][:] 
## copiar variable 

def reconoce_netcdf(nc_fid):
    #Toma el archivo netcdf y determina sus propieades y variables
    nc_vars=[var for var in nc_fid.variables]
    nc_dims=[dim for dim in nc_fid.dimensions]
    nc_prop=nc_fid.ncattrs()
    return nc_vars,nc_dims,nc_prop

nc_file='OISST_MonthClim_1982-2011.nc'
nc_fid=Dataset(nc_file,'r')
#Reconociendo lo que tiene adentro
nc_vars,nc_dims,nc_prop=reconoce_netcdf(nc_fid)

temp=nc_fid.variables['interpolated_sst'][:]
lat = nc_fid.variables['lat'][:]
lon= nc_fid.variables['lon'][:]

#temp1=temp[11].data ###meses 


#Lectura de propieades principales
lats=nc_fid.variables['lat'][:]
lons=nc_fid.variables['lon'][:]
time=nc_fid.variables['time'][:]
temp=nc_fid.variables['interpolated_sst'][:]



#Juntando todo en un vector (Espacio+Tiempo)

tempi_vect=[]
for k in range(12):
    tempk=temp[k]
    for i in range(300,336): ##longitud
        for j in range(40, 64): ##latitud
            tempi_vect.append(tempk[i][j])

   
#Borrando los datos enmascarados            
tempi_vect2=[]
for i in tempi_vect:
    if i!="masked":
        tempi_vect2.append(i) #Datos que finalmente se van a utilizar de temp

#m= np.mean(tempi_vect2)
#
#
#
## Remueve ciclo anual
#idx_mean = 0
#for idx_values in range (1, tempi_vect2):
##    print idx_values
#     tempi_vect2[idx_values] = tempi_vect2[idx_values] - m
#     tempi_vect2[idx_values] = tempi_vect2[idx_values] * tempi_vect
#     if idx_mean >= 11:
#         idx_mean = 0
#     else:
#         idx_mean = idx_mean + 1


###




##################### AUTOCORRELACIONES DE LA SERIE
np.random.shuffle(tempi_vect2)
#Pearson para la serie
a=[]
for i in range(0,100):
    pe=st.pearsonr(tempi_vect2[i:],tempi_vect2[:len(tempi_vect2)-i])
    a.append(pe)

#Spearman para la serie 
b=[]
for i in range (0,100):
    sp=st.spearmanr(tempi_vect2[i:],tempi_vect2[:len(tempi_vect2)-i])
    b.append(sp)

#a1=np.reshape(a,(10,2))

#usar solo los datos que necesito
g=[]
for i in range(len(a)):
    g.append(a[i][0])

h=[]
for i in range(len(b)):
    h.append(b[i][0])



plt.figure()
plt.plot(g, color="r")
plt.plot(h, color="b")
plt.title("Autocorrelograma serie de datos SST")
plt.xlabel("Rezagos")
plt.ylabel("Correlacion")
plt.show()
plt.legend("Pearson")
plt.savefig('autocorrel_serie')



#####INFORMACIÓN MUTUA
X=np.random.normal(0.0,1.0,size=1000)
Z=np.random.normal(0.0,1.0,size=1000)
B=1.0
C=1.0
K=np.sqrt(B**2.0+C**2.0)

Y=(B*X+C*Z)/K

Bi=20

def mutualinformation (X,Y,bins=Bi):
    pxy,b1,b2=np.histogram2d(X,Y,bins=Bi)
    fx=np.histogram(X, bins=Bi)[0]; fx=fx.astype(float)
    gy=np.histogram(Y, bins=Bi)[0]; gy=gy.astype(float)
    pxy=pxy/pxy.sum();fx=fx/fx.sum()
    gy=gy/gy.sum()    
    val=0
    for posX, i in enumerate (fx):
        for posY, j in enumerate (gy):
            v=pxy[posX,posY]*np.log2(pxy[posX,posY]/(i*j))
            if np.isfinite(v):
                val+=v
    return val
val=mutualinformation(X,Y,Bi)

#SERIE

x1=tempi_vect2
#x1=np.concatenate(x1)
mutual=[]
rez=[]
for i in range (0,20):  
    val=mutualinformation(x1[i:len(x1)],x1[:len(x1)-i],Bi)
    rez.append(i)
    mutual.append(val)

plt. figure()
plt.plot(rez,mutual)
plt.show
#plt.savefig('informacionmutuaserie.png')


