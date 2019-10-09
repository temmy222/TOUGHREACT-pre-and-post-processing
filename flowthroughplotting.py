# -*- coding: utf-8 -*-
"""
Created on Wed May 22 11:55:04 2019

@author: tajayi3
"""

"""
copy files back to PYTOUGH folder for result treatments
"""

from t2data import *
from t2incons import *
from toughtotreact import *
from t2listing import * 
import os
import subprocess
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import griddata
from t2listing import * 
from t2data import *
from math import log10
import numpy as np
import scipy 
import matplotlib.pyplot as plt
from t2listing import *
from mpl_toolkits.mplot3d import Axes3D
from scipy import interpolate
from scipy.interpolate import griddata
from prepfortoughreact import *
from flowreactionplotroutine import *
from batchreactionplotroutine import *

dest = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\For paper\Gulf of Mexico Sandstone Cement Flow - Onshore"
dest2 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Geometry Change\Gulf of Mexico Sandstone Cement Flow - Onshore - longer batch"

loc = r"C:\Users\tajayi3\Desktop\Research\Software\PyTOUGH-master"

#
#loca =[loca9,loca10,loca11,loca12]

#labels =['Shale Cement Flow - Onshore','Shale Cement Flow - Offshore','Sandstone Cement Flow - Onshore','Sandstone Cement Flow - Offshore' ]

file_name = "kdd_conc.tec"
file_name2 = "MESH"
lookup = 'CONNE'
myList = ["kdd_conc.tec", "kdd_gas.tec", "kdd_min.tec", "kdd_tim.tec", "MESH","geom2.dat","INFILE"]
#myList = ["hpip_conc.tec", "hpip_gas.tec", "hpip_min.tec", "hpip_tim.tec", "MESH"]
tre1 = prepfortoughreact(dest2,loc,myList,lookup)
tre1.copyallfiles()
tre1.writetofile()


"""
Graph Plotting
"""
with open('test.txt') as f:
    br3 = f.read().splitlines()

#tre = toughreact_tecplot('kdd_concvtk.tec',br3)

gridblock = br3[0]
filenamegrid = 'geom2.dat'



# write to vtk for viewing with Paraview

#geo = mulgrid().read(filenamegrid)
#filenamevtk = 'more minerals.pvd'
#trem = toughreact_tecplot(myList[2],br3)
#trem.write_vtk(geo, filenamevtk)


width = 10
height = 6

parameters = ['pH','t_cl-','t_na+','t_mg+2','t_so4-2','t_hco3-']
paramflow = ['pH','t_cl-','t_mg+2']
plotconc = flowreactionplotroutine(myList[0],br3,paramflow,dest)
plotconcbatch = batchreactionplotroutine(myList[0],br3,parameters,dest)


param2 = ['friedel_salt','Porosity','brucite','portlandite','calcite','jennite']
param2flow = ['Porosity','brucite','portlandite']
plotmin = flowreactionplotroutine(myList[2],br3,param2flow,dest)
plotminbatch = batchreactionplotroutine(myList[2],br3,param2,dest)


paramgas = ['SatGas','RH','co2(g)']
plotgas = flowreactionplotroutine(myList[1],br3,paramgas,dest)
plotgasbatch = batchreactionplotroutine(myList[1],br3,paramgas,dest)


plotconc.threeinone(width,height,br3)
masa,lst = plotconc.retrievedatadistance('X',25)
plotmin.plotsingle('X',25)
plotconc.plotsingle('X',25)
plotmin.threeinone(width,height,br3)
plotconcbatch.sixinone(width,height,gridblock)
plotminbatch.sixinone(width,height,gridblock)
plotgasbatch.threeinone(width,height,gridblock)