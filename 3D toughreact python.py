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
from prepfortoughreact import *

path = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Cement Flow through 2 - Gherardi-Sea Water - PorPerm - Portlanditecalcite"
dest = r"C:\Users\tajayi3\Desktop\Research\Software\PyTOUGH-master"
file_name = "kdd_conc.tec"
file_name2 = "MESH"
lookup = 'CONNE'
myList = ["kdd_conc.tec", "kdd_gas.tec", "kdd_min.tec", "kdd_tim.tec", "MESH"]
tre1 = prepfortoughreact(path,dest,myList,lookup)
tre1.copyallfiles()
tre1.writetofile()


with open('test.txt') as f:
    br3 = f.read().splitlines()

tre = toughreact_tecplot('kdd_conc.tec',br3)
tre.last()
tre.next()
pH = tre.element['pH']
X = tre.element['X(m)']
Y = tre.element['Y(m)']
Z = tre.element['Z(m)']

xi,yi = np.meshgrid(X,Y)

zi = griddata((X,Y),pH,(xi,yi),method='nearest')

# plot
fig = plt.figure()
ax = fig.add_subplot(111)
#levels = [-4, -3, -2, -1, 1, 2, 3, 4]
cs = plt.contourf(xi,yi,zi,100,  cmap='jet')  

"""
Possible values are: 
Accent, Accent_r, Blues, Blues_r, BrBG, BrBG_r, BuGn, BuGn_r, BuPu, BuPu_r, 
CMRmap, CMRmap_r, Dark2, Dark2_r, GnBu, GnBu_r, Greens, Greens_r, Greys, Greys_r, 
OrRd, OrRd_r, Oranges, Oranges_r, PRGn, PRGn_r, Paired, Paired_r, Pastel1, Pastel1_r, 
Pastel2, Pastel2_r, PiYG, PiYG_r, PuBu, PuBuGn, PuBuGn_r, PuBu_r, PuOr, PuOr_r, PuRd, PuRd_r, 
Purples, Purples_r, RdBu, RdBu_r, RdGy, RdGy_r, RdPu, RdPu_r, RdYlBu, RdYlBu_r, RdYlGn, RdYlGn_r, 
Reds, Reds_r, Set1, Set1_r, Set2, Set2_r, Set3, Set3_r, Spectral, Spectral_r, Wistia, Wistia_r, YlGn, 
YlGnBu, YlGnBu_r, YlGn_r, YlOrBr, YlOrBr_r, YlOrRd, YlOrRd_r, afmhot, afmhot_r, autumn, autumn_r, 
binary, binary_r, bone, bone_r, brg, brg_r, bwr, bwr_r, cividis, cividis_r, cool, cool_r, coolwarm, 
coolwarm_r, copper, copper_r, cubehelix, cubehelix_r, flag, flag_r, gist_earth, gist_earth_r, gist_gray, 
gist_gray_r, gist_heat, gist_heat_r, gist_ncar, gist_ncar_r, gist_rainbow, gist_rainbow_r, gist_stern, 
gist_stern_r, gist_yarg, gist_yarg_r, gnuplot, gnuplot2, gnuplot2_r, gnuplot_r, gray, gray_r, hot, hot_r, 
hsv, hsv_r, inferno, inferno_r, jet, jet_r, magma, magma_r, nipy_spectral, nipy_spectral_r, ocean, ocean_r, 
pink, pink_r, plasma, plasma_r, prism, prism_r, rainbow, rainbow_r, seismic, seismic_r, spring, spring_r, s
ummer, summer_r, tab10, tab10_r, tab20, tab20_r, tab20b, tab20b_r, tab20c, tab20c_r, terrain, terrain_r, 
twilight, twilight_r, twilight_shifted, twilight_shifted_r, viridis, viridis_r, winter, winter_r

"""
#ax.set_ylabel('Temperature (K)')
#ax.set_xlabel('Time (seconds)')
# other cmaps are gray, winter, viridis, inferno,magma,autumn,Reds,'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
#'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
#'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn' https://matplotlib.org/tutorials/colors/colormaps.html
#cs.cmap.set_over('red')
#cs.cmap.set_under('blue')
#cs.changed()
plt.colorbar()
#plt.plot(X,Y,'k.')
plt.xlabel('xi',fontsize=16)
plt.ylabel('yi',fontsize=16)
plt.tight_layout()