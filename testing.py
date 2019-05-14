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

with open('test.txt') as f:
    br3 = f.read().splitlines()

tre = toughreact_tecplot('kdd_min.tec',br3)
tre.last()
t_h2o = tre.element['hydrotalcite']
X = tre.element['X(m)']
Y = tre.element['Y(m)']
Z = tre.element['Z(m)']

xi,yi = np.meshgrid(X,Y)

zi = griddata((X,Y),t_h2o,(xi,yi),method='linear')

# plot
fig = plt.figure()
ax = fig.add_subplot(111)
plt.contourf(xi,yi,zi)
#plt.plot(X,Y,'k.')
plt.xlabel('xi',fontsize=16)
plt.ylabel('yi',fontsize=16)