# -*- coding: utf-8 -*-
"""
Created on Tue May  7 18:12:44 2019

@author: tajayi3
"""

import os
import shutil
import itertools
from prepfortoughreact import *
"""
copy files function
"""


path = r"D:\Working-folder - Ajayi\my TOUGHREACT$TOUGH Simulations\Moving Forward\Cement Flow through 2 - Gherardi-Sea Water - PorPerm"
dest = r"D:\Working-folder - Ajayi\Software\PyTOUGH-master"
file_name = "kdd_conc.tec"
file_name2 = "MESH"
lookup = 'CONNE'
myList = ["kdd_conc.tec", "kdd_gas.tec", "kdd_min.tec", "kdd_tim.tec", "MESH"]
tre = prepfortoughreact(path,dest,myList,lookup)
tre.copyallfiles()
tre.writetofile()