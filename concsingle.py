# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 15:25:32 2019

@author: tajayi3
"""

from t2listing import * 
from t2data import *
from math import log10
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from t2listing import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
mpl.style.use('default')
from prepfortoughreact import *
from batchreactionplotroutine import *
"""
read data
"""

path = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Gulf of Mexico Batch Reactions"
dest = r"C:\Users\tajayi3\Desktop\Research\Software\PyTOUGH-master"
file_name = "kdd_conc.tec"
file_name2 = "MESH"
lookup = 'CONNE'
myList = ["kdd_conc.tec", "kdd_gas.tec", "kdd_min.tec", "kdd_tim.tec", "MESH"]
tre1 = prepfortoughreact(path,dest,myList,lookup)
tre1.copyallfiles()
tre1.writetofile()


with open('test.txt') as f:
    br3 = f.read().splitlines()

#edit results
tre = toughreact_tecplot('kdd_conc.tec',br3)
tremin = toughreact_tecplot('kdd_min.tec',br3)
tre.last()
tremin.last()

gridblock = 'A11 1'
width = 10
height = 4
parameters = ['pH','t_ca+2','t_na+']
param2 = ['calcite','csh(1.6)','portlandite']
plotconc = batchreactionplotroutine(myList[0],br3,parameters)
plotmin = batchreactionplotroutine(myList[2],br3,param2)
plotconc.threeinone(width,height,gridblock)
plotmin.threeinone(width,height,gridblock)



data1 = tre.element['t_ca+2']
X = tre.element['X(m)']
Y = tre.element['Y(m)']
Z = tre.element['Z(m)']
X, Y = np.meshgrid(X, Y)
rblk = [blk[0] for blk in br3]
data1 = tre.element['t_ca+2']


    
mf = tre.history([('A11 1','pH')])
time = mf[0]
pH= mf[1]

#mf1 = tre.history([('A11 1','t_ca+2')])
#time1 = mf1[0]
#t_ca= mf1[1]
#
#
#mf2 = tre.history([('A11 1','t_hs-')])
#time = mf2[0]
#t_h= mf2[1]

#font = {'family' : 'normal',
#        'weight' : 'bold',
#        'size'   : 22}
#
#matplotlib.rc('font', **font)

#fig = plt.figure(figsize=(8,6)) 
#ax1 = fig.add_subplot(1,1,1)
#ax1.plot(time,pH,'r--', marker='x')
#ax1.grid()
#ax1.set_ylabel('pH')
#ax1.set_xlabel('Time (seconds)')
##ax1.legend(loc="upper right")
##plt.legend(['Permeabiliy of 6D'], loc='upper left')
#plt.tight_layout()





#ax2 = fig.add_subplot(2,3,3)
##ax1.semilogx(rblk,T,'k--', marker='o')
#ax2.plot(time,pH,'r--', marker='x')
#ax2.grid()
#ax2.set_ylabel('t_ca+2')
#ax2.set_xlabel('Time (seconds)')
##ax2.legend(loc="upper right")
##plt.legend(['Permeabiliy of 6D'], loc='upper left')
#plt.tight_layout()
#
#ax3 = fig.add_subplot(2,3,1)
##ax1.semilogx(rblk,T,'k--', marker='o')
#ax3.plot(time,t_h,'r--', marker='x')
#ax3.grid()
#ax3.set_ylabel('t_hs-')
#ax3.set_xlabel('Time (seconds)')
#ax3.legend(loc="upper right")
#plt.legend(['Permeabiliy of 6D'], loc='upper left')
plt.tight_layout()

fig.savefig('concplots.png',bbox_inches='tight') 
fig.savefig('concplots.pdf')