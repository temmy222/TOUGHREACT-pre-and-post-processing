# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 14:18:50 2018

@author: tajayi3
"""

"""Horizontal 1D model with temperatures and pressures specified at
each end. One end has two-phase conditions, the other single
phase. The script sets up the model, runs it, and produces a plot of
gas saturation along the model at the final time."""

from t2data import *
from t2listing import *

# --- set up the model ---------------------------------

length = 200.
nblks = 10
dx = [length / nblks] * nblks
dy = dz = [1.0]
geo = mulgrid().rectangular(dx, dy, dz)
geo.write('geom.dat')

# Create TOUGH2 input data file:
dat = t2data()
dat.title = 'Horizontal 1D example'
dat.grid = t2grid().fromgeo(geo)
dat.parameter.update(
    {'max_timesteps': 200,
     'tstop': 1.e10,
     'const_timestep': 100.,
     'print_interval': 20,
     'gravity': 9.81,
     'default_incons': [101.3e3, 20.]})
dat.start = True

# Set MOPs:
dat.parameter['option'][1] = 1
dat.parameter['option'][16] = 5

# add boundary condition block at each end:
bvol = 0.0
conarea = dy[0] * dz[0]
condist = 1.e-6

b1 = t2block('bdy01', bvol, dat.grid.rocktype['dfalt'])
dat.grid.add_block(b1)
con1 = t2connection([b1, dat.grid.blocklist[0]],
                    distance = [condist, 0.5*dx[0]], area = conarea)
dat.grid.add_connection(con1)

b2 = t2block('bdy02', bvol, dat.grid.rocktype['dfalt'])
dat.grid.add_block(b2)
con2 = t2connection([dat.grid.blocklist[nblks-1], b2],
                    distance = [0.5*dx[nblks-1], condist], area = conarea)
dat.grid.add_connection(con2)

# Set initial condition at x = 0:
dat.incon['bdy01'] = [None, [120.e3, 200.]]

dat.write('INFILE2')
dat.grid.write_vtk(geo, 'INFILE2.vtu')
dat.write('horiz1D.dat')

# --- run the model ------------------------------------

dat.run(simulator = 't2eos1')
dat.write('INFILE2')
dat.grid.write_vtk(geo, 'INFILE3.vtu')
lst = t2listing('horiz1D.listing')
lst.write_vtk(geo, 'OUTFILE.pvd', dat.grid)

# --- post-process the output ---------------------------

import matplotlib.pyplot as plt
lst = t2listing('horiz1D.listing')
lst.last()
# omit boundary blocks from the plot results:
x = [blk.centre[0] for blk in dat.grid.blocklist[:nblks]]
sg = lst.element['SG'][:nblks]
plt.plot(x, sg, 'o-')
plt.xlabel('x (m)'); plt.ylabel('Gas saturation')
plt.title('time: %6.2e s' %lst.time)
plt.show()