# -*- coding: utf-8 -*-
"""
Created on Wed Oct 07 00:16:11 2015

@author: Laura Rodríguez
"""



import numpy as np
import pandas as pnd
import scipy.stats as st


campoviento= "202_Vientos_2013.txt"
x=np.loadtxt(campoviento, dtype="string")
o=x[:,2]
y=x[:,3]
z=x[:,4]
o = np.float64(o)

start = pnd.datetime(2013, 07, 11, 13, 26) 
end = pnd.datetime(2013, 12, 31, 23, 59)
rng = pnd.date_range(start, end, freq="min")

tss=pnd.DataFrame(data={"velocidad": o }, index=rng, dtype=float)

tss= tss[tss!=-999.0]
mediahoraria=tss["velocidad"].resample("H", how="mean") 

has=0
des=0
nor=np.zeros(len(mediahoraria))
index=[]
for r in range(24):
    has+=len(mediahoraria.at_time(str(r)+":00:00"))
    cd=mediahoraria.at_time(str(r)+":00:00")
    nor[des:has]=(cd-cd.mean())/cd.std()
    index.extend(cd.index.tolist())
    des=has
tss2=pnd.DataFrame(nor,index=index,columns=['velocidad']).sort_index() 
tss2=tss2.dropna()


#pearson=[]
#spearman=[]
#
#for i in range (0,100):
#    pearson.append(scipy.stats.mstats.pearsonr(tss2[i:], tss2[:len(tss2)-i])[0])
#    spearman.append(scipy.stats.spearmanr(tss2[i:], tss2[:len(tss2)-i])[0])
#
#plt.ylabel("Coeficiente de correlacion")
#plt.xlabel("Rezagos (horas)")
#plt.plot(pearson, color="red"); #mela
#plt.plot(spearman, color="blue")
#red_patch = mpatches.Patch(color='red', label='Pearson')
#plt.legend(handles=[red_patch])
#blue_patch = mpatches.Patch(color='blue', label='Spearman')
#plt.legend(handles=[red_patch, blue_patch])
#plt.show()