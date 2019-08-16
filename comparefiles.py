# -*- coding: utf-8 -*-
"""
Created on Fri May 10 20:34:58 2019

@author: tajayi3
"""
#from treactcompare import *
from prepfortoughreact import *
from batchreactionplotroutine import *
import matplotlib
import matplotlib.pyplot as plt
from t2listing import * 
import os
import pandas as pd
import random
loca1 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\VTK testing"
loca2 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Diffusion Testing"
loca3 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Cement Batch Reactions TOUGH Brine - Diffusion"
loca4 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Gulf of Mexico Sandstone Cement Flow - Onshore - GridTest"
loca5 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Gulf of Mexico Sandstone Cement Flow - Onshore - GridTest2"
loca6 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Gulf of Mexico Shale Cement Flow - Onshore"
loca7 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Paper Flow\Geometry Change\Gulf of Mexico Shale Cement Flow - Onshore"
#loca =[loca1,loca2,loca3]
loca =[loca4,loca5,loca7]
dest = r"C:\Users\tajayi3\Desktop\Research\Software\PyTOUGH-master"
files2 = ["kdd_concdiff.tec", "kdd_gasdiff.tec", "kdd_mindiff.tec", "kdd_timdiff.tec", "MESH"]
files1 = ["kdd_concvtk.tec", "kdd_gasvtk.tec", "kdd_minvtk.tec", "kdd_timvtk.tec", "MESH"]
files3 = ["kdd_conc.tec", "kdd_gas.tec", "kdd_min.tec", "kdd_tim.tec", "MESH"]
lookup = 'CONNE'
parameters = ['pH','t_ca+2','aH2O']
param2 = ['Permx(m^2)','Porosity','Permz(m^2)','calcite']
rep = 'Porosity'

#plotconclong = batchreactionplotroutine(files3[0],br3,parameters)
labels =['try1','try2','try3' ,'try4']

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
def retrievedata (locations,dest,files,gridblocknumber,indexa,prop):
    dictionary = {}
    lst = []
    lookup = 'CONNE'
    for i in range(0,len(locations)):
        tre1 = prepfortoughreact(locations[i],dest,files,lookup)
        tre1.copyallfiles()
        tre1.writetofile()
        os.chdir(dest)
        timer1 = 'first0'
        data1 = 'data0'
        with open('test.txt') as f:
            br3 = f.read().splitlines()
        tre=toughreact_tecplot(files[indexa],br3)
        tre.last()
        for j in range(0,len(param2)):
            if (timer1 or data1) not in lst:
                timer1 = 'first' + str(random.randint(1,101))
                data1 = 'data' + str(random.randint(1,101))
                lst.append(timer1)
                lst.append(data1)
            elif (timer1 or data1) in lst:
                timer1 = 'first' + str(random.randint(1,101)) + str(random.randint(1,101))
                data1 = 'data' + str(random.randint(1,101)) + str(random.randint(1,101))
                lst.append(timer1)
                lst.append(data1)
            mf = tre.history([(br3[gridblocknumber],prop[j])])
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

    # truncate large dataset
    for state, capital in dictionary.items():
        if len(dictionary[state][0]) > 100:
            dictionary[state][0] = dictionary[state][0][::20]

    # pick minimum time for analysis
    value1 = 10000000000000000000000000000000000000
    for state, capital in dictionary.items():
        if 'first' in state:
            manny = dictionary[state][0]
            value0 = manny[len(manny)-1]
            if value0 <= value1:
                value1 = value0
    return dictionary, lst, value1
    
    
def colorcoding(style):
    markers = ["o","v","^","<",">","1","2","3","4","8","s","p","P","*","h","H","+","x","X","D","d","|","_"]
    if style.lower()=='publication':
        colormarker = 'k' + markers[random.randint(0,(len(markers)-1))]
    elif style.lower()=='presentation':
        colormarker = 'r' + markers[random.randint(0,(len(markers)-1))]
    return colormarker
    
m,n,value1 = retrievedata(loca,dest,files3,2,2,param2)
    
    
def plotmulti (width,height,prop,linestyle='dashed'):
    font = {'family' : 'normal','weight' : 'bold','size'   : 14}
    matplotlib.rc('font', **font)
    dictionary,lst,value1 = retrievedata(loca,dest,files3,2,2,param2)
    fig = plt.figure(figsize=(width,height))
    kpansa = 0
    paralengthdouble = len(param2)*2
    for number in range(1,len(param2)+1):
        ax = fig.add_subplot(1,len(param2),number)
        for i in range(kpansa,len(dictionary),paralengthdouble):
            ax.plot(dictionary[lst[i]][0],dictionary[lst[i+1]][0],colorcoding('publication'),linestyle=linestyle,label=labels[number-1])
            ax.set_xlim((0,value1))
            ax.set_ylim((min(dictionary[lst[i]][0]),max(dictionary[lst[i+1]][0])))
        kpansa = kpansa+2
        ax.legend()
        ax.grid()
        ax.set_xlabel('Time (seconds)',fontsize=14,fontweight='bold')
        ax.set_ylabel(prop[number-1],fontsize=14,fontweight='bold')
        plt.tight_layout()
    os.chdir(loca[0])
    fig.savefig(labels[0] +'.jpg',bbox_inches='tight',dpi=(600))
    matplotlib.style.use('classic')
    
    
plotmulti(14,7,param2)
#dictionary = {}
#lst = []
#color = ['kd-.','','ko--','','ko--','','k>--','','k<:','','kx:','','kd-.','kd-.','','ko--','','ko--','','k>--','','k<:','','kx:','','kd-.']
#for i in range(0,len(loca)):
#    tre1 = prepfortoughreact(loca[i],dest,files3,lookup)
#    tre1.copyallfiles()
#    tre1.writetofile()
#    os.chdir(dest)
#    timer1 = 'first0'
#    data1 = 'data0'
#    with open('test.txt') as f:
#        br3 = f.read().splitlines()
#    tre=toughreact_tecplot(files3[0],br3)
#    tre.last()
#    for j in range(0,len(parameters)):
#        if (timer1 or data1) not in lst:
#            timer1 = 'first' + str(random.randint(1,101))
#            data1 = 'data' + str(random.randint(1,101))
#            lst.append(timer1)
#            lst.append(data1)
#        elif (timer1 or data1) in lst:
#            timer1 = 'first' + str(random.randint(1,101)) + str(random.randint(1,101))
#            data1 = 'data' + str(random.randint(1,101)) + str(random.randint(1,101))
#            lst.append(timer1)
#            lst.append(data1)
#        mf = tre.history([(br3[0],parameters[j])])
#        timerr = mf[0]
#        data= mf[1]
#        for index,character in enumerate(lst): 
#            if character not in dictionary.keys():
#                dictionary[character] = [] # because same character might be repeated in different positions
#        for index,character in enumerate(lst): 
#            if 'first' in character and len(dictionary[character]) == 0:
#                dictionary[character].append(timerr)
#            elif 'data' in character and len(dictionary[character]) == 0:
#                dictionary[character].append(data)
#
## truncate large dataset
#for state, capital in dictionary.items():
#    if len(dictionary[state][0]) > 100:
#        dictionary[state][0] = dictionary[state][0][::20]
#
## pick minimum time for analysis
#value1 = 10000000000000000000000000000000000000
#for state, capital in dictionary.items():
#    if 'first' in state:
#        manny = dictionary[state][0]
#        value0 = manny[len(manny)-1]
#        if value0 <= value1:
#            value1 = value0
#
#fig = plt.figure(figsize=(8,6))
#kpansa = 0
#paralengthdouble = len(parameters)*2
#mandy = (len(loca)*2)-1
#for number in range(1,len(parameters)+1):
#    ax = fig.add_subplot(1,3,number)
#    for i in range(kpansa,len(dictionary),paralengthdouble):
#        print(paralengthdouble)
#        print(kpansa)
#        ax.plot(dictionary[lst[i]][0],dictionary[lst[i+1]][0],color[i],label=labels[number-1])
#        ax.set_xlim((0,value1))
#    kpansa = kpansa+2
#    ax.legend()
#    ax.grid()
#    ax.set_xlabel('Time (seconds) ')
#    ax.set_ylabel(parameters[number-1])
#    plt.tight_layout()

