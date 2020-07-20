# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 20:45:34 2020

@author: AJ
"""

"""Constructing a TOUGH2 input data file for a simple 3D rectangular
model with two rocktypes and atmospheric boundary condition on top,
and an initial conditions file."""

from t2data import *
from t2incons import *
import numpy as np

# Create geometry- grid sizes are constant 1000 x 800 m horizontal,
# and 15 vertical layers increasing logarithmically in thickness from
# 10 m at surface to 100 m at bottom:
# dx = [1000.]*3
# dy = [800.]*4
# dz = np.logspace(1., 2., 5)
# geo = mulgrid().rectangular(dx, dy, dz)
xgridspacing = 100
ygridspacing = 1
zgridspacing = 6
xblock = 10
yblock = 1
zblock = 5
dx = [xgridspacing]*xblock
dy = [ygridspacing]*yblock
dz = [zgridspacing] *zblock

second = 1
minute = 60 * second
hour = 60 * minute
day = 24 * hour
year = 365. * day
year = float(year)

depthm = -91
depth = depthm * 3.281 #ft
simtime = 1000 * year

Temp = 30 #Centigrade
pressgrad = 0.465 #psi/ft
initP = abs(pressgrad*depth* 6894.76)


geo = mulgrid().rectangular(dx, dy, dz,origin=[0., 0., depthm])
#geo = mulgrid().rectangular(dx, dy, dz,origin=[0., 0., 0.])
geo.write('geom.dat')
incond = [initP, Temp]

# Create TOUGH2 input data file:
dat = t2data()
dat.title = 'For TMVOC'
dat.grid = t2grid().fromgeo(geo)
dat.parameter.update(
    {'max_timesteps': 9999,
     'tstop': simtime,
     'const_timestep': 1,
     'print_interval': 20,
     'gravity': 9.81,
     'max_timestep': 8640,
     'relative_error': 0.000001,
     'default_incons': incond})
dat.start = True

# Set MOPs:
dat.parameter['option'][1] = 1
dat.parameter['option'][16] = 5

# Set relative permeability (Corey) and capillarity functions:
dat.relative_permeability = {'type': 6, 'parameters': [0.15, 0.05, 0.01, 3., 0.]}
dat.capillarity = {'type':6 , 'parameters': [0., 0.25, 1., 0., 0.]}

# add generator:
energy = 5.
shutintime = 0.2 * year
testtime = [0, shutintime,simtime]
injrate = [6e-08,0 ,0]
energyrate =[0,0,0]
total_components = 6
compo = 'COM'
j = 0
num_well = 5
wellnames=[]
blocks =[]

"""
in generator block

name is the name given to the well at that block
block is which the grid block it is going to be located
type is the component type e.g compo here is COM so if i is 3 then it is component 3
ltab is the number of times for well rate activity changes starting from 0 and end time
itab is for changes in well enthalpies
"""
indexa = (xblock) -1

# create wells
for i in range(num_well):
    wellnames.append('INJ'+str(i))
    
for j in range(0,xblock,2):
    blocks.append(dat.grid.blocklist[j].name)
    
# print(indexa)
    
# blocks.append('  j 1')
j=1    
for i in range(0,len(wellnames)):
    for k in range(total_components):
        gen = t2generator(name = 'INJ'+str(j), block = blocks[i], type = compo+str(k+3), ltab=3,itab = 3,time = testtime, rate = injrate, enthalpy = energyrate)
        dat.add_generator(gen)
        j=j+1
# j=0
# for i in range(0,xblock):
#     gen = t2generator(name = 'INJ'+str(j), block = dat.grid.blocklist[j].name, type = compo+str(3), ltab=3,itab = 3,time = testtime, rate = injrate, enthalpy = energyrate)
#     dat.add_generator(gen)
#     j=j+1
    
    
# for i in range(total_components):
#     gen = t2generator(name = 'INJ'+str(i), block = dat.grid.blocklist[j].name, type = compo+str(3), ltab=3,itab = 3,time = testtime, rate = injrate, enthalpy = energyrate)
#     dat.add_generator(gen)
#     j=j+1

#gen = t2generator(name = 'PRO'+str(i), block = dat.grid.blocklist[indexa+1].name, type = compo+str(3), ltab=0,itab = 0, gx = -9.2E-9)
#dat.add_generator(gen)
# Add a second rocktype, with anisotropic permeability:
#r2 = rocktype('rock2', permeability = [0.6e-15]*2 + [0.3e-15])
#dat.grid.add_rocktype(r2)
# Assign it to blocks below -100 m elevation:
#for blk in dat.grid.blocklist[1:]:
 #   if blk.centre[2] <= -100: blk.rocktype = r2

# (Note: we skipped the first block (dat.grid.blocklist[0]) which is
# the atmosphere and has no centre defined)

# Write data file and (optional) VTK file for the grid, for 3D
# visualization:
# dat.write('INFILE')
# dat.grid.write_vtk(geo, 'INFILE.vtu')

# Set up and write initial conditions file with approximate
# hydrostatic pressure profile:
# inc = dat.grid.incons()
# rho = 998.
# g = 9.8
# P0 = dat.parameter['default_incons'][0]
# T0 = dat.parameter['default_incons'][1]
# for blk in dat.grid.blocklist:
#     # get depth if block centre is defined-
#     # otherwise use zero (atmosphere block)
#     h = -blk.centre[2] if blk.centre is not None else 0.
#     P = P0 + rho * g * h
#     T = T0
#     inc[blk.name].variable = [P, T]
# inc.write('INCON')

dat.write('tmvoc.dat')