# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 13:53:14 2018

@author: tajayi3
"""

from t2grids import *
geo = mulgrid().rectangular([500]*20, [1000], [100]*20, atmos_type = 0,
convention = 2)
geo.write('2Dgrd.dat')
grid = t2grid().fromgeo(geo)
grid.add_rocktype(rocktype('greyw', permeability = [1.e-15]*2 + [0.1e-15]))
grid.add_rocktype(rocktype('fill ', permeability = [15.e-15]*2 + [5.e-15]))
for blk in grid.blocklist[1:]:
    if 200 <= blk.centre[0] <= 400: blk.rocktype = grid.rocktype['fill ']
    else: blk.rocktype = grid.rocktype['greyw']