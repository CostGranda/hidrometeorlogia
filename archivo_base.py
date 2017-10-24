# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 21:44:03 2017

@author: larom
"""

from mpl_toolkits.basemap import Basemap
from netCDF4 import Dataset
import matplotlib.pyplot as plt
from calculos import calcularFecha

# Open dataset
dataset = Dataset('http://apdrc.soest.hawaii.edu:80/dods/public_data/satellite_product/TRMM/TRMM_PR/3B42_daily/v7')
#La lat/lon empieza en 0, uno menos del de la tabla.
# Longitud: 77.13W = 1132, 74.13W = 1144, avanzan de a .25
# Latitud: 8.92N = 236, 5,32N  = 222
data = dataset.variables['precipitation'][calcularFecha('29/6/2017'),221:236,1131:1144]

plt.figure(figsize=(10,10))
#6.216667, -75.566667
m = Basemap(projection='lcc', resolution='h',epsg=3115,llcrnrlat=5.375,llcrnrlon=282.625,urcrnrlat=8.92,urcrnrlon=286.625)

m.drawcoastlines()
m.drawstates()
#m.drawparallels(np.arange(m.latmin, m.latmax, 0.5), labels=[1,0,0,0])
#m.drawmeridians(np.arange(m.lonmin, m.lonmax, 0.5), labels=[0,0,0,1])

ny = data.shape[0]; nx = data.shape[1]
lons, lats = m.makegrid(nx, ny)
x, y = m(lons, lats)

cs = m.contourf(x,y,data,7,cmap = plt.get_cmap('spectral'))
cbar = m.colorbar(cs,location='bottom', pad='20%')
cbar.set_label('mm')
plt.title('Precipitation')
plt.savefig('C:\\Users\\larom\\Documents\\GitHub\\hidrometeorlogia\\hola.png')
plt.show()
