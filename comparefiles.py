# -*- coding: utf-8 -*-
"""
Created on Fri May 10 20:34:58 2019

@author: tajayi3
"""
#from treactcompare import *
from prepfortoughreact import *
import matplotlib.pyplot as plt
from t2listing import * 

loca1 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\VTK testing"
loca2 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Diffusion Testing"
loca3 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Cement Batch Reactions TOUGH Brine - Diffusion"
loca =[loca1,loca2,loca3]
dest = r"C:\Users\tajayi3\Desktop\Research\Software\PyTOUGH-master"
files2 = ["kdd_concdiff.tec", "kdd_gasdiff.tec", "kdd_mindiff.tec", "kdd_timdiff.tec", "MESH"]
files1 = ["kdd_concvtk.tec", "kdd_gasvtk.tec", "kdd_minvtk.tec", "kdd_timvtk.tec", "MESH"]
files3 = ["kdd_conc.tec", "kdd_gas.tec", "kdd_min.tec", "kdd_tim.tec", "MESH"]
lookup = 'CONNE'

def batchcompare (file1,file2,numbertocompare,gridblocks,index,prop,file3=None):
    if file3 != None:
        tre1 = toughreact_tecplot(file1[numbertocompare],gridblocks)
        tre2 = toughreact_tecplot(file2[numbertocompare],gridblocks)
        tre3 = toughreact_tecplot(file3[numbertocompare],gridblocks)
        mf1 = tre1.history([(gridblocks[index],prop)])
        mf2 = tre2.history([(gridblocks[index],prop)])
        mf3 = tre3.history([(gridblocks[index],prop)])
        time1 = mf1[0]
        var1= mf1[1]
        time2 = mf2[0]
        var2= mf2[1]
        time3 = mf3[0]
        var3= mf3[1]
        
        fig = plt.figure(figsize=(10,7))
        ax = fig.add_subplot(1,1,1)
        ax.plot(time1,var1)
        ax.plot(time2,var2)
        ax.plot(time3,var3)
        ax.grid()
        plt.tight_layout()
    else:
        tre1 = toughreact_tecplot(file1[numbertocompare],gridblocks)
        tre2 = toughreact_tecplot(file2[numbertocompare],gridblocks)
        mf1 = tre1.history([(gridblocks[index],prop)])
        mf2 = tre2.history([(gridblocks[index],prop)])
        time1 = mf1[0]
        var1= mf1[1]
        time2 = mf2[0]
        var2= mf2[1]
        fig = plt.figure(figsize=(10,7))
        ax = fig.add_subplot(1,1,1)
        ax.plot(time1,var1)
        ax.plot(time2,var2)
        ax.grid()
        plt.tight_layout()
        
tre1 = prepfortoughreact(loca1,dest,files1,lookup)
tre1.copyallfiles()


tre2 = prepfortoughreact(loca2,dest,files2,lookup)
tre2.copyallfiles()

tre3 = prepfortoughreact(loca3,dest,files3,lookup)
tre3.copyallfiles()

prop = 'pH'

with open('test.txt') as f:
    br3 = f.read().splitlines()

#masa =  treactcompare(loca1,dest,files1,files2)
batchcompare(files1,files2,0,br3,15,prop)

