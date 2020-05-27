from prepfortoughreact import *
from batchreactionplotroutine import *
from multiplotroutine import *
import matplotlib
import matplotlib.pyplot as plt
from t2listing import * 
import os
import pandas as pd
import random
from crossplotmultiroutine import *


files = ["kdd_conc.tec", "kdd_gas.tec", "kdd_min.tec", "kdd_tim.tec", "MESH"]
filecheck = ["kdd_conc.tec", "kdd_gas.tec", "kdd_min.tec"]
loca21=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - same low cond  - longer time"
loca22=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - Ca injected sand equil brine Onshore - same low cond - longer time"
loca23 = r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - Na acetate sand equil injected Onshore - same low cond  - longer time"
loca24=r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - same low cond"


loca28 = r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer time"
loca29 = r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - Ca injected sand equil brine Onshore - longer time"
loca30 = r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - Na acetate sand equil injected Onshore - longer time"
loca31 = r"C:\Users\AJ\OneDrive - Louisiana State University\Increased depth\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - longer"

loca =[loca28,loca29,loca30,loca31]
dest = r"C:\Users\AJ\Desktop\My Desktop\LSU\LSU-Corona\PyTOUGH-master"


param6 = ['brucite','chalcedony','dolomite','pH']

masa2 = crossplotmultiroutine(loca,dest,files,0,2,param6)
# lista = masa2.getparam()
# masaaa = masa2.get_dict_for_params()
# letsee = masa2.find_file_for_param2('brucite')
labels =['Ca Offshore (Case 4)','Ca onshore (Case 3)','Na acetate (Case 2)','NaCl (Case 1)','NaCl Same','More Ca','More HCO3']
# dictionary,lst,value1 = masa2.retrievedatamulti(loca,dest,files,0,0,param6)
masa2.plotmultimulti(labels,purpose='presentation',style='multiple')


# dictionary = {}
# lst = []
# lookup = 'CONNE'
# tre1 = prepfortoughreact(loca21,dest,files,lookup)
# tre1.copyallfiles()
# tre1.writetofile()
# os.chdir(dest)
# with open('test.txt') as f:
#     br3 = f.read().splitlines()

# for file in filecheck:  
#     tre=toughreact_tecplot(file,br3)
#     tre._file.seek(0)
#     line  = tre.skipto(['VARIABLES', 'Variables', 'variables'])
#     eqpos = line.find('=')
#     sep = ',' if ',' in line else None
#     rawcols = line[eqpos+1:].strip().split(sep)
#     cols = []
#     for col in rawcols:
#         colstrip = col.strip()
#         if colstrip:
#             if col.startswith('"') and col.endswith('"'):
#                 cols.append(col[1:-1].strip())
#             else:
#                 cols.append(colstrip)
#     dictionary[file]=cols



# final={}
# for i in range(len(param6)):
#     for j in range(len(filecheck)):
#         if param6[i] in dictionary[filecheck[j]]:
#             if filecheck[j] in final.keys():
#                 final[filecheck[j]].append(param6[i])
#             else:
#                 final[filecheck[j]] = [param6[i]]
# for file in files:
#     i=0
#     if param6[i] in cols:
#         dictionary[file]=param6[i]
#     i=i+1