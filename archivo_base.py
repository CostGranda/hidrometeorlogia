# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 21:44:03 2017

@author: larom
"""

from mpl_toolkits.basemap import Basemap
from netCDF4 import Dataset, date2index
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


# Open dataset
dataset = Dataset('http://apdrc.soest.hawaii.edu:80/dods/public_data/satellite_product/TRMM/TRMM_PR/3B42_daily/v7')

data = dataset.variables['precipitation'][7119,21:37,1130:1147]

#6.216667, -75.566667
m = Basemap(projection='lcc', resolution='h',lat_0=0.1, lon_0=-32,llcrnrlat=5.375,llcrnrlon=282.625,urcrnrlat=9.125,urcrnrlon=286.625, area_thresh=10)

m.drawcoastlines()
m.drawstates()
m.drawparallels(np.arange(m.latmin, m.latmax, 0.5), labels=[1,0,0,0])
m.drawmeridians(np.arange(m.lonmin, m.lonmax, 0.5), labels=[0,0,0,1])


ny = data.shape[0]; nx = data.shape[1]
lons, lats = m.makegrid(nx, ny)
x, y = m(lons, lats)
clevs = [0,3,6,9,12,15,18,21,24,27,30]
cs = m.contourf(x,y,data)
cbar = m.colorbar(cs,location='bottom', pad='20%')
cbar.set_label('mm')
plt.show()