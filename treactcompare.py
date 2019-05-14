# -*- coding: utf-8 -*-
"""
Created on Fri May 10 13:22:21 2019

@author: tajayi3
"""
from t2listing import * 
import os
import shutil
import matplotlib.pyplot as plt
class treactcompare(object):
    def __init__ (self,locations,destination,filestocompare,parameter):
        self.destination = destination
        self.locations = locations
        self.filestocompare = filestocompare
        self.parameter = parameter

#with open('test.txt') as f:
#    br3 = f.read().splitlines()


    def copyfile(self,filename):
        #copy specific file
        for i in range(0,len(self.locations)):
            a = self.locations[i]
            src_files = os.listdir(a)
            for file_name in src_files:
                if file_name == filename:
                    full_file_name = os.path.join(a, file_name)
                if (os.path.isfile(full_file_name)):
                    shutil.copy(full_file_name, self.destination)
                
    def copyallfiles (self):
        #copy all files
        for i in range(0,len(self.filenames)):
            a = self.filenames[i]
            print ('...copying files...')
            self.copyfile(a)
            
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
            
            plt.plot(time1,var1)
            plt.plot(time2,var2)
            plt.plot(time3,var3)
        else:
            tre1 = toughreact_tecplot(file1[numbertocompare],gridblocks)
            tre2 = toughreact_tecplot(file2[numbertocompare],gridblocks)
            mf1 = tre1.history([(gridblocks[index],prop)])
            mf2 = tre2.history([(bgridblocks[index],prop)])
            time1 = mf1[0]
            var1= mf1[1]
            time2 = mf2[0]
            var2= mf2[1]
            plt.plot(time1,var1)
            plt.plot(time2,var2)

                

loca1 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\VTK testing"
loca2 = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Diffusion Testing"
loca =[loca1,loca2]
dest = r"C:\Users\tajayi3\Desktop\Research\Software\PyTOUGH-master"
files1 = ["kdd_concdiff.tec", "kdd_gasdiff.tec", "kdd_mindiff.tec", "kdd_timdiff.tec", "MESH"]
files2 = ["kdd_concvtk.tec", "kdd_gasvtk.tec", "kdd_minvtk.tec", "kdd_timvtk.tec", "MESH"]


            