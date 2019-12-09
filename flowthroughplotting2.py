# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 20:04:11 2019

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
 
            
dest1 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\For paper\GOM Cement flow with batch\Increased depth\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore"
dest2 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\For paper\GOM Cement flow with batch\Increased depth\Gulf of Mexico Cement Flow - Ca injected sand equil brine Onshore"
dest3 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\For paper\GOM Cement flow with batch\Increased depth\Gulf of Mexico Cement Flow - Na acetate sand equil injected Onshore"
dest4 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\For paper\GOM Cement flow with batch\Increased depth\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore"
dest5 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\For paper\GOM Cement flow with batch\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - same cond"

dest6=r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\For paper\GOM Cement flow with batch\Increased depth\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - same high cond"
dest7=r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\For paper\GOM Cement flow with batch\Increased depth\Gulf of Mexico Cement Flow - Ca injected sand equil brine Onshore - same high cond"
dest8=r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\For paper\GOM Cement flow with batch\Increased depth\Gulf of Mexico Cement Flow - Na acetate sand equil injected Onshore - same high cond"
dest9=r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\For paper\GOM Cement flow with batch\Increased depth\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - same high cond"

dest10=r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\For paper\GOM Cement flow with batch\Increased depth\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - same low cond"
dest11=r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\For paper\GOM Cement flow with batch\Increased depth\Gulf of Mexico Cement Flow - Ca injected sand equil brine Onshore - same low cond"
dest12=r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\For paper\GOM Cement flow with batch\Increased depth\Gulf of Mexico Cement Flow - Na acetate sand equil injected Onshore - same low cond"
dest13=r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\For paper\GOM Cement flow with batch\Increased depth\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - same low cond"

loc = r"C:\Users\tajayi3\Desktop\Research\Software\PyTOUGH-master"

dest = dest1

file_name = "kdd_conc.tec"
file_name2 = "MESH"
lookup = 'CONNE'
myList = ["kdd_conc.tec", "kdd_gas.tec", "kdd_min.tec", "kdd_tim.tec", "MESH","geom2.dat","INFILE"]
tre1 = prepfortoughreact(dest,loc,myList,lookup)
tre1.copyallfiles()
tre1.writetofile()

"""
Graph Plotting
"""
with open('test.txt') as f:
    br3 = f.read().splitlines()
    
paramconc = ['pH','t_cl-','t_mg+2']
paramconc2 = ['t_na+','t_so4-2','t_hco3-']
paramconc3 = ['t_h4sio4','t_al+3','t_fe+2']
paramconc4 = ['t_hs-','t_h2o','aH2O']
param2 = ['monosulfoalu','Porosity','jennite']
param3 = ['dolomite','portlandite','ettringite']
param4  = ['katoitesi1','c3fh6','hydrotalcite']
param5 = ['portlandite','calcite','monosulfoalu']
param6 = ['gypsum','ettringite','friedel_salt']
paramone = ['Porosity','monosulfoalu','calcite']




#write to vtk for viewing with Paraview

#filenamegrid = 'geom2.dat'
#geo = mulgrid().read(filenamegrid)
#filenamevtk = 'GOM Ca brine Cement Flow - Offshore low temp cond.pvd'
#trem = toughreact_tecplot(myList[2],br3)
#trem.write_vtk(geo, filenamevtk)


face = 'Z'
plotX = 'X'
Zlayer = 5
Ylayer = 1
Xlayer = 3


plotmins = flowreactionplotroutine(myList[2],br3,paramone,dest)
dama = plotmins.plotdistance(face,plotX,Xlayer,Ylayer,Zlayer,0)
dama2 = plotmins.retrievedatadistance2(face,plotX,Xlayer,Ylayer,Zlayer,0)

plotconc = flowreactionplotroutine(myList[0],br3,paramconc,dest)
plotconc.plot2D(10,5,br3,'XZ')
plotmins.plot2D(10,5,br3,'XZ')

os.chdir(loc)
plotmin = flowreactionplotroutine(myList[2],br3,param4,dest)
plotconc2 = flowreactionplotroutine(myList[0],br3,paramconc2,dest)
plotconc2.plot2D(10,5,br3,'XZ')
plotmin.plot2D(10,5,br3,'XZ')


os.chdir(loc)
plotmin2 = flowreactionplotroutine(myList[2],br3,param6,dest)
plotconc3 = flowreactionplotroutine(myList[0],br3,paramconc3,dest)
plotconc3.plot2D(10,5,br3,'XZ')
plotmin2.plot2D(10,5,br3,'XZ')

os.chdir(loc)
plotmin3 = flowreactionplotroutine(myList[2],br3,param3,dest)
plotconc4 = flowreactionplotroutine(myList[0],br3,paramconc4,dest)
plotconc4.plot2D(10,5,br3,'XZ')
plotmin3.plot2D(10,5,br3,'XZ')

"""
what to do

modify threeinone plot in flowreactionplotroutine to include single plot (that is one plot per screen, two plots and so on)
 and to accept direction of plots ( that is X-Z, Y-Z or X-Y)
 
 incorporate time into analysis as well
 
 look at negative depth
"""

#tre = toughreact_tecplot('kdd_concvtk.tec',br3)

#gridblock = br3[0]
#filenamegrid = 'geom2.dat'
#
#param2 = ['brucite','Porosity','friedel_salt']
#tre = toughreact_tecplot(myList[2],br3)
#tre.last()
#X = tre.element['X(m)']
#Y = tre.element['Y(m)']
#Z = tre.element['Z(m)']
#tcl = tre.element['t_cl-']
#dictionary = {}
#dictionary['X'] = []
#dictionary['Y'] = []
#dictionary['Z'] = []
#dictionary['tcl'] = []
#dictionary['X'].append(X)
#dictionary['Y'].append(Y)
#dictionary['Z'].append(Z)
#dictionary['tcl'].append(tcl)
#face = 'X'
#plotX = 'Y'
#Xgrid = 25
#Ygrid = 2
#Zgrid = 5
#dimension = [25,2,5]
#Zlayer = 1
#Ylayer = 1
#Xlayer = 3
#
#df = pd.DataFrame(index=range(len(X)))
#df['X'] = X
#df['Y'] = Y
#df['Z'] = Z
#df['tcl'] = tcl
#
#def getgridnumber(df,direction):
#    X = df[direction]
#    d ={}
#    for i in X:
#        if i not in d:
#            d[i] = 1
#        else:
#            d[i] += 1
#    m = list(d.keys())
#    return m, len(d) 
#
#Z1,Z2 = getgridnumber(df,'Z')
#Y1,Y2 = getgridnumber(df,'Y')
#X1,X2 = getgridnumber(df,'X')
#
#
#if face == 'Z':  
#    m = []
#    n = []
#    for index, row in df.iterrows():
#        if df.iloc[index,2]!=Z1[Zlayer-1]:
#            m.append(index)
#    df.drop(m, inplace=True)
#    df = df.reset_index(drop=True)
#    if plotX == 'X':
#        for index, row in df.iterrows():
#            if df.iloc[index,1]!=Y1[Ylayer-1]:
#                n.append(index)
#        df.drop(n, inplace=True)
#        df = df.reset_index(drop=True)
#        plt.plot(df['X'],df['tcl'])
#        plt.grid()
#    if plotX == 'Y':
#        for index, row in df.iterrows():
#            if df.iloc[index,0]!=X1[Xlayer-1]:
#                n.append(index)
#        df.drop(n, inplace=True)
#        df = df.reset_index(drop=True)
#        plt.plot(df['Y'],df['tcl'])
#        plt.grid()
#        
#if face == 'Y':  
#    m = []
#    n = []
#    for index, row in df.iterrows():
#        if df.iloc[index,1]!=Y1[Ylayer-1]:
#            m.append(index)
#    df.drop(m, inplace=True)
#    df = df.reset_index(drop=True)
#    if plotX == 'X':
#        for index, row in df.iterrows():
#            if df.iloc[index,2]!=Z1[Zlayer-1]:
#                n.append(index)
#        df.drop(n, inplace=True)
#        df = df.reset_index(drop=True)
#        plt.plot(df['X'],df['tcl'])
#        plt.grid()
#    if plotX == 'Z':
#        for index, row in df.iterrows():
#            if df.iloc[index,0]!=X1[Xlayer-1]:
#                n.append(index)
#        df.drop(n, inplace=True)
#        df = df.reset_index(drop=True)
#        plt.plot(df['Z'],df['tcl'])
#        plt.grid()
#        
#
#            
#if face == 'X':
#    m = []
#    n = []
#    for index, row in df.iterrows():
#        if df.iloc[index,0]!=X1[Xlayer-1]:
#            m.append(index)
#    df.drop(m, inplace=True)
#    df = df.reset_index(drop=True)
#    if plotX == 'Z':
#        for index, row in df.iterrows():
#            if df.iloc[index,1]!=Y1[Ylayer-1]:
#                n.append(index)
#        df.drop(n, inplace=True)
#        df = df.reset_index(drop=True)
#        plt.plot(df['Z'],df['tcl'])
#        plt.grid()
#    if plotX == 'Y':
#        for index, row in df.iterrows():
#            if df.iloc[index,2]!=Z1[Zlayer-1]:
#                n.append(index)
#        df.drop(n, inplace=True)
#        df = df.reset_index(drop=True)
#        plt.plot(df['Y'],df['tcl'])
#        plt.grid()
#    