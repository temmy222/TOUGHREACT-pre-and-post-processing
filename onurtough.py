from t2data import *
from math import log10
import matplotlib.pyplot as plt
from t2listing import *

# mesh parameters:
well_radius = 0.1
num_blocks = 200
midp = int(abs(num_blocks/2))
dr_min, dr_max = 0.1, 1.
layer_thickness = 1.
perm = 1.056e-13

dr = np.logspace(log10(dr_min), log10(dr_max), num_blocks)
dz = np.array([layer_thickness])
orig = np.array([well_radius, 0., 0.])

# create TOUGH2 input data:
dat = t2data()
dat.title = 'Radial model' 
dat.grid = t2grid().radial(dr, dz, origin = orig)
dat.grid.rocktype['dfalt'].permeability[:0] = perm
dat.grid.rocktype['dfalt'].permeability[:1] = perm
dat.grid.rocktype['dfalt'].permeability[:2] = perm
dat.grid.rocktype['dfalt'].porosity = 0.29
dat.grid.rocktype['dfalt'].conductivity = 3
dat.grid.rocktype['dfalt'].specific_heat = 962.96
dat.grid.rocktype['dfalt'].density = 2643.05

dat.parameter.update(
    {'const_timestep': 0.1,
     'max_timesteps': 9999,
     'tstop': 480 * 3600.,
     'print_interval': 1,
     'max_timestep': 5*3600,
     'gravity': 9.81,
     'default_incons': [13060000, 78.33]})
dat.parameter['option'][1] = 1
dat.parameter['option'][16] = 5
dat.parameter['option'][21] = 5
dat.multi = {'num_components': 1, 'num_equations' :2,'num_phases': 2,'num_secondary_parameters': 6}
#dat.generator= {'block', 'name', 'nseq', 'nadd', 'nads', 'ltab',
#                  '', 'type', 'itab', 'gx', 'ex', 'hg', 'fg'}
#dat.solver = {'type':5, '':None, 'z_precond':'Z3', '':None, 'o_precond':'O0', 'relative_max_iterations':0.1, 'closure':1e-10}
dat.start = True

# add generator:
tstop= 480 * 3600.
energy = 0.
shutintime = 120*3600
flow_rate = -0.00312822
flow_rate2 = 0.00312822
testtime = [0, shutintime ,tstop]
testrate = [flow_rate, 0,0]
testenthalpy = [energy,0,0]
gen = t2generator(name = 'wel 1', block = dat.grid.blocklist[midp].name,
  gx = flow_rate,ex=energy, type = 'COM1',ltab=3,itab = 3,time = testtime, rate = testrate, enthalpy = testenthalpy)
#gen2 = t2generator(name = 'wel 2', block = dat.grid.blocklist[0].name,
#                  ex = energy, type = 'HEAT',enthalpy=50000,gx = flow_rate)
dat.add_generator(gen)
#dat.add_generator(gen2)
dat.write('radial.dat')

# run the simulation:
dat.run(simulator = 't2eos1')
dat.write_history_generators('GOFT')
# plot pressure curve vs. radial distance:

lst = t2listing('radial.listing')
lst.last()
rblk = [blk.centre[0] for blk in dat.grid.blocklist]
P = lst.element['P'] / 1.e6
T = lst.element['T']
mf = lst.history([('e',dat.grid.blocklist[midp].name,'T')])
mf2 = lst.history([('e',dat.grid.blocklist[midp].name,'P')])
time = mf[0]
temperature = mf[1]
Pressure = mf2[1]
for i in range(0,len(time)):
    time[i] = time[i]/3600
    temperature[i] = temperature[i]+273.15
    Pressure[i] = Pressure[i]/1.e6
for i in range(0,len(T)):
    T[i] = T[i]+273.15




fig = plt.figure(figsize=(13,10)) 
#ax1 = fig.add_subplot(2,2,1)
##ax1.semilogx(rblk,T,'k--', marker='o')
#ax1.semilogx(rblk,T,'b--', marker='x')
#ax1.grid()
#plt.legend(['Temperature change with distance'], loc='upper right')
#ax1.set_ylabel('Temperature (K)')
#ax1.set_xlabel('Radius (m)')
#plt.title('Temperature at time ' + str(lst.time) + ' s')
#plt.tight_layout()

ax2 = fig.add_subplot(1,1,1)
ax2.plot(time,temperature,'r--', marker='x')
ax2.grid()
plt.legend(['Temperature change with time'], loc='upper left')
plt.tight_layout()
ax2.set_ylabel('Temperature (K)')
ax2.set_xlabel('Time (seconds)')
plt.title('Temperature Profile for duration of simulation',fontweight="bold")
plt.tight_layout() 
plt.savefig('TOUGH Temperature Plots.png',bbox_inches='tight') 
plt.savefig('TOUGH Temperature Plots.pdf') 



fig = plt.figure(figsize=(13,10)) 
ax1 = fig.add_subplot(2,2,1)
#ax1.semilogx(rblk,T,'k--', marker='o')
ax1.semilogx(rblk,P,'b--', marker='x')
ax1.grid()
plt.legend(['Pressure change with distance'], loc='upper right')
plt.tight_layout()
ax1.set_ylabel('Pressure (MPa)')
ax1.set_xlabel('Radius (m)')
plt.title('Pressure at time ' + str(lst.time) + ' s')
plt.tight_layout()

ax2 = fig.add_subplot(2,2,2)
ax2.plot(time,Pressure,'r--', marker='x')
ax2.grid()
plt.legend(['Pressure change with time'], loc='upper left')
plt.tight_layout()
ax2.set_ylabel('Pressure (K)')
ax2.set_xlabel('Time (seconds)')
plt.tight_layout()
plt.savefig('TOUGH Pressure Plots.png',bbox_inches='tight') 
plt.savefig('TOUGH Pressure Plots.pdf') 




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

