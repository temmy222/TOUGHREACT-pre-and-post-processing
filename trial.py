# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 17:48:49 2019

@author: tajayi3
"""

from prepfortoughreact import *
from batchreactionplotroutine import *
from multiplotroutine import *
import matplotlib
import matplotlib.pyplot as plt
from t2listing import * 
import os
import pandas as pd
import random


loca1 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Testing\H2S\Gulf of Mexico Shale Cement Flow - Onshore"
loca2 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Testing\H2S\Gulf of Mexico Shale Cement Flow - Offshore"
loca3 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Testing\H2S\Gulf of Mexico Sandstone Cement Flow - Onshore"
loca4 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Testing\H2S\Gulf of Mexico Sandstone Cement Flow - Offshore"
loca5 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Gulf of Mexico Batch Reactions Offshore Brine"
loca6 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Gulf of Mexico Sandstone Cement Flow - Onshore - GridTest"
loca7 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Gulf of Mexico Sandstone Cement Flow - Onshore - GridTest2"
loca8 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Geometry Change\H2S\Gulf of Mexico Shale Cement Flow - Onshore"
loca9 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Geometry Change\Gulf of Mexico Shale Cement Flow - Onshore"
loca10 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Pitzer\Sample file from TOUGH - Single block"
loca11 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Pitzer\Portlandite Calcite normal compare"
loca12 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Testing\Portlandite Calcite normal compare"
loca13 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Testing\Portlandite Calcite normal compare - less calcite"
loca14 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Testing\Portlandite Calcite normal compare - less hco3"
loca15 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Testing\Portlandite Calcite normal compare - less calcite - lesshco3"
loca16a = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Geometry Change\Gulf of Mexico Sandstone Cement Flow - Onshore - longer batch"
loca16b = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Geometry Change\Gulf of Mexico Sandstone Cement Flow - Offshore - longer batch"
loca17a = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Geometry Change\Gulf of Mexico Shale Cement Flow - Onshore - longer batch"
loca17b = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Geometry Change\Gulf of Mexico Shale Cement Flow - Offshore - longer batch"
loca18 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Testing\Portlandite Calcite normal compare - add csh - more portlandite"
loca19 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Gulf of Mexico Batch Reactions - Onshore Brine"
loca20 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Testing\Portlandite Calcite normal compare - add csh - add amorphous silica"
loca21 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Testing\Portlandite Calcite normal compare - add csh - add amorphous silica - mineral sensitivity1"
loca22 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Testing\Portlandite Calcite normal compare - add csh - add amorphous silica - mineral sensitivty2"
loca23 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Testing\Portlandite Calcite normal compare - add csh - add amorphous silica - hco32"
loca24 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Testing\Portlandite Calcite normal compare - add csh - add amorphous silica - hco31"
loca25 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Testing\Portlandite Calcite normal compare - add csh - add ettringitesilica"
loca26 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Gulf of Mexico Batch Reactions - Onshore Brine - more HCO3"
loca27 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Gulf of Mexico Batch Reactions - Onshore Brine - more HCO3 - longer time"
loca28 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Gulf of Mexico Shale Batch Reactions - Offshore brine"
loca29 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Gulf of Mexico Batch Reactions - Onshore Brine - more HCO3 - longer time"
loca30 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Pitzer\Portlandite Calcite CSH amorphous silica- high pressure - flow"
loca31 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Pitzer\Portlandite Calcite CSH amorphous silica- high pressure - DB flow"
loca =[loca30,loca31]
dest = r"C:\Users\tajayi3\Desktop\Research\Software\PyTOUGH-master"
files3 = ["kdd_conc.tec", "kdd_gas.tec", "kdd_min.tec", "kdd_tim.tec", "MESH"]
lookup = 'CONNE'
paramconc = ['pH','t_ca+2','t_hco3-']
parammin = ['Porosity','portlandite','calcite']
paramminsingle = ['Porosity','portlandite','ettringite']
paramminsinglelong = ['katoitesi1','Permz(m^2)','c3fh6','calcite','csh(1.6)','hydrotalcite']
paramgas = 'co2(g)'

#labels =['More Calcite','Less Calcite','Less HCO3','Less HCO3 less calcite','Add cSH']
labels =['Pitzer','Debye Huckel']


plotmin = multiplotroutine(loca,dest,files3,0,2,parammin)
plotconc = multiplotroutine(loca,dest,files3,0,0,paramconc)
plotgas = multiplotroutine(loca,dest,files3,0,1,paramgas) 

#m,n,v=plotconc.retrievedatamulti(loca,dest,files3,0,2,parammin)
plotmin.plotmulti(labels,purpose='presentation')
plotconc.plotmulti(labels,purpose='presentation')
plotgas.plotmulti(labels,purpose='presentation')


tre1 = prepfortoughreact(loca30,dest,files3,lookup)
tre1.copyallfiles()
tre1.writetofile()
with open('test.txt') as f:
    br3 = f.read().splitlines()

gridblock = br3[0]
plotminbatchpitz = batchreactionplotroutine(files3[2],br3,parammin,loca30)
#plotminbatch2 = batchreactionplotroutine(files3[2],br3,paramminsinglelong,loca17)
plotminbatchpitz.threeinonepitz(10,5,gridblock)

#plotminbatch2.sixinonepitz(10,5,gridblock)
#
#
#plotconcbatch = batchreactionplotroutine(files3[0],br3,paramconc,loca16)
#plotconcbatch.threeinone(10,5,gridblock)


tre1 = prepfortoughreact(loca31,dest,files3,lookup)
tre1.copyallfiles()
tre1.writetofile()
with open('test.txt') as f:
    br3 = f.read().splitlines()
    
plotminbatch = batchreactionplotroutine(files3[2],br3,parammin,loca31)
plotminbatch.threeinone(10,5,gridblock)