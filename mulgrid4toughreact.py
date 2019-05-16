# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:44:31 2019

@author: tajayi3
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

"""
flow input files with mulgrid as a template to facilitate writing to pvd for viewing with paraview
"""

xblock = 20
yblock = 20
zblock = 1
dx = [10.]*xblock
dy = [8.]*yblock
dz = [1.0] *zblock

geo = mulgrid().rectangular(dx, dy, dz)
geo.write('geom2.dat')

# Testing Mulgrid for toughreact
dat = t2data()
dat.title = 'Hydrostatic 3D example'
dat.grid = t2grid().fromgeo(geo)
dat.parameter.update(
    {'max_timesteps': 2999,
     'tstop': 8640000,
     'const_timestep': 1,
     'print_interval': 20,
     'gravity': 9.81,
     'default_incons': [101.3e3, 20.]})
dat.start = True

dat.grid.rocktype['dfalt'].permeability[:0] = 9.869233e-15
dat.grid.rocktype['dfalt'].permeability[:1] = 9.869233e-15
dat.grid.rocktype['dfalt'].permeability[:2] = 9.869233e-15
dat.grid.rocktype['dfalt'].porosity = 0.6

# Set MOPs:
dat.parameter['option'][1] = 1
dat.parameter['option'][16] = 5

# Set relative permeability (Corey) and capillarity functions:
dat.relative_permeability = {'type': 3, 'parameters': [0.3, 0.1, 0., 0., 0.]}
dat.capillarity = {'type': 1, 'parameters': [0., 0., 1., 0., 0.]}
dat.multi = {'num_components': 1, 'num_equations' :2,'num_phases': 2,'num_secondary_parameters': 6}

# add generator:
energy = 5.
shutintime = 6*3600
simtime = 31.25 * 86400
rate = 0.00920081019
rate2 = -0.920081019
testenthalpy = [energy,0 ,0]
well = 'wel '
compo = 'WATE'
direction = 'x'

if direction == 'x':
    for i in range(0,xblock):
        gen = t2generator(name = well + str(i), block = dat.grid.blocklist[i].name,gx = rate, type = compo, rate = rate)
        dat.add_generator(gen)
elif direction == 'y':
    for i in range(0,yblock):
        gen = t2generator(name = well + str(i), block = dat.grid.blocklist[i*xblock].name,gx = rate, type = compo, rate = rate)
        dat.add_generator(gen)
    

#gen = t2generator(name = 'wel 1', block = dat.grid.blocklist[0].name,gx = rate, type = 'WATE', rate = rate)
#gen2 = t2generator(name = 'wel 2', block = dat.grid.blocklist[5].name,gx = rate, type = 'WATE', rate = rate)
#gen3 = t2generator(name = 'wel 3', block = dat.grid.blocklist[8].name,gx = rate, type = 'WATE', rate = rate)
#gen4 = t2generator(name = 'wel 4', block = dat.grid.blocklist[9].name,gx = rate, type = 'WATE', rate = rate)
##gen2 = t2generator(name = 'wel 2', block = dat.grid.blocklist[0].name,
##                  ex = energy, type = 'HEAT',enthalpy=50000,gx = flow_rate)
#dat.add_generator(gen)
#dat.add_generator(gen2)
#dat.add_generator(gen3)
#dat.add_generator(gen4)

## Assign it to blocks below -100 m elevation:
#for blk in dat.grid.blocklist[1:]:
#    if blk.centre[2] <= -100: blk.rocktype = r2


# Write data file and (optional) VTK file for the grid, for 3D
# visualization:
dat.write('INFILE')
dat.write('flow.inp')
dat.grid.write_vtk(geo, 'INFILE.vtu')

"""
converting TOUGH file to TOUGHREACT using the TOUGHTOREACT class and moving from PYTOUGH to location for running
with chemical.inp and solute.inp files
"""

dest = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\VTK testing"

loc = r"C:\Users\tajayi3\Desktop\Research\Software\PyTOUGH-master"

filename = "flow.inp"

tre = toughtotoughreact(loc,dest,filename)

tre.converttotreact()

tre.copyfile(filename)

"""
changing directory to ensure it runs from the directory containing the chemical.inp and solute.inp files
"""
try:
    # Change the current working Directory    
    os.chdir(dest)
    print("... Directory changed ...")
    print("... Running simulation ... ")
except OSError:
    print("Can't change the Current Working Directory") 
    
"""
run the file in command window
"""
def run(inputfile):
    FNULL = open(os.devnull, 'w')    #use this if you want to suppress output to stdout from the subprocess

    args = "treacteos1.exe" + "<" + inputfile 
    print(args)
    subprocess.run(args, stdout=FNULL, stderr=FNULL, shell=True, check=True)

inputfile = 'flow.inp'
run(inputfile)
print ('...simulation complete...')


"""
copy files back to PYTOUGH folder for result treatments
"""
path = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\VTK testing"
dest = r"C:\Users\tajayi3\Desktop\Research\Software\PyTOUGH-master"
file_name = "kdd_conc.tec"
file_name2 = "MESH"
lookup = 'CONNE'
myList = ["kdd_concvtk.tec", "kdd_gasvtk.tec", "kdd_minvtk.tec", "kdd_timvtk.tec", "MESH"]
tre1 = prepfortoughreact(path,dest,myList,lookup)
tre1.copyallfiles()
tre1.writetofile()


"""
Graph Plotting
"""
with open('test.txt') as f:
    br3 = f.read().splitlines()

#tre = toughreact_tecplot('kdd_concvtk.tec',br3)

gridblock = br3[1]

width = 10
height = 4

parameters = ['pH','t_cl-','t_na+']
plotconc = flowreactionplotroutine(myList[0],br3,parameters)
plotconcbatch = batchreactionplotroutine(myList[0],br3,parameters)


param2 = ['calcite','csh(1.6)','portlandite']
plotmin = flowreactionplotroutine(myList[2],br3,param2)

plotconc.threeinone(width,height,br3)
plotconcbatch.threeinone(width,height,gridblock)











"""
---------------------------------------------
Former Plotting Routine
------------------------------------------------
#lst = t2listing('horiz1D.listing')
tre.last()
pH = tre.element['pH']
Pres = tre.element['P(bar)']
X = tre.element['X(m)']
Y = tre.element['Y(m)']
Z = tre.element['Z(m)']

xi,yi = np.meshgrid(X,Y)

zi = griddata((X,Y),pH,(xi,yi),method='nearest')
pi = griddata((X,Y),Pres,(xi,yi),method='nearest')

# plot
fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(2,2,1)
#levels = [-4, -3, -2, -1, 1, 2, 3, 4]
cs2 = plt.contourf(xi,yi,zi,10,  cmap='jet')  
plt.colorbar()
plt.xlabel('xi',fontsize=16)
plt.ylabel('yi',fontsize=16)
plt.tight_layout()


ax2 = fig.add_subplot(2,2,2)
cs = plt.contourf(xi,yi,pi,10,  cmap='jet')  
plt.colorbar()
#plt.plot(X,Y,'k.')
plt.xlabel('xi',fontsize=16)
plt.ylabel('yi',fontsize=16)
plt.tight_layout()
tre.write_vtk(geo, 'OUTFILE.pvd')

mf = tre.history([('  a 1','pH')])
time = mf[0]
pH= mf[1]

fig = plt.figure(figsize=(8,6)) 
ax1 = fig.add_subplot(1,1,1)
ax1.plot(time,pH,'r--', marker='x')
ax1.grid()
ax1.set_ylabel('pH')
ax1.set_xlabel('Time (seconds)')
plt.tight_layout()
"""