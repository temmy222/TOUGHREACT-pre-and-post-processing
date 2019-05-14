# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 15:25:32 2019

@author: tajayi3
"""

from t2listing import * 
from t2data import *
from math import log10
import numpy as np
import matplotlib.pyplot as plt
from t2listing import *
from mpl_toolkits.mplot3d import Axes3D
"""
read data
"""
with open('test.txt') as f:
    br3 = f.read().splitlines()

#edit results
tre = toughreact_tecplot('kdd_min.tec',br3)
trepermchange = toughreact_tecplot('kdd_min - Copy.tec',br3)
tre.last()
trepermchange.last()

t_h2o = tre.element['t_ca+2']
X = tre.element['X(m)']
Y = tre.element['Y(m)']
Z = tre.element['Z(m)']
X, Y = np.meshgrid(X, Y)
rblk = [blk[0] for blk in br3]
t_ca = tre.element['t_ca+2']

mf = tre.history([('A11 1','calcite')])
mfpermchange = trepermchange.history([('A11 1','calcite')])
time = mf[0]
t_ca= mf[1]
timepermchange = mfpermchange[0]
t_capermchange= mfpermchange[1]

mf1 = tre.history([('A11 1','portlandite')])
mf1permchange = trepermchange.history([('A11 1','portlandite')])
time1 = mf1[0]
pH= mf1[1]
pHpermchange= mf1permchange[1]

mf2 = tre.history([('A11 1','csh(1.6)')])
mf2permchange = trepermchange.history([('A11 1','csh(1.6)')])
time = mf2[0]
t_h= mf2[1]
t_hpermchange= mf2permchange[1]

fig = plt.figure(figsize=(11,13)) 
ax1 = fig.add_subplot(2,3,1)
ax1.plot(time1,pH,'r--', marker='x')
ax4 = ax1.twinx() 
ax4.plot(timepermchange,pHpermchange,'b--', marker='o')
#ax4.set_ylabel('sin')
ax1.grid()
ax1.set_ylabel('portlandite')
ax1.set_xlabel('Time (seconds)')
#ax1.legend(loc="upper right")
plt.legend(['Different Mineralogy','Different Mineralogy'], loc='upper left')
plt.tight_layout()


ax2 = fig.add_subplot(2,3,2)
#ax1.semilogx(rblk,T,'k--', marker='o')
ax2.plot(time,t_h,'r--', marker='x')
ax5 = ax2.twinx() 
ax5.plot(timepermchange,t_hpermchange,'b--', marker='o')
ax2.grid()
ax2.set_ylabel('csh(1.6)')
ax2.set_xlabel('Time (seconds)')
#ax2.legend(loc="upper right")
plt.legend(['Different Mineralogy'], loc='lower left')
plt.tight_layout()

ax3 = fig.add_subplot(2,3,3)
#ax1.semilogx(rblk,T,'k--', marker='o')
ax3.plot(time,t_ca,'r--', marker='x')
ax6 = ax3.twinx() 
ax6.plot(timepermchange,t_capermchange,'b--', marker='o')
ax3.grid()
ax3.set_ylabel('Calcite')
ax3.set_xlabel('Time (seconds)')
#ax3.legend(loc="upper right")
plt.legend(['Different Mineralogy','Different Mineralogy'], loc='upper left')
plt.tight_layout()

fig.savefig('mincompareplots.png',bbox_inches='tight') 
fig.savefig('mincompareplots.pdf')