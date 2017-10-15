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

# Contours ssh for specified time and space
# Find the index for date Oct 3, 2004.
date = datetime(2004,10,3,0)
# Open dataset
dataset = Dataset('http://apdrc.soest.hawaii.edu:80/dods/public_data/satellite_product/TRMM/TRMM_PR/3B42_daily/v7')
timevar = dataset.variables['time']
timeindex = date2index(date,timevar) # find time index for desired date.
# Read lats and lons (representing centers of grid boxes).
lats = dataset.variables['lat'][:]
lons = dataset.variables['lon'][:]
# Find the indexes for 165W-153W, 18N-24N
lat_bnds = [ 18 , 24 ]
lon_bnds = [ -165+360 , -154+360 ]
lat_inds = np.where((lats >= lat_bnds[0]) & (lats <= lat_bnds[1]))[0]
lon_inds = np.where((lons >= lon_bnds[0]) & (lons <= lon_bnds[1]))[0]
# Load the NLOM sea surface height from the above information
ssh = dataset.variables['ssh'][timeindex,lat_inds,lon_inds].squeeze()
# Create figure, axes instances.
fig = plt.figure()
ax = fig.add_axes([0.05,0.05,0.9,0.9])
# Create Basemap instance.
m = Basemap(llcrnrlon=-165.,llcrnrlat=18.,urcrnrlon=-154.,urcrnrlat=24.,projection='mill')
# Plot land outlines
m.drawcoastlines()
# Use subset of lats and lons
sublons, sublats = np.meshgrid(lons[lon_inds]-360,lats[lat_inds])
# Contour sea surface height
im1 = m.contourf(sublons, sublats, ssh, latlon=True)
cb = m.colorbar(im1,"bottom", size="5%", pad="2%")
ax.set_title('NLOM 1/16 degree Sea Surface Height [cm] October 3, 2004')
plt.show()