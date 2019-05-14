# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 19:31:59 2018

@author: tajayi3
"""

from t2data import *
from math import log10

# mesh parameters:
well_radius = 0.1
num_blocks = 30
dr_min, dr_max = 0.1, 1000.
layer_thickness = 10.

dr = np.logspace(log10(dr_min), log10(dr_max), num_blocks)
dz = np.array([layer_thickness])
orig = np.array([well_radius, 0., 0.])

# create TOUGH2 input data:
dat = t2data()
dat.title = 'Radial model' 
dat.grid = t2grid().radial(dr, dz, origin = orig)
dat.grid.rocktype['dfalt'].permeability[:2] = 50.e-15
dat.parameter.update(
    {'const_timestep': 0.1,
     'max_timesteps': 1000,
     'tstop': 6. * 3600.,
     'print_interval': 20,
     'gravity': 9.81,
     'default_incons': [3.e5, 20.]})
dat.parameter['option'][1] = 1
dat.parameter['option'][16] = 5
dat.start = True

# add generator:
flow_rate = -0.1
gen = t2generator(name = 'wel 1', block = dat.grid.blocklist[0].name,
                  gx = flow_rate, type = 'MASS')
dat.add_generator(gen)
dat.write('radial.dat')

# run the simulation:
dat.run(simulator = 't2eos1')

# plot pressure curve vs. radial distance:
import matplotlib.pyplot as plt
from t2listing import *
lst = t2listing('radial.listing')
lst.last()
rblk = [blk.centre[0] for blk in dat.grid.blocklist]
p = lst.element['P'] / 1.e5
plt.semilogx(rblk, p, 'o-')
plt.xlabel('Radius (m)')
plt.ylabel('Pressure (bar)')
plt.title('Pressure at time ' + str(lst.time) + ' s')
plt.show()