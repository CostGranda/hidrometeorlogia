import datetime
import numpy as np
import matplotlib
matplotlib.use ("template")
import matplotlib.pyplot as plt
plt.ioff ()
from scipy import linalg as la

from netCDF4 import Dataset

# Lectura de Datos
sst_filename = 'sst.mnmean.nc'
nc_obj = Dataset(sst_filename, 'r')

sstmean_filename = 'sst.ltm.1971-2000.nc'
ncmean_obj = Dataset(sstmean_filename, 'r')

mask_filename = 'lsmask.nc'
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
for idx_values in range (1, sst_values.shape[0]):
#    print idx_values
     sst_values[idx_values] = sst_values[idx_values] - sst_mean_values[idx_mean]
     sst_values[idx_values] = sst_values[idx_values] * mask_values
     if idx_mean >= 11:
         idx_mean = 0
     else:
         idx_mean = idx_mean + 1


# Quita el primer registro porque se omitio en el calculo
sst_values = np.array (sst_values[1:])
print sst_values.shape

# Grafica sst_values
plt.close ('all')
plt.imshow (sst_values[0])
plt.savefig ("sst_values.png")

# Calcula EOF
#sst_values_tropico = np.zeros ((sst_values.shape[0], lat_mean_values[np.abs (lat_mean_values) <= 30].shape[0], lon_mean_values[(lon_mean_values >= 120) & (lon_mean_values <= 290)].shape[0]))
sst_values_tropico = np.zeros ((sst_values.shape[0], lat_mean_values[np.abs (lat_mean_values) <= 30].shape[0], lon_mean_values[(lon_mean_values >= 150) & (lon_mean_values <= 280)].shape[0]))
print sst_values_tropico.shape
for idx_values in range (0, sst_values.shape[0]):
#    print idx_values
    aux_x1 = sst_values[idx_values,np.abs (lat_mean_values) <= 30,:]
#    print aux_x1.shape
#    aux_x1 = aux_x1[:,(lon_mean_values >= 120) & (lon_mean_values <= 290)]
    aux_x1 = aux_x1[:,(lon_mean_values >= 150) & (lon_mean_values <= 280)]
#    print aux_x1.shape
#    print sst_values[0,0,0]
#    sst_values_tropico[idx_values] = np.array (sst_values[idx_values][np.abs (lat_mean_values) < 30][(lon_mean_values >= 150) & (lon_mean_values <= 240)])
#    sst_values_tropico[idx_values] = np.array (sst_values[idx_values,np.abs (lat_mean_values) < 30,(lon_mean_values >= 150) & (lon_mean_values <= 240)])
    sst_values_tropico[idx_values] = aux_x1

print sst_values_tropico.shape

plt.close ('all')
plt.imshow (sst_values_tropico[0])
plt.savefig ("sst_values_tropico.png")

# Reshape de los datos
sst_values_tropico_reshape = sst_values_tropico.reshape (sst_values_tropico.shape[0], sst_values_tropico.shape[1] * sst_values_tropico.shape[2])
print sst_values_tropico_reshape.shape

#sst_values_tropico = np.zeros ((2,2,2))
#sst_values_tropico_reshape = np.array ([[2,4,-6,8],[1,2,-3,4]])
#sst_values_tropico_reshape = np.array ([[np.nan,4,np.nan,8],[np.nan,2,np.nan,4]])

#mascaraNaN = np.ma.array (sst_values_tropico_reshape, mask = (np.isnan (sst_values_tropico_reshape)))
#sst_values_tropico_reshape_nonan

print sst_values_tropico_reshape

idx_nan_array = np.where (np.isnan (sst_values_tropico_reshape[0]))
sst_values_tropico_reshape_nonan = np.delete (sst_values_tropico_reshape, idx_nan_array, 1)

print sst_values_tropico_reshape_nonan

# Matriz de Covarianza
#matriz_cov_1 = np.dot (sst_values_tropico_reshape.T, sst_values_tropico_reshape) 
#matriz_cov_2 = np.dot (sst_values_tropico_reshape, sst_values_tropico_reshape.T)
matriz_cov_1 = np.dot (sst_values_tropico_reshape_nonan.T, sst_values_tropico_reshape_nonan) 
print matriz_cov_1.shape
matriz_cov_2 = np.dot (sst_values_tropico_reshape_nonan, sst_values_tropico_reshape_nonan.T)
print matriz_cov_2.shape

print matriz_cov_1
print matriz_cov_2
#print aaa.aaa ()

matriz_cov = matriz_cov_1
#print matriz_cov

#indicesData = sst_values_tropico_reshape[]

# Valores y Vectores Propios (Componentes Principales son los e_vecs)
e_vals, e_vecs = la.eig (matriz_cov)
#e_vals, e_vecs = la.eig (matriz_cov_no_nan)
print aaa.aaa ()

print e_vals
print e_vecs * -1

# Varianza Explicada
sum_evals = np.sum (e_vals)
var_exp = (e_vals / sum_evals) * 100
print var_exp

# Grafica Varianza Explicada
plt.close ('all')
plt.plot (var_exp[0:10])
plt.savefig ("var_exp.png")

# EOF
#pc_mat = np.dot (e_vecs.T, sst_values_tropico_reshape)
pc_mat = np.dot (e_vecs.T, sst_values_tropico_reshape_nonan)

pc_mat

print pc_mat
print pc_mat.shape
#pc_mat_reshape1 = pc_mat.reshape (sst_values_tropico.shape[0], sst_values_tropico_reshape_nonan.shape[1], sst_values_tropico_reshape_nonan.shape[2])
#print pc_mat_reshape1.shape

for idx_add in idx_nan_array[0]:
    print "idx_add"
    print idx_add
    pc_mat = np.insert (pc_mat, idx_add, np.array ([np.NaN] * pc_mat.shape[0]), 1)

print sst_values_tropico_reshape_nonan.shape
print sst_values_tropico_reshape.shape
print pc_mat.shape 

# Reshape de los eof para graficacion
#pc_mat = pc_mat.reshape (sst_values_tropico.shape[0], sst_values_tropico.shape[1], sst_values_tropico.shape[2])
pc_mat = pc_mat.reshape (sst_values_tropico.shape[0], sst_values_tropico.shape[1], sst_values_tropico.shape[2])
print pc_mat.shape

plt.close ('all')
imshow_result = plt.imshow (pc_mat[1], vmin = -15, vmax = 15)
plt.savefig ("pc_mat.png")


