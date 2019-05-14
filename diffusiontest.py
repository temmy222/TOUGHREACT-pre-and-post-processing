# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:44:31 2019

@author: tajayi3
"""
from t2data import *
from t2incons import *
from toughtotreact import *
from t2listing import * 
from t2grids import *
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
from treactcompare import *
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
dat.grid.rocktype['dfalt'].nad = 1  # if nad is made greater or equal to 1, it can take the second row for rocks
dat.grid.rocktype['dfalt'].tortuosity = 0.9
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
    

##gen2 = t2generator(name = 'wel 2', block = dat.grid.blocklist[0].name,
##                  ex = energy, type = 'HEAT',enthalpy=50000,gx = flow_rate)


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

dest = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Diffusion Testing"

loc = r"C:\Users\tajayi3\Desktop\Research\Software\PyTOUGH-master"

filename = "flow.inp"

tampo = toughtotoughreact(loc,dest,filename)

tampo.converttotreact()

tampo.copyfile(filename)

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
file_name = "kdd_concdiff.tec"
file_name2 = "MESH"
lookup = 'CONNE'
myList = ["kdd_concdiff.tec", "kdd_gasdiff.tec", "kdd_mindiff.tec", "kdd_timdiff.tec", "MESH"]
tre1 = prepfortoughreact(dest,loc,myList,lookup)
tre1.copyallfiles()
tre1.writetofile()


"""
Graph Plotting
"""
with open('test.txt') as f:
    br3 = f.read().splitlines()

tre = toughreact_tecplot('kdd_concdiff.tec',br3)

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
mff = tre.history([('  a 1','t_na+')])
time2 = mff[0]
t_na= mff[1]
time = mf[0]
pH= mf[1]
t_na = np.log10(t_na)

fig = plt.figure(figsize=(8,6)) 
ax1 = fig.add_subplot(2,2,1)
ax1.plot(time,pH,'r--', marker='x')
ax1.grid()
ax1.set_ylabel('pH')
ax1.set_xlabel('Time (seconds)')
plt.tight_layout()


ax1 = fig.add_subplot(2,2,2)
ax1.plot(time2,t_na,'r--', marker='x')
ax1.grid()
ax1.set_ylabel('t_na')
ax1.set_xlabel('Time (seconds)')
plt.tight_layout()