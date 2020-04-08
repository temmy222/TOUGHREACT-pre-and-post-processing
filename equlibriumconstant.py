# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 13:32:15 2019

@author: tajayi3
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import griddata
from t2listing import * 
from t2data import *
from math import log10
import numpy as np
import scipy 
import matplotlib as mpl
from t2listing import *
from mpl_toolkits.mplot3d import Axes3D
from scipy import interpolate
from scipy.interpolate import griddata
from prepfortoughreact import *
from mpl_toolkits.axes_grid1 import make_axes_locatable
import re 
from prepfortoughreact import *
from batchreactionplotroutine import *
from flowreactionplotroutine import *
import os
import random
from prepfortoughreact import *
from flowreactionplotroutine import *
from batchreactionplotroutine import *
import pandas as pd
import re
from miscellaneous import *


dest1 = r"D:\Working-folder - Ajayi\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\For paper\GOM Cement flow with batch\Increased depth\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore"
os.chdir(dest1)
filename = 'thddem1214r3_hs.dat'

tre = miscellaneous(dest1,filename)
minerals = ['Gypsum','Ettringite','Friedel_Salt','Calcite','Sepiolite','Tobermorite(11A)','Jennite','Portlandite','Chalcedony','KatoiteSi1','Hydrotalcite','Dolomite']
#minerals = ['Calcite','Portlandite']
gases = ['CO2(g)']
tre.plotGasK('CO2(g)')
tre.plotMineralK('Hydrotalcite')
tre.plotmultipleMineralK(minerals)

rateconstants = {'Gypsum':1.6216e-3,'Ettringite':1.2589e-012,'Friedel_Salt':1.2589e-012,'Calcite':1.5488e-06,'Sepiolite':3.9811e-013,
                 'Tobermorite(11A)':1.0e-012,'Jennite':1.0e-012,'Portlandite':2.18e-08,'Chalcedony':1.6982e-013,
                 'KatoiteSi1':1.2589e-012,'Hydrotalcite':1.2589e-012}

molarvolumes = {'Gypsum':74.6900,'Ettringite':710.3200,'Friedel_Salt':276.2400,'Calcite':36.9300,'Sepiolite':285.5000,
                 'Tobermorite(11A)':286.1900,'Jennite':456.4000,'Portlandite':33.0600,'Chalcedony':22.6900 ,
                 'KatoiteSi1':141.5100,'Hydrotalcite':227.3600,'Dolomite':64.3700}
mine =[]
vale =[]
#for key in molarvolumes:
#    mine.append(key)
#    vale.append(np.log10(rateconstants[key]))
    
for key in molarvolumes:
    mine.append(key)
    vale.append((molarvolumes[key]))
    
fig = plt.figure()
ax = fig.add_subplot(111)
y_pos = np.arange(len(mine))
ax.bar(y_pos, vale, align='center', alpha=0.5)
plt.xticks(y_pos, mine)
plt.ylabel('Log of Rate Constant')
plt.title('Rate Constant for different minerals')
plt.setp(ax.get_xticklabels(), fontsize=10, rotation='vertical')
plt.grid()
fig.savefig('Rate constant' +'.jpg',bbox_inches='tight',dpi=(600)) 
