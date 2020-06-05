# -*- coding: utf-8 -*-
"""
Created on Fri May 10 20:34:58 2019

@author: tajayi3
"""
#from treactcompare import *
from prepfortoughreact import *
from batchreactionplotroutine import *
from multiplotroutine import *
import matplotlib
import matplotlib.pyplot as plt
from t2listing import * 
import os
import pandas as pd
import random
from crossplotmultiroutine import *


loca1 = r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore"
loca2 = r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - Ca injected sand equil brine Onshore"
loca3 = r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - Na acetate sand equil injected Onshore"
loca4 = r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore"
loca5 = r"C:\Users\AJ\OneDrive - Louisiana State University\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - same cond"

loca6=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - same high cond"
loca7=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - Ca injected sand equil brine Onshore - same high cond - longer time"
loca8=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - Na acetate sand equil injected Onshore - same high cond - longer time"
loca9=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - same high cond - longer time"

loca10=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - same low cond"
loca11=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - Ca injected sand equil brine Onshore - same low cond"
loca12=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - Na acetate sand equil injected Onshore - same low cond"
loca13=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - same low cond"

loca14 =r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Grid Sensitivity\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore"
loca15 = r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Grid Sensitivity\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer grid"
loca16 = r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Grid Sensitivity\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer grid2"

loca17=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - shc - longer time"
loca18=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - Ca injected sand equil brine Onshore - same high cond - longer time"
loca19 = r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - Na acetate sand equil injected Onshore - same high cond - longer time"
loca20=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - same high cond - longer time"

loca21=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - same low cond  - longer time"
loca22=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - Ca injected sand equil brine Onshore - same low cond - longer time"
loca23 = r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - Na acetate sand equil injected Onshore - same low cond  - longer time"
loca24=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - same low cond"

loca25=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Diffusivity sensitivity\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore"
loca26=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Diffusivity sensitivity\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - larger"
loca26b =r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Diffusivity sensitivity\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - muchlar"
loca27=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Diffusivity sensitivity\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - smaller"

loca28 = r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer time"
loca29 = r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - Ca injected sand equil brine Onshore - longer time"
loca30 = r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - Na acetate sand equil injected Onshore - longer time"
loca31 = r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - longer"

loca32 = r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\same RSA\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - longer"
loca33 = r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - longer"

loca34 = r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\no monosulfoaluminate\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - longer"
loca35 = r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - longer"

loca36 = r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Fast Rate all minerals\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - longer"

loca37 = r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\closed boundary\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - longer"

loca38 =r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\closed boundary\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer time"
loca39 = r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\closed boundary\Gulf of Mexico Cement Flow - Ca injected sand equil brine Onshore - longer time"
loca40 =r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\closed boundary\Gulf of Mexico Cement Flow - Na acetate sand equil injected Onshore - longer time"
loca41 = r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\closed boundary\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - longer"

loca42 =r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\remove gypsum\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer time"
loca43 = r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\CSH\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer time"

loca44 = r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\more co2\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer time"

loca45 = r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\h2s\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer time"

loca46 = r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\increased flow\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer time"
loca47 = r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\increased flow\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer time2"

loca48 = r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\same RSA\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer time"

loca49 = r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Fast Rate all minerals\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer"

loca50 = r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\more ca\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer time"
loca50b = r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Zeolites\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer time -addnocash"

loca51=r"C:\Users\AJ\OneDrive - Louisiana State University\GOM Sandstone Cement flow with Batch surface\Increased depth\Gulf of Mexico Sandstone Cement Flow - Ca injected brine Offshore"
loca52=r"C:\Users\AJ\OneDrive - Louisiana State University\GOM Sandstone Cement flow with Batch surface\Increased depth\Gulf of Mexico Sandstone Cement Flow - Ca injected brine Onshore"
loca53=r"C:\Users\AJ\OneDrive - Louisiana State University\GOM Sandstone Cement flow with Batch surface\Increased depth\Gulf of Mexico Sandstone Cement Flow - Na acetate brine"
loca54=r"C:\Users\AJ\OneDrive - Louisiana State University\GOM Sandstone Cement flow with Batch surface\Increased depth\Gulf of Mexico Sandstone Cement Flow - NaCl brine"

loca55=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Zeolites\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer time -add"
loca56=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Zeolites\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer time"
loca57 = r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\more cl\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - longer"

loca58 = r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\more na\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - longer -highertemp"
loca59 = r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\more cl\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - longer -hightemp"
loca60 = r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\more ca\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - longer"

loca61 = r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\more na\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer time"
loca62 = r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\more cl\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer time"
loca63 = r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\more ca\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer time"

loca64=r"C:\Users\AJ\OneDrive - Louisiana State University\GOM Sandstone Cement flow with Batch\Increased depth\Gulf of Mexico Sandstone Cement Flow - Ca injected brine Offshore"
loca65=r"C:\Users\AJ\OneDrive - Louisiana State University\GOM Sandstone Cement flow with Batch\Increased depth\Gulf of Mexico Sandstone Cement Flow - Ca injected brine Onshore"
loca66=r"C:\Users\AJ\OneDrive - Louisiana State University\GOM Sandstone Cement flow with Batch\Increased depth\Gulf of Mexico Sandstone Cement Flow - Na acetate brine"
loca67=r"C:\Users\AJ\OneDrive - Louisiana State University\GOM Sandstone Cement flow with Batch\Increased depth\Gulf of Mexico Sandstone Cement Flow - NaCl brine"


loca68 =r"C:\Users\AJ\OneDrive - Louisiana State University\GOM Shale Cement flow with Batch\Gulf of Mexico Shale Cement Flow - Ca injected brine Offshore"
loca69=r"C:\Users\AJ\OneDrive - Louisiana State University\GOM Shale Cement flow with Batch\Gulf of Mexico Shale Cement Flow - Ca injected brine Onshore"
loca70 = r"C:\Users\AJ\OneDrive - Louisiana State University\GOM Shale Cement flow with Batch\Gulf of Mexico Shale Cement Flow - Na acetate brine"
loca71 = r"C:\Users\AJ\OneDrive - Louisiana State University\GOM Shale Cement flow with Batch\Gulf of Mexico Shale Cement Flow - NaCl brine"

loca72 = r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Crack investigation\Gulf of Mexico Sandstone Cement Flow - NaCl brine"


loca73=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Diffusivity sensitivity\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer time"
loca74=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Diffusivity sensitivity\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longest - larger"
loca75=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Diffusivity sensitivity\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longest - muchlar"
loca76=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Diffusivity sensitivity\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longest - smaller"

loca77=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Diffusivity sensitivity\Gulf of Mexico Cement Flow - Ca injected sand equil brine Onshore - longer time"
loca78=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Diffusivity sensitivity\Gulf of Mexico Cement Flow - Ca injected sand equil brine Onshore - longer time - larger"
loca79=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Diffusivity sensitivity\Gulf of Mexico Cement Flow - Ca injected sand equil brine Onshore - longer time - muchlar"
loca80=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Diffusivity sensitivity\Gulf of Mexico Cement Flow - Ca injected sand equil brine Onshore - longer time - smaller"

loca81=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Diffusivity sensitivity\Gulf of Mexico Cement Flow - Na acetate sand equil injected Onshore - longer time"
loca82=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Diffusivity sensitivity\Gulf of Mexico Cement Flow - Na acetate sand equil injected Onshore - longer time - larger"
loca83=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Diffusivity sensitivity\Gulf of Mexico Cement Flow - Na acetate sand equil injected Onshore - longer time - muchlar"
loca84=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Diffusivity sensitivity\Gulf of Mexico Cement Flow - Na acetate sand equil injected Onshore - longer time - smaller"

loca85 =r"C:\Users\AJ\OneDrive - Louisiana State University\GOM Sandstone Cement flow with Batch\Increased depth\Gulf of Mexico Sandstone Cement Flow - Ca injected brine Offshore"
loca86=r"C:\Users\AJ\OneDrive - Louisiana State University\GOM Sandstone Cement flow with Batch\Increased depth\Gulf of Mexico Sandstone Cement Flow - Ca injected brine Onshore"
loca87 = r"C:\Users\AJ\OneDrive - Louisiana State University\GOM Sandstone Cement flow with Batch\Increased depth\Gulf of Mexico Sandstone Cement Flow - Na acetate brine"
loca88 = r"C:\Users\AJ\OneDrive - Louisiana State University\GOM Sandstone Cement flow with Batch\Increased depth\Gulf of Mexico Sandstone Cement Flow - NaCl brine"

loca89=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\increased flow\Gulf of Mexico Cement Flow - Ca injected sand equil brine Onshore - longer time"
loca90=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\increased flow\Gulf of Mexico Cement Flow - Ca injected sand equil brine Onshore - longer time2"

loca91=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\increased flow\Gulf of Mexico Cement Flow - Na acetate sand equil injected Onshore - longer time"
loca92=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\increased flow\Gulf of Mexico Cement Flow - Na acetate sand equil injected Onshore - longer time2"


loca93=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\increased flow\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - longer"
loca94=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\increased flow\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - longer time2"

loca95=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\GOM Ca Onshore flux with Ca offshore"
loca96=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\GOM Ca Onshore flux with Na acetate"

loca97=r"C:\Users\AJ\OneDrive - Louisiana State University\GOM Shale Cement flow with Batch\GOM Ca Onshore flux with Ca offshore"
loca98=r"C:\Users\AJ\OneDrive - Louisiana State University\GOM Shale Cement flow with Batch\GOM Ca Onshore flux with Na acetate"

loca99=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\increased flow\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - shorter time"
loca100=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\increased flow\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer time3"

loca101=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\increased flow\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - shorter time"
loca102=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\increased flow\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - longer time3"

loca103 = r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\GOM NaCl flux with Ca Offshore"
loca104=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\GOM NaCl flux with Na acetate"

loca105=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Diffusivity sensitivity\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longest -E-7"
loca106=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Diffusivity sensitivity\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longest -E-8"
loca107=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Diffusivity sensitivity\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longest -E-12"
loca108=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Diffusivity sensitivity\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longest -E-13"

loca109=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\same RSA\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - order higher"
loca110=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\same RSA\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - order lower"

loca111=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Crack investigation\Gulf of Mexico Sandstone Cement Flow - NaCl brine - Closed"

# loca =[loca21,loca22,loca23,loca24]
# loca =[loca27,loca25,loca26,loca26b]
# loca =[loca28,loca29,loca30,loca31]
#loca = [loca51,loca52,loca53,loca54]
#loca=[loca64,loca65,loca66,loca67]
#loca=[loca68,loca69,loca70,loca71]

# loca=[loca72,loca31]
# loca =[loca32,loca33]
# loca = [loca6,loca7,loca8,loca9]
#loca = [loca10,loca11,loca12,loca13]
# loca = [loca48,loca28]
#loca = [loca34,loca36]
# loca = [loca37,loca35]
# loca = [loca38,loca28]
#loca = [loca38,loca39,loca40,loca41]
#loca = [loca17,loca18,loca19,loca20]
# loca = [loca41,loca31]
# loca = [loca47,loca46,loca28]
# loca = [loca89,loca90,loca29]
# loca = [loca91,loca92,loca30]
# loca = [loca93,loca94,loca31]
# loca = [loca29,loca95,loca96]
# loca = [loca69,loca97,loca98]
# loca = [loca99,loca28,loca100]
# loca = [loca101,loca31,loca102]
# loca = [loca31,loca103,loca104]

# loca = [loca60,loca31]
# loca = [loca50,loca28]
# loca = [loca49]
# loca = [loca55,loca56,loca28]
#loca = [loca57,loca31]
# loca = [loca76,loca73,loca74,loca75]
# loca = [loca76,loca73,loca75]
# loca = [loca77,loca78,loca79,loca80]
# loca = [loca81,loca82,loca83,loca84]
# loca = [loca85,loca86,loca87,loca88]
# loca = [loca105,loca106,loca107,loca108]
loca = [loca109,loca28,loca110]

dest = r"C:\Users\AJ\Desktop\My Desktop\LSU\LSU-Corona\PyTOUGH-master"
files2 = ["kdd_concdiff.tec", "kdd_gasdiff.tec", "kdd_mindiff.tec", "kdd_timdiff.tec", "MESH"]
files1 = ["kdd_concvtk.tec", "kdd_gasvtk.tec", "kdd_minvtk.tec", "kdd_timvtk.tec", "MESH"]
files3 = ["kdd_conc.tec", "kdd_gas.tec", "kdd_min.tec", "kdd_tim.tec", "MESH"]
lookup = 'CONNE'


parameters = ['pH','t_mg+2','t_ca+2','t_so4-2']
parameters2 = ['t_h+','t_na+','t_hco3-','t_cl-']
parameters3 = ['t_h4sio4','t_al+3','t_fe+2','t_hs-']
parameters4 = ['t_al+3','t_fe+2']
parameters5 = ['P(bar)','T(C)']
parameters6 = ['t_hco3-','t_cl-']
parameters7 = ['t_h4sio4','t_hs-']
parameters8 = ['aH2O','t_h2o']


# param2 = ['gypsum','Porosity','friedel_salt','ettringite']
param2 = ['calcite','Porosity','portlandite','ettringite']
# param3 = ['portlandite','calcite','jennite','monosulfoalu']
param3 = ['friedel_salt','gypsum','jennite','monosulfoalu']
#param3 = ['portlandite','ettringite']
# param4 = ['friedel_salt']
#param4  = ['katoitesi1','c3fh6']
param5  = ['katoitesi1','c3fh6','tobermorite(','hydrotalcite']
param6 = ['brucite','chalcedony','dolomite','calcite']
param7 = ['calcite','sepiolite']
param8 = ['hydrotalcite','dolomite']
param9 = ['monosulfoalu','jennite']
paramcross = ['brucite','chalcedony','dolomite','pH']
rep = 'Porosity'

#param2 = ['quartz(alpha','microcline','albite(low)']
#param3 = ['halite','kaolinite','illite(mg)']
#param4  = ['montmorillon','muscovite(or','chlorite(cca']
#param5 = ['dolomite','hematite']

#plotconclong = batchreactionplotroutine(files3[0],br3,parameters)
# labels =['Ca Offshore (Case 4)','Ca onshore (Case 3)','Na acetate (Case 2)','NaCl (Case 1)','NaCl Same','More Ca','More HCO3']
# labels =['$1.65E-11 m^{2}/s$','$1.65E-10 m^{2}/s$ (base case)','$1.65E-9 m^{2}/s$','$1.65E-5 m^{2}/s$']
# labels =['$1.65E-11 m^{2}/s$','$1.65E-10 m^{2}/s$ (base case)','$1.65E-5 m^{2}/s$']
# labels =['Closed boundary','Open boundary (base case)']
# labels =['Cracked Cement','Uncracked Cement']
# labels=['Zeolites added from start','Zeolites only allowed to precipitate','No zeolites at all']
# labels = ["Increased Calcium Conc","Base Case Calcium Conc"]
# labels = ["0.01 Mole fraction CO2","1.00 Mole fraction CO2"]
# labels =['Fastest rate','Faster rate','Fast rate']
# labels =['1.53E-7 m$^3$/day','1.53E-5 m$^3$/day (base case)','1.53E-3 m$^3$/day']
# labels =['Sea Water Flux (base case)','Ca Offshore brine flux','Na acetate brine flux']
# labels =['Fixed reactive area','Varying reactive area']
# labels =['RSA-1','RSA-2 (base case)']
# labels = ['Fixed kinetic parameters','Different kinetic parameters']
# labels =['$1.65E-7 m^{2}/s$','$1.65E-8 m^{2}/s$','$1.65E-12 m^{2}/s$','$1.65E-13 m^{2}/s$']
labels =['RSA-1 (higher)','RSA (base case)','RSA-2 (lower)']

masa2 = multiplotroutine(loca,dest,files3,0,2,param2)
masa3 = multiplotroutine(loca,dest,files3,0,2,param3)
# masa4 = multiplotroutine(loca,dest,files3,0,2,param4)
# masa5 = multiplotroutine(loca,dest,files3,0,2,param5)
# masa6 = multiplotroutine(loca,dest,files3,0,2,param6)
# masa7 = multiplotroutine(loca,dest,files3,0,2,param7)
#masa8 = multiplotroutine(loca,dest,files3,0,2,param8)
#masa9 = multiplotroutine(loca,dest,files3,0,2,param9)
# cross2 = crossplotmultiroutine(loca,dest,files3,0,2,paramcross)
#
#
#
masaconc1 = multiplotroutine(loca,dest,files3,0,0,parameters)
# masaconc2 = multiplotroutine(loca,dest,files3,0,0,parameters2)
# masaconc3 = multiplotroutine(loca,dest,files3,0,0,parameters3)
# masaconc4 = multiplotroutine(loca,dest,files3,0,0,parameters4)
#masaconc5 = multiplotroutine(loca,dest,files3,0,0,parameters5)
#masaconc6 = multiplotroutine(loca,dest,files3,0,0,parameters6)
#masaconc7 = multiplotroutine(loca,dest,files3,0,0,parameters7)
#masaconc8 = multiplotroutine(loca,dest,files3,0,0,parameters8)





masa2.plotmultimulti(labels,purpose='presentation',style='multiple')
masa3.plotmultimulti(labels,purpose='presentation',style='multiple')
# masa4.plotmultimulti(labels,purpose='presentation',style='multiple')
# masa5.plotmultimulti(labels,purpose='presentation',style='multiple')
# masa6.plotmultimulti(labels,purpose='presentation',style='multiple')
# masa7.plotmultimulti(labels,purpose='presentation',style='multiple')
#masa8.plotmultimulti(labels,purpose='presentation')
#masa9.plotmultimulti(labels,purpose='presentation')
# cross2.plotmultimulti(labels,purpose='presentation',style='multiple')

#
#masa2.plotmultimulti(labels,purpose='presentation',style='vertical')
#masa3.plotmultimulti(labels,purpose='presentation',style='vertical')
#masa4.plotmultimulti(labels,purpose='presentation',style='vertical')
#masa5.plotmultimulti(labels,purpose='presentation',style='vertical')
#masa6.plotmultimulti(labels,purpose='presentation',style='vertical')
#masa7.plotmultimulti(labels,purpose='presentation',style='vertical')
#masa8.plotmultimulti(labels,purpose='presentation',style='vertical')
#masa9.plotmultimulti(labels,purpose='presentation',style='vertical')
#
#
#
masaconc1.plotmultimulti(labels,purpose='presentation',style='multiple')
# masaconc2.plotmultimulti(labels,purpose='presentation',style='multiple')
# masaconc3.plotmultimulti(labels,purpose='presentation',style='multiple')
# masaconc4.plotmultimulti(labels,purpose='presentation')
#masaconc5.plotmultimulti(labels,purpose='presentation')
#masaconc6.plotmultimulti(labels,purpose='presentation')
#masaconc7.plotmultimulti(labels,purpose='presentation')
#masaconc8.plotmultimulti(labels,purpose='presentation')
#
#masaconc1.plotmultimulti(labels,purpose='presentation',style='vertical')
#masaconc2.plotmultimulti(labels,purpose='presentation',style='vertical')
#masaconc3.plotmultimulti(labels,purpose='presentation',style='vertical')
#masaconc4.plotmultimulti(labels,purpose='presentation',style='vertical')
#masaconc5.plotmultimulti(labels,purpose='presentation',style='vertical')
#masaconc6.plotmultimulti(labels,purpose='presentation',style='vertical')
#masaconc7.plotmultimulti(labels,purpose='presentation',style='vertical')
#masaconc8.plotmultimulti(labels,purpose='presentation',style='vertical')


#m,n,value1 = retrievedata(loca,dest,files3,2,2,param2)
#m,n,o = masa2.retrievedatamulti(loca,dest,files3,0,0,parameters)


'''
commented out codes
'''
'''
#def batchcompare (locations,dest,files,gridblocknumber,indexa,prop,labels):
#    color = ['kd-.','','k+--','','ko--','','k>--','','k<:','','kx:','','kd-.']
#    dictionary = {}
#    lst = []
#    for i in range(0,len(locations)):
#        timer1 = 'first' + str(i)
#        data1 = 'data' + str(i)
#        lst.append(timer1)
#        lst.append(data1)
#        tre1 = prepfortoughreact(locations[i],dest,files,lookup)
#        tre1.copyallfiles()
#        tre1.writetofile()
#        os.chdir(dest)
#        with open('test.txt') as f:
#            br3 = f.read().splitlines()
#        tre=toughreact_tecplot(files[indexa],br3)
#        tre.last()
#        mf = tre.history([(br3[gridblocknumber],prop)])
#        timerr = mf[0]
#        data= mf[1]
#        for index,character in enumerate(lst): 
#            if character not in dictionary.keys():
#                dictionary[character] = [] # because same character might be repeated in different positions
#        for index,character in enumerate(lst): 
#            if 'first' in character and len(dictionary[character]) == 0:
#                dictionary[character].append(timerr)
#            elif 'data' in character and len(dictionary[character]) == 0:
#                dictionary[character].append(data)
#                
#    for state, capital in dictionary.items():
#        if len(dictionary[state][0]) > 100:
#            dictionary[state][0] = dictionary[state][0][::20]
#
#    value1 = 10000000000000000000000000000000000000
#    for state, capital in dictionary.items():
#        if 'first' in state:
#            manny = dictionary[state][0]
#            value0 = manny[len(manny)-1]
#            if value0 <= value1:
#                value1 = value0
#    
#    for i in range(0,len(lst),2):
#        plt.plot(dictionary[lst[i]][0],dictionary[lst[i+1]][0],color[i])
#        plt.legend(labels)
#    plt.grid()
#    plt.xlabel('Time (seconds) ')
#    plt.ylabel(prop)
##    return dictionary
#  
#batchcompare(loca,dest,files3,0,2,param2[1],labels)
#
#
#def retrievedata (locations,dest,files,gridblocknumber,indexa,prop):
#    dictionary = {}
#    lst = []
#    lookup = 'CONNE'
#    for i in range(0,len(locations)):
#        tre1 = prepfortoughreact(locations[i],dest,files,lookup)
#        tre1.copyallfiles()
#        tre1.writetofile()
#        os.chdir(dest)
#        timer1 = 'first0'
#        data1 = 'data0'
#        with open('test.txt') as f:
#            br3 = f.read().splitlines()
#        tre=toughreact_tecplot(files[indexa],br3)
#        tre.last()
#        for j in range(0,len(param2)):
#            if (timer1 or data1) not in lst:
#                timer1 = 'first' + str(random.randint(1,101))
#                data1 = 'data' + str(random.randint(1,101))
#                lst.append(timer1)
#                lst.append(data1)
#            elif (timer1 or data1) in lst:
#                timer1 = 'first' + str(random.randint(1,101)) + str(random.randint(1,101))
#                data1 = 'data' + str(random.randint(1,101)) + str(random.randint(1,101))
#                lst.append(timer1)
#                lst.append(data1)
#            mf = tre.history([(br3[gridblocknumber],prop[j])])
#            timerr = mf[0]
#            data= mf[1]
#            for index,character in enumerate(lst): 
#                if character not in dictionary.keys():
#                    dictionary[character] = [] # because same character might be repeated in different positions
#            for index,character in enumerate(lst): 
#                if 'first' in character and len(dictionary[character]) == 0:
#                    dictionary[character].append(timerr)
#                elif 'data' in character and len(dictionary[character]) == 0:
#                    dictionary[character].append(data)
#
#    # truncate large dataset
#    for state, capital in dictionary.items():
#        if len(dictionary[state][0]) > 100:
#            dictionary[state][0] = dictionary[state][0][::20]
#
#    # pick minimum time for analysis
#    value1 = 10000000000000000000000000000000000000
#    for state, capital in dictionary.items():
#        if 'first' in state:
#            manny = dictionary[state][0]
#            value0 = manny[len(manny)-1]
#            if value0 <= value1:
#                value1 = value0
#    return dictionary, lst, value1
#    
#    
#def colorcoding(style):
#    markers = ["o","v","^","<",">","1","2","3","4","8","s","p","P","*","h","H","+","x","X","D","d","|","_"]
#    if style.lower()=='publication':
#        colormarker = 'k' + markers[random.randint(0,(len(markers)-1))]
#    elif style.lower()=='presentation':
#        colormarker = 'r' + markers[random.randint(0,(len(markers)-1))]
#    return colormarker
#    
#
#    
#    
#def plotmulti (width,height,prop,linestyle='dashed'):
#    font = {'family' : 'normal','weight' : 'bold','size'   : 14}
#    matplotlib.rc('font', **font)
#    dictionary,lst,value1 = retrievedata(loca,dest,files3,2,2,param2)
#    fig = plt.figure(figsize=(width,height))
#    kpansa = 0
#    paralengthdouble = len(param2)*2
#    for number in range(1,len(param2)+1):
#        ax = fig.add_subplot(1,len(param2),number)
#        for i in range(kpansa,len(dictionary),paralengthdouble):
#            ax.plot(dictionary[lst[i]][0],dictionary[lst[i+1]][0],colorcoding('publication'),linestyle=linestyle,label=labels[number-1])
#            ax.set_xlim((0,value1))
#            ax.set_ylim((min(dictionary[lst[i]][0]),max(dictionary[lst[i+1]][0])))
#        kpansa = kpansa+2
#        ax.legend()
#        ax.grid()
#        ax.set_xlabel('Time (seconds)',fontsize=14,fontweight='bold')
#        ax.set_ylabel(prop[number-1],fontsize=14,fontweight='bold')
#        plt.tight_layout()

#    os.chdir(loca[0])
#    fig.savefig(labels[0] +'.jpg',bbox_inches='tight',dpi=(600))
#    matplotlib.style.use('classic')
    
    
#plotmulti(14,7,param2)


#dictionary = {}
#lst = []
#color = ['kd-.','','ko--','','ko--','','k>--','','k<:','','kx:','','kd-.','kd-.','','ko--','','ko--','','k>--','','k<:','','kx:','','kd-.']
#for i in range(0,len(loca)):
#    tre1 = prepfortoughreact(loca[i],dest,files3,lookup)
#    tre1.copyallfiles()
#    tre1.writetofile()
#    os.chdir(dest)
#    timer1 = 'first0'
#    data1 = 'data0'
#    with open('test.txt') as f:
#        br3 = f.read().splitlines()
#    tre=toughreact_tecplot(files3[0],br3)
#    tre.last()
#    for j in range(0,len(parameters)):
#        if (timer1 or data1) not in lst:
#            timer1 = 'first' + str(random.randint(1,101))
#            data1 = 'data' + str(random.randint(1,101))
#            lst.append(timer1)
#            lst.append(data1)
#        elif (timer1 or data1) in lst:
#            timer1 = 'first' + str(random.randint(1,101)) + str(random.randint(1,101))
#            data1 = 'data' + str(random.randint(1,101)) + str(random.randint(1,101))
#            lst.append(timer1)
#            lst.append(data1)
#        mf = tre.history([(br3[0],parameters[j])])
#        timerr = mf[0]
#        data= mf[1]
#        for index,character in enumerate(lst): 
#            if character not in dictionary.keys():
#                dictionary[character] = [] # because same character might be repeated in different positions
#        for index,character in enumerate(lst): 
#            if 'first' in character and len(dictionary[character]) == 0:
#                dictionary[character].append(timerr)
#            elif 'data' in character and len(dictionary[character]) == 0:
#                dictionary[character].append(data)
#
## truncate large dataset
#for state, capital in dictionary.items():
#    if len(dictionary[state][0]) > 100:
#        dictionary[state][0] = dictionary[state][0][::20]
#
## pick minimum time for analysis
#value1 = 10000000000000000000000000000000000000
#for state, capital in dictionary.items():
#    if 'first' in state:
#        manny = dictionary[state][0]
#        value0 = manny[len(manny)-1]
#        if value0 <= value1:
#            value1 = value0
#
#fig = plt.figure(figsize=(8,6))
#kpansa = 0
#paralengthdouble = len(parameters)*2
#mandy = (len(loca)*2)-1
#for number in range(1,len(parameters)+1):
#    ax = fig.add_subplot(1,3,number)
#    for i in range(kpansa,len(dictionary),paralengthdouble):
#        print(paralengthdouble)
#        print(kpansa)
#        ax.plot(dictionary[lst[i]][0],dictionary[lst[i+1]][0],color[i],label=labels[number-1])
#        ax.set_xlim((0,value1))
#    kpansa = kpansa+2
#    ax.legend()
#    ax.grid()
#    ax.set_xlabel('Time (seconds) ')
#    ax.set_ylabel(parameters[number-1])
#    plt.tight_layout()

'''