from t2data import *
from scipy import *
from scipy import interpolate
from math import log10
import numpy as np
import matplotlib.pyplot as plt
from t2listing import *
import matplotlib as mpl
mpl.style.use('default')

# mesh parameters:
well_radius = 0.1
num_blocks = 50
midp = int(abs(num_blocks/2))
dr_min, dr_max = 0.001537416, 0.153270274
outerB = 500000
layer_thickness = 10.

dr1 = np.logspace(log10(dr_min), log10(dr_max), num_blocks)
dr2 = np.linspace(dr_max,outerB,500)
dr = np.concatenate((dr1,dr2),axis=0)
dz = np.array([layer_thickness])
orig = np.array([well_radius, 0., 0.])

# create TOUGH2 input data:
dat = t2data()
dat.title = 'Radial model' 
dat.grid = t2grid().radial(dr, dz, origin = orig)
dat.grid.rocktype['dfalt'].permeability[:0] = 9.869233e-15
dat.grid.rocktype['dfalt'].permeability[:1] = 9.869233e-15
dat.grid.rocktype['dfalt'].permeability[:2] = 9.869233e-15
dat.grid.rocktype['dfalt'].porosity = 0.3
dat.grid.rocktype['dfalt'].conductivity = 3
dat.grid.rocktype['dfalt'].specific_heat = 1000
dat.grid.rocktype['dfalt'].density = 2650

dat.parameter.update(
    {'const_timestep': 99,
     'max_timesteps': 9999,
     'print_interval': 1,
     'tstop': 31.25 * 86400,
#     'print_interval': 0.01,
#     'max_timestep': 8600,
     'gravity': 9.81,
     'default_incons': [100000, 150.]})
dat.parameter['option'][1] = 1
dat.parameter['option'][16] = 5
dat.parameter['option'][21] = 5
dat.multi = {'num_components': 1, 'num_equations' :2,'num_phases': 2,'num_secondary_parameters': 6}
#dat.generator= {'block', 'name', 'nseq', 'nadd', 'nads', 'ltab',
#                  '', 'type', 'itab', 'gx', 'ex', 'hg', 'fg'}
#dat.solver = {'type':5, '':None, 'z_precond':'Z3', '':None, 'o_precond':'O0', 'relative_max_iterations':0.1, 'closure':None}
dat.start = True

# add generator:
energy = 5.
shutintime = 6*3600
simtime = 31.25 * 86400
rate = 0.00920081019
flow_rate = 0.00920081019
testtime = [0, shutintime,simtime]
testrate = [0.00920081019, 0 ,0]
testenthalpy = [energy,0 ,0]
gen = t2generator(name = 'wel 1', block = dat.grid.blocklist[0].name,
  gx = flow_rate,ex=energy, type = 'COM1',ltab=3,itab = 3,time = testtime, rate = testrate, enthalpy = testenthalpy)
#gen2 = t2generator(name = 'wel 2', block = dat.grid.blocklist[0].name,
#                  ex = energy, type = 'HEAT',enthalpy=50000,gx = flow_rate)
dat.add_generator(gen)
#dat.add_generator(gen2)
dat.write('radial.dat')

# run the simulation:
dat.run(simulator = 't2eos1')

# plot pressure curve vs. radial distance:

lst = t2listing('radial.listing')
lst.last()
rblk = [blk.centre[0] for blk in dat.grid.blocklist]
P = lst.element['P'] / 1.e5
T = lst.element['T']


fig = plt.figure(figsize=(13,10)) 
ax1 = fig.add_subplot(2,2,1)
#ax1.semilogx(rblk,T,'k--', marker='o')
ax1.semilogx(rblk,T,'b--', marker='x')
ax1.grid()
plt.legend(['Temperature change with distance'], loc='center right')
plt.tight_layout()
ax1.set_ylabel('Temperature (K)')
ax1.set_xlabel('Radius (m)')
plt.title('Temperature at time ' + str(lst.time) + ' s')

ax2 = fig.add_subplot(2,2,2)
mf = lst.history([('e',dat.grid.blocklist[0].name,'T')])
mf2 = lst.history([('e',dat.grid.blocklist[0].name,'P')])
time = mf[0]
temperature = mf[1]
Pressure = mf2[1]
ax2.semilogx(time,temperature,'r--', marker='x')
ax2.grid()
plt.legend(['Temperature change with time'], loc='upper left')
plt.tight_layout()
ax2.set_ylabel('Temperature (K)')
ax2.set_xlabel('Time (seconds)')








#plt.semilogx(rblk, p, 'o-')
#plt.xlabel('Radius (m)')
#plt.ylabel('Pressure (bar)')
#plt.title('Pressure at time ' + str(lst.time) + ' s')
#plt.grid()
#plt.show()

#fig, ax1 = plt.subplots(figsize=(13,10))
#mf = lst.history([('e',dat.grid.blocklist[0].name,'T')])
#ax1.plot(timetest,prodtest,'k--', marker='o')
#ax1.plot(timetest2,prodtest2,'k:', marker='^')
#ax1.grid()
#plt.legend(['krw vs Sw', 'krow vs Sw'], loc='upper left')
#plt.tight_layout()
#ax1.set_ylabel('Cumulative Oil Production (m3)')
#ax1.set_xlabel('Time  (days)')
#fig.savefig('Prodplots.png',bbox_inches='tight') 
#fig.savefig('Prodplots.pdf')

