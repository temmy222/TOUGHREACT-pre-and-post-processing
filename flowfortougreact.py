# -*- coding: utf-8 -*-
"""
Created on Wed May 22 12:45:11 2019

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

dest = r"C:\Users\AJ\Desktop\flow through"

loc = r"C:\Users\AJ\Desktop\My Desktop\LSU\LSU-Corona\PyTOUGH-master"

try:
    # Change the current working Directory    
    os.chdir(dest)
    print("... Directory changed ...")
except OSError:
    print("Can't change the Current Working Directory") 
    
"""
flow input files with mulgrid as a template to facilitate writing to pvd for viewing with paraview
"""

xblock = 20
yblock = 1
zblock = 8

second = 1
minute = 60 * second
hour = 60 * minute
day = 24 * hour
year = 365. * day
year = float(year)
xgridspacing = 0.001
ygridspacing = 0.1
zgridspacing = 0.001
dx = [xgridspacing]*xblock
dy = [ygridspacing]*yblock
dz = [zgridspacing] *zblock
simtime = 200 * day


    
rock = 'cement'
rocknext = 'sands'
depth = 10032.81 #feet
depth = 0
depthm = depth * 0.3048
depthm = 5090
depthm = 0
depth = depthm * 3.281
Temp = 170 #Centigrade
Temp = 50
pressgrad = 0.7 #psi/ft

if rock.lower() == 'sandstone':
    k1 = k2 = k3 = 6.51E-15
elif rock.lower() == 'shale':
    k1 = k2 = k3 = 6.51E-17
elif rock.lower() == 'cement':
    k1 = k2 = k3 = 6.51E-19

initP = pressgrad*depth* 6894.76
initP = 10000000

incond = [initP, Temp]
geo = mulgrid().rectangular(dx, dy, dz,origin=[0., 0., -depthm])
geo.write('geom2.dat')

# Testing Mulgrid for toughreact
dat = t2data()
dat.title = 'TOUGHREACT FILE'
dat.grid = t2grid().fromgeo(geo)
dat.parameter.update(
    {'max_timesteps': 9999,
     'tstop': simtime,
     'const_timestep': 1,
     'print_interval': 2000,
     'gravity':  9.81,
     'max_timestep': 8640,
     'relative_error': 0.000001,
     'print_block': '  a 1',
     'default_incons': incond})
dat.start = True

dat.grid.rocktype['dfalt'].permeability = [k1,k2,k3]

#dat.grid.rocktype['dfalt'].permeability[:0] = 6.51E-19
#dat.grid.rocktype['dfalt'].permeability[:1] = 6.51E-19
#dat.grid.rocktype['dfalt'].permeability[:2] = 6.51E-19
#dat.grid.rocktype['dfalt'].nad = 1  # if nad is made greater or equal to 1, it can take the second row for rocks
dat.grid.rocktype['dfalt'].porosity = 0.27


if rocknext.lower() == 'sands':
    k1 = k2 = k3 = 6.51E-15

k_shale= 6.51E-17
k_carbonate = 6.51E-16

conductivity = 1.5
specific_heat = 900
r2 = rocktype('sands',0,2600, 0.27,[k1, k2, k3],conductivity,specific_heat)  # how to add another rocktype
r3 = rocktype('shale',0,2600, 0.27,[k_shale, k_shale, k_shale],conductivity,specific_heat) 
r4 = rocktype('carbo',0,2600, 0.27,[k_carbonate, k_carbonate, k_carbonate],conductivity,specific_heat) 
dat.grid.add_rocktype(r2)
dat.grid.add_rocktype(r3)
dat.grid.add_rocktype(r4)
# how to add the rocktype to specific gridblocks in the model

for blk in dat.grid.blocklist[0:]:
    if blk.centre[0] > 2.500e-01 and blk.centre[2] <= -5091 and blk.centre[2] >= -5093 : blk.rocktype = r3  
    if blk.centre[0] > 2.500e-01 and blk.centre[2] <= -5093 and blk.centre[2] >= -5095 : blk.rocktype = r2 
    if blk.centre[0] > 2.500e-01 and blk.centre[2] <= -5095 and blk.centre[2] >= -5097 : blk.rocktype = r3 
    if blk.centre[0] > 2.500e-01 and blk.centre[2] <= -5097 and blk.centre[2] >= -5097 : blk.rocktype = r4



# Set MOPs:
dat.parameter['option'][1] = 0     # MOP for printouts
dat.parameter['option'][16] = 4    # MOP for automatic time step control
dat.parameter['option'][21] = 5   # MOP for linear solver
dat.parameter['option'][18] = 1   # MOP for upstram weighting

# Set relative permeability (Corey) and capillarity functions:
dat.relative_permeability = {'type': 3, 'parameters': [0.3, 0.1, 0., 0., 0.]}
dat.capillarity = {'type': 1, 'parameters': [0., 0., 1., 0., 0.]}
dat.multi = {'num_components': 1, 'num_equations' :1,'num_phases': 2,'num_secondary_parameters': 6}

# add boundary condition block at each end:
#bvol = 1000000000
lastgrid = (xblock * yblock * zblock) - 1
dat.grid.blocklist[lastgrid].volume = 10**9
#conarea = dy[0] * dz[0]
#condist = 1.e-6
#
#b1 = t2block('bdy01', bvol, dat.grid.rocktype['dfalt'])
#dat.grid.add_block(b1)
#con1 = t2connection([b1, dat.grid.blocklist[0]],
#                    distance = [condist, 0.5*dx[0]], area = conarea)
#dat.grid.add_connection(con1)

# add generator:
energy = 5.
shutintime = 0.25 * year
shutintime2 = 0.5 * year
rate = 9.20081019e-9
rate2 = -9.20081019e-9
totalratetime = 20
testenthalpy = [energy,0 ,0,0]
testtime = [0, shutintime,shutintime2,simtime]
testtime2 = np.linspace(0,simtime,totalratetime)
testrate = [0.00920081019,0.001, 0 ,0]
testrate2 = [-0.00920081019,-0.001, 0 ,0]
well = 'wl '
compo = 'WATE'
compo2 = 'MASS'
direction = 'x'
injectionrate =[]
productionrate =[]
energyrate = []


# intermittent injection
# for i in range(0,totalratetime):
#     if i%2 ==0:
#         injectionrate.append(rate)
#         productionrate.append(rate)
#         energyrate.append(5)
#     else:
#         injectionrate.append(0)
#         productionrate.append(rate2)
#         energyrate.append(5)

# constant injection
for i in range(0,totalratetime):
    injectionrate.append(rate)
    productionrate.append(rate)
    energyrate.append(5)

if direction == 'x':
    for i in range(75,99):
#        if i%5 == 0:
            gen = t2generator(name = well + str(i), block = dat.grid.blocklist[i].name, type = compo, ltab=totalratetime,itab = 3,time = testtime2, rate = injectionrate, enthalpy = energyrate)
            dat.add_generator(gen)
#            dat.grid.blocklist[i].volume = 1000000000
#        elif i == xblock-1:
#            gen = t2generator(name = well + str(i), block = dat.grid.blocklist[i].name,gx = rate2, ex=0.5, type = compo2)
#            dat.add_generator(gen)
#        else:
#            gen = t2generator(name = well + str(i), block = dat.grid.blocklist[i].name,gx = rate, type = compo, ltab=4,itab = 3,time = testtime, rate = testrate2, enthalpy = testenthalpy)
#            dat.add_generator(gen)           
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

dest = r"C:\Users\AJ\Desktop\vtk testing"

loc = r"C:\Users\AJ\Desktop\My Desktop\LSU\LSU-Corona\PyTOUGH-master"

#dest = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\VTK testing"

#loc = r"C:\Users\tajayi3\Desktop\Research\Software\PyTOUGH-master"

filename = "flow.inp"

tre = toughtotoughreact(loc,dest,filename)

tre.converttotreact()

tre.copyfile(filename)
