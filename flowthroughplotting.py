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

dest = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Geometry Change\Gulf of Mexico Sandstone Cement Flow - Onshore - longer batch"
#dest2 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Geometry Change\Gulf of Mexico Sandstone Cement Flow - Onshore"

loc = r"C:\Users\tajayi3\Desktop\Research\Software\PyTOUGH-master"
#
#loca1 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\VTK testing"
#loca2 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Diffusion Testing"
#loca3 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Cement Batch Reactions TOUGH Brine - Diffusion"
#loca4 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Gulf of Mexico Sandstone Cement Flow - Onshore - GridTest"
#loca5 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Gulf of Mexico Sandstone Cement Flow - Onshore - GridTest2"
#loca6 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Gulf of Mexico Shale Cement Flow - Onshore"
#loca7 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Geometry Change\H2S\Gulf of Mexico Sandstone Cement Flow - Onshore"
#loca8 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Geometry Change\Gulf of Mexico Sandstone Cement Flow - Onshore"
#loca9 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Testing\H2S\Gulf of Mexico Shale Cement Flow - Onshore"
#loca10 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Testing\H2S\Gulf of Mexico Shale Cement Flow - Offshore"
#loca11 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Testing\H2S\Gulf of Mexico Sandstone Cement Flow - Onshore"
#loca12 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Testing\H2S\Gulf of Mexico Sandstone Cement Flow - Offshore"
#loca13 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Testing\Gulf of Mexico Shale Cement Flow - Onshore"
#loca14 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Testing\Gulf of Mexico Shale Cement Flow - Offshore"
#loca15 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Testing\Gulf of Mexico Sandstone Cement Flow - Onshore"
#loca16 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Testing\Gulf of Mexico Sandstone Cement Flow - Offshore"
#
#loca =[loca9,loca10,loca11,loca12]

#labels =['Shale Cement Flow - Onshore','Shale Cement Flow - Offshore','Sandstone Cement Flow - Onshore','Sandstone Cement Flow - Offshore' ]

file_name = "kdd_conc.tec"
file_name2 = "MESH"
lookup = 'CONNE'
myList = ["kdd_conc.tec", "kdd_gas.tec", "kdd_min.tec", "kdd_tim.tec", "MESH","geom2.dat"]
#myList = ["hpip_conc.tec", "hpip_gas.tec", "hpip_min.tec", "hpip_tim.tec", "MESH"]
tre1 = prepfortoughreact(dest,loc,myList,lookup)
tre1.copyallfiles()
tre1.writetofile()

print(os.getcwd())

"""
Graph Plotting
"""
with open('test.txt') as f:
    br3 = f.read().splitlines()

#tre = toughreact_tecplot('kdd_concvtk.tec',br3)

gridblock = br3[0]
filenamegrid = 'geom2.dat'



# write to vtk for viewing with Paraview

geo = mulgrid().read(filenamegrid)
filenamevtk = 'Sandstone Real Onshore Flow mineral.pvd'
trem = toughreact_tecplot(myList[2],br3)
trem.write_vtk(geo, filenamevtk)


width = 10
height = 6

parameters = ['pH','t_cl-','t_na+']
plotconc = flowreactionplotroutine(myList[0],br3,parameters)
plotconcbatch = batchreactionplotroutine(myList[0],br3,parameters,dest)


param2 = ['calcite','Porosity','microcline']
plotmin = flowreactionplotroutine(myList[2],br3,param2)
plotminbatch = batchreactionplotroutine(myList[2],br3,param2,dest)


paramgas = ['SatGas','RH','co2(g)']
plotgas = flowreactionplotroutine(myList[1],br3,paramgas)
plotgasbatch = batchreactionplotroutine(myList[1],br3,paramgas,dest)


plotconc.threeinone(width,height,br3)
plotmin.threeinone(width,height,br3)
#plotconcbatch.threeinone(width,height,gridblock)
#plotminbatch.threeinone(width,height,gridblock)
#plotgasbatch.threeinone(width,height,gridblock)
#plotconcbatch.resultscompare(loca,loc,myList,0,0,parameters[0],labels)