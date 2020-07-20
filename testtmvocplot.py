# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 18:27:48 2020

@author: AJ
"""

from tmvocplotting import *
from random import randrange

fileloc = r"C:\Users\AJ\Desktop\My Desktop\LSU\LSU-Corona\tmvoc\chen-5\test"
fileloc2 = r"C:\Users\AJ\Desktop\My Desktop\LSU\LSU-Corona\tmvoc\chen-5\no biodeg"
fileloc3=r"C:\Users\AJ\Desktop\My Desktop\LSU\LSU-Corona\tmvoc\chen-5"
fileloc4=r"C:\Users\AJ\Desktop\My Desktop\LSU\LSU-Corona\tmvoc\chen-5\test - onecomponent"
fileloc5 = r"C:\Users\AJ\Desktop\My Desktop\LSU\LSU-Corona\tmvoc\chen-5\test - onecomponent -changeyield"
fileloc6= r"C:\Users\AJ\Desktop\My Desktop\LSU\LSU-Corona\tmvoc\chen-5\test - onecomponent -changeyield - Case1"
fileloc7=r"C:\Users\AJ\Desktop\My Desktop\LSU\LSU-Corona\tmvoc\chen-5\test - onecomponent -changeyield - Case2"
fileloc8=r"C:\Users\AJ\Desktop\My Desktop\LSU\LSU-Corona\tmvoc\chen-5\test - onecomponent -changeyield - Case3"
fileloc9 = r"C:\Users\AJ\Desktop\My Desktop\LSU\LSU-Corona\tmvoc\mymodels\napl three phase"
fileloc10 = r"C:\Users\AJ\Desktop\My Desktop\LSU\LSU-Corona\tmvoc\mymodels\paper work"
fileloc11 = r"C:\Users\AJ\Desktop\My Desktop\LSU\LSU-Corona\tmvoc\mymodels\paper work\one component"
fileloc12 = r"C:\Users\AJ\Desktop\My Desktop\LSU\LSU-Corona\tmvoc\mymodels\paper work\one component\biodegradation"
fileloc12b=r"C:\Users\AJ\Desktop\My Desktop\LSU\LSU-Corona\tmvoc\mymodels\paper work\one component\no biodegradation"
fileloc13=r"C:\Users\AJ\Desktop\My Desktop\LSU\LSU-Corona\tmvoc\mymodels\paper work\one component\bio inject com1"
fileloc14=r"C:\Users\AJ\Desktop\My Desktop\LSU\LSU-Corona\tmvoc\mymodels\paper work\one component\batch no biodg"
fileloc15=r"C:\Users\AJ\Desktop\My Desktop\LSU\LSU-Corona\tmvoc\mymodels\paper work\one component\batch biodg"
fileloc16=r"C:\Users\AJ\Desktop\My Desktop\LSU\LSU-Corona\tmvoc\mymodels\paper work\one component\batch biodg - two biomass"
fileloc17=r"C:\Users\AJ\Desktop\My Desktop\LSU\LSU-Corona\tmvoc\mymodels\paper work\all components"
fileloc17b=r"C:\Users\AJ\Desktop\My Desktop\LSU\LSU-Corona\tmvoc\mymodels\paper work\all components\biodegradation"
file = 'OUTPUT_ELEME.csv'

plottmvoc = tmvocplotting(fileloc17b,file,50)
ma = plottmvoc.file_as_list

# times = plottmvoc.convert_times_year()
# time_index = plottmvoc.get_time_index()
# elements = plottmvoc.get_elements()
results = plottmvoc.resultdict()
params = ['X_toluen_N','X_toluen_L']
params1 = ['BIO1']
params2 = ['DEN_L','sat_N']
params3 = ['pres','den_N']
# get_pres_data = plottmvoc.get_timeseries_data('x', 59)
# press_spec = plottmvoc.get_element_data(1e12, 'z')
# test = np.asarray(press_spec)
# data = test.reshape(5,30)
# chop = plottmvoc.choplist(press_spec)

# diff = len(press_spec) - 10000
# for _ in range(diff):
#     ind = randrange(len(press_spec))
#     press_spec.pop(ind)  #a quick timing check suggests that `pop` is faster than `del`


# plottmvoc.plot_time('Pres', 40)
# plottmvoc.plot_time('den_g', 4)
# plottmvoc.multi_time_plot(params2, 0,style='vertical')
# plottmvoc.plot2D_one('DEN_L',1e8)
# plottmvoc.plot2D_one('X_n-DECA_L',1e8)
#plottmvoc.plot2D_withgrid('TEMP',0)

plottmvoc.multi_time_plot(params, 0,style='vertical')
plottmvoc.multi_time_plot(params1, 0,style='vertical')
# plottmvoc.multi_time_plot(params2, 0,style='vertical')
# plottmvoc.multi_time_plot(params3, 0,style='vertical')
# plottmvoc.plot2D_one('X_toluen_L',1e8)
# plottmvoc.plot2D_one('X_toluen_N',1e8)
# plottmvoc.plot2D_one('X_toluen_G',1e8)
# plottmvoc.plot2D_one('PRES',1e8)
