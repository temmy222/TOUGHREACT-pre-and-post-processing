# -*- coding: utf-8 -*-
"""
Created on Fri May 10 20:34:58 2019

@author: tajayi3
"""
#from treactcompare import *
from prepfortoughreact import *
from batchreactionplotroutine import *
import matplotlib.pyplot as plt
from t2listing import * 
import os
import pandas as pd
loca1 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\VTK testing"
loca2 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Diffusion Testing"
loca3 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Cement Batch Reactions TOUGH Brine - Diffusion"
loca4 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Gulf of Mexico Sandstone Cement Flow - Onshore - GridTest"
loca5 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Gulf of Mexico Sandstone Cement Flow - Onshore - GridTest2"
loca6 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Gulf of Mexico Shale Cement Flow - Onshore"
loca7 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Geometry Change\Gulf of Mexico Shale Cement Flow - Onshore"
#loca =[loca1,loca2,loca3]
loca =[loca4,loca5]
dest = r"C:\Users\tajayi3\Desktop\Research\Software\PyTOUGH-master"
files2 = ["kdd_concdiff.tec", "kdd_gasdiff.tec", "kdd_mindiff.tec", "kdd_timdiff.tec", "MESH"]
files1 = ["kdd_concvtk.tec", "kdd_gasvtk.tec", "kdd_minvtk.tec", "kdd_timvtk.tec", "MESH"]
files3 = ["kdd_conc.tec", "kdd_gas.tec", "kdd_min.tec", "kdd_tim.tec", "MESH"]
lookup = 'CONNE'
parameters = ['pH','t_ca+2','aH2O']
param2 = ['calcite','Porosity','microcline']
rep = 'Porosity'

#plotconclong = batchreactionplotroutine(files3[0],br3,parameters)
labels =['try1','try2','try3' ]

'''
def batchcompare (locations,dest,files,gridblocknumber,indexa,prop,labels):
    color = ['kd-.','','k+--','','ko--','','k>--','','k<:','','kx:','','kd-.']
    dictionary = {}
    lst = []
    for i in range(0,len(locations)):
        timer1 = 'first' + str(i)
        data1 = 'data' + str(i)
        lst.append(timer1)
        lst.append(data1)
        tre1 = prepfortoughreact(locations[i],dest,files,lookup)
        tre1.copyallfiles()
        tre1.writetofile()
        os.chdir(dest)
        with open('test.txt') as f:
            br3 = f.read().splitlines()
        tre=toughreact_tecplot(files[indexa],br3)
        tre.last()
        mf = tre.history([(br3[gridblocknumber],prop)])
        timerr = mf[0]
        data= mf[1]
        for index,character in enumerate(lst): 
            if character not in dictionary.keys():
                dictionary[character] = [] # because same character might be repeated in different positions
        for index,character in enumerate(lst): 
            if 'first' in character and len(dictionary[character]) == 0:
                dictionary[character].append(timerr)
            elif 'data' in character and len(dictionary[character]) == 0:
                dictionary[character].append(data)
                
    for state, capital in dictionary.items():
        if len(dictionary[state][0]) > 100:
            dictionary[state][0] = dictionary[state][0][::20]

    value1 = 10000000000000000000000000000000000000
    for state, capital in dictionary.items():
        if 'first' in state:
            manny = dictionary[state][0]
            value0 = manny[len(manny)-1]
            if value0 <= value1:
                value1 = value0
    
    for i in range(0,len(lst),2):
        plt.plot(dictionary[lst[i]][0],dictionary[lst[i+1]][0],color[i])
        plt.legend(labels)
    plt.grid()
    plt.xlabel('Time (seconds) ')
    plt.ylabel(prop)
#    return dictionary
  
batchcompare(loca,dest,files3,0,2,param2[1],labels)

'''


dictionary = {}
lst = []
color = ['kd-.','','ko--','','ko--','','k>--','','k<:','','kx:','','kd-.']
for i in range(0,len(loca)):
    tre1 = prepfortoughreact(loca[i],dest,files3,lookup)
    tre1.copyallfiles()
    tre1.writetofile()
    os.chdir(dest)
    with open('test.txt') as f:
        br3 = f.read().splitlines()
    tre=toughreact_tecplot(files3[0],br3)
    tre.last()
    for i in range(0,len(parameters)):
        timer1 = 'first' + str(i)
        data1 = 'data' + str(i)
        lst.append(timer1)
        lst.append(data1)
        mf = tre.history([(br3[0],parameters[i])])
        timerr = mf[0]
        data= mf[1]
        for index,character in enumerate(lst): 
            if character not in dictionary.keys():
                dictionary[character] = [] # because same character might be repeated in different positions
        for index,character in enumerate(lst): 
            if 'first' in character and len(dictionary[character]) == 0:
                dictionary[character].append(timerr)
            elif 'data' in character and len(dictionary[character]) == 0:
                dictionary[character].append(data)

for state, capital in dictionary.items():
    if len(dictionary[state][0]) > 100:
        dictionary[state][0] = dictionary[state][0][::20]

value1 = 10000000000000000000000000000000000000
for state, capital in dictionary.items():
    if 'first' in state:
        manny = dictionary[state][0]
        value0 = manny[len(manny)-1]
        if value0 <= value1:
            value1 = value0
        
fig = plt.figure(figsize=(8,6))
i = 0
for number in range(1,len(parameters)+1):
    ax = fig.add_subplot(1,3,number)
    ax.plot(dictionary[lst[i]][0],dictionary[lst[i+1]][0],color[i],label=labels[number-1])
    ax.legend()
    ax.grid()
    ax.set_xlabel('Time (seconds) ')
    ax.set_ylabel(parameters[number-1])
    i = i+2
    plt.tight_layout()
#        ax.xlim((0,value1))



#series = pd.Series(dictionary)
#masa = pd.DataFrame.from_dict(dictionary)
#fig = plt.figure(figsize=(10,7))
#ax = fig.add_subplot(1,1,1)
#plt.plot(series[0],series[1])
#plt.plot(series[2],series[3])
#plt.plot(series[4],series[5])
#plt.grid()
#plt.show()
#plt.tight_layout()            

#            e["mf{0}".format(i)] = 

#        tre2 = toughreact_tecplot(file2[numbertocompare],gridblocks)
#        tre3 = toughreact_tecplot(file3[numbertocompare],gridblocks)
#            mf+str(i) = tre1.history([(gridblocks[index],prop)])
#        mf2 = tre2.history([(gridblocks[index],prop)])
#        mf3 = tre3.history([(gridblocks[index],prop)])
#        time1 = mf1[0]
#        var1= mf1[1]
#        time2 = mf2[0]
#        var2= mf2[1]
#        time3 = mf3[0]
#        var3= mf3[1]
#        
#        fig = plt.figure(figsize=(10,7))
#        ax = fig.add_subplot(1,1,1)
#        ax.plot(time1,var1)
#        ax.plot(time2,var2)
#        ax.plot(time3,var3)
#        ax.grid()
#        plt.tight_layout()
#    else:
#        tre1 = toughreact_tecplot(file1[numbertocompare],gridblocks)
#        tre2 = toughreact_tecplot(file2[numbertocompare],gridblocks)
#        mf1 = tre1.history([(gridblocks[index],prop)])
#        mf2 = tre2.history([(gridblocks[index],prop)])
#        time1 = mf1[0]
#        var1= mf1[1]
#        time2 = mf2[0]
#        var2= mf2[1]
#        fig = plt.figure(figsize=(10,7))
#        ax = fig.add_subplot(1,1,1)
#        ax.plot(time1,var1)
#        ax.plot(time2,var2)
#        ax.grid()
#        plt.tight_layout()
#        
#tre1 = prepfortoughreact(loca1,dest,files1,lookup)
#tre1.copyallfiles()
#
#
#tre2 = prepfortoughreact(loca2,dest,files2,lookup)
#tre2.copyallfiles()
#
#tre3 = prepfortoughreact(loca3,dest,files3,lookup)
#tre3.copyallfiles()
#
#prop = 'pH'
#
#with open('test.txt') as f:
#    br3 = f.read().splitlines()
#
##masa =  treactcompare(loca1,dest,files1,files2)
#batchcompare(files1,files2,0,br3,15,prop)

