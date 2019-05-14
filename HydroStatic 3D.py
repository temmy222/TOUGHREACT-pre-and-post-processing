# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 18:05:28 2018

@author: tajayi3
"""

"""Constructing a TOUGH2 input data file for a simple 3D rectangular
model with two rocktypes and atmospheric boundary condition on top,
and an initial conditions file."""

from t2data import *
from t2incons import *

# Create geometry- grid sizes are constant 1000 x 800 m horizontal,
# and 15 vertical layers increasing logarithmically in thickness from
# 10 m at surface to 100 m at bottom:
dx = [1000.]*10
dy = [800.]*12
dz = np.logspace(1., 2., 15)
geo = mulgrid().rectangular(dx, dy, dz, atmos_type = 0)
geo.write('geom.dat')

# Create TOUGH2 input data file:
dat = t2data()
dat.title = 'Hydrostatic 3D example'
dat.grid = t2grid().fromgeo(geo)
dat.parameter.update(
    {'max_timesteps': 999,
     'tstop': 1.e14,
     'const_timestep': 1.e7,
     'print_interval': 20,
     'gravity': 9.81,
     'default_incons': [101.3e3, 20.]})
dat.start = True

# Set MOPs:
dat.parameter['option'][1] = 1
dat.parameter['option'][16] = 5

# Set relative permeability (Corey) and capillarity functions:
dat.relative_permeability = {'type': 3, 'parameters': [0.3, 0.1, 0., 0., 0.]}
dat.capillarity = {'type': 1, 'parameters': [0., 0., 1., 0., 0.]}

# Add a second rocktype, with anisotropic permeability:
r2 = rocktype('rock2', permeability = [0.6e-15]*2 + [0.3e-15])
dat.grid.add_rocktype(r2)
# Assign it to blocks below -100 m elevation:
for blk in dat.grid.blocklist[1:]:
    if blk.centre[2] <= -100: blk.rocktype = r2

# (Note: we skipped the first block (dat.grid.blocklist[0]) which is
# the atmosphere and has no centre defined)

# Write data file and (optional) VTK file for the grid, for 3D
# visualization:
dat.write('INFILE')
dat.grid.write_vtk(geo, 'INFILE.vtu')

# Set up and write initial conditions file with approximate
# hydrostatic pressure profile:
inc = dat.grid.incons()
rho = 998.
g = 9.8
P0 = dat.parameter['default_incons'][0]
T0 = dat.parameter['default_incons'][1]
for blk in dat.grid.blocklist:
    # get depth if block centre is defined-
    # otherwise use zero (atmosphere block)
    h = -blk.centre[2] if blk.centre is not None else 0.
    P = P0 + rho * g * h
    T = T0
    inc[blk.name].variable = [P, T]
inc.write('INCON')