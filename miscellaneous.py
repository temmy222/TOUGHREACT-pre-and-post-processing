# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 21:36:03 2019

@author: tajayi3
"""

import matplotlib
import matplotlib.pyplot as plt
from t2listing import *
import numpy as np
import os
from scipy import interpolate
from scipy.interpolate import griddata
import random
import pandas as pd
import re

class miscellaneous(object):
    """
    This class helps in making plots for batch reactions carried out with TOUGHREACT
    
    """
    def __init__  (self,dest,file):
        
        """
        An instance of this class takes in two parameters;
        
        file --> the name of the file
        dest ---> where the file is located
        """
        self.dest = dest
        self.file = file
        os.chdir(dest)
        
    def slicing(self,pattern,array):
        many = []
        index = []
        for i in range(0,len(array)):
            if re.match(pattern, array[i]):
                many.append(array[i])
                index.append(i)
        return many, index
    
    def split(self,array):
        m = {}
        for i in range(0, len(array)):
            n = array[i].split()
            m[i] = n
        return m
    
    def getCompName(self,inputt):
        stre = []
        for i in range(0,len(inputt)):
            inputt[i][0].strip("'")
            stre.append(inputt[i][0])
        return stre
    
    def searchComp(self,compname,stre):
        stre = self.getCompName(stre)
        var2 = "'"
        compname = var2 +  compname + var2
        strep = []
        for i in range(0,len(stre)):
            if stre[i] == compname:
                strep.append(i)
        return strep
    
    def converttofloat(self,values):
        for i in range(0,len(values)):
            values[i] = float(values[i])
        return values
        
    def getComponents(self):
        os.chdir(self.dest)
        f = open(self.file, 'r')
        m = f.readlines()
        for i in range(len(m)-1, -1, -1) :
            if re.match(r'\s', m[i]):
                del m[i]
        pattern =r"[^'#]"
        pattern = r"['#]" # means string that contains any of ' or # (the [] means that)
        pattern2 = r'^#######'  # ^ is used to check if a string starts with a certain character. https://www.programiz.com/python-programming/regex
        nextpattern = r'[^#]' # means string that does not contain the #
        nextpattern2 = r'[^null]'
        
        listt, mache = self.slicing(pattern,m)
        many, index = self.slicing(pattern2,listt)
        
        aqueous = listt[index[1]+1:index[2]]
        mineral = listt[index[3]+1:index[4]]
        gas = listt[index[5]+1:len(listt)]

        aqueous2,num = self.slicing(nextpattern,aqueous)
        mineral2,num = self.slicing(nextpattern,mineral)
        gas2,num = self.slicing(nextpattern,gas)   
        
        aqueousfinal,num2 = self.slicing(nextpattern2,aqueous2)
        mineralfinal,num2 = self.slicing(nextpattern2,mineral2)
        gasfinal,num2 = self.slicing(nextpattern2,gas2) 
        
        gases = self.split(gasfinal)
        aqueouss = self.split(aqueousfinal)
        minerals = self.split(mineralfinal)
        
        return gases,aqueouss,minerals
    
    def plotGasK(self,compname):
        gases,aqueouss,minerals = self.getComponents()
        print(gases)
        pos = self.searchComp(compname,gases)
        temp = [0,25,60,100,150,200,250,300]
        fig = plt.figure(figsize=(10,5))
        values = gases[pos[1]][1:9]
        print(values)
        for i in range(0,len(values)):
            values[i] = float(values[i])
        plt.plot(temp,values)
        plt.grid()
        compname2 = list(compname.split(" "))
        plt.legend(compname2, prop={'size': 16})
        plt.xlabel('Temperature (Celsius) ',fontsize=14)
        plt.ylabel('Log of Equilibirum Constant',fontsize=14)
        fig.savefig('Equilibrium constant' +'.jpg',bbox_inches='tight',dpi=(600)) 
        
    def plotSpecieK(self,compname):
        gases,aqueouss,minerals = self.getComponents()
        pos = self.searchComp(compname,aqueouss)
        temp = [0,25,60,100,150,200,250,300]
        fig = plt.figure(figsize=(10,5))
        values = aqueouss[pos[1]][1:9]
        for i in range(0,len(values)):
            values[i] = float(values[i])
        plt.plot(temp,values)
        plt.grid()
        compname2 = list(compname.split(" "))
        plt.legend(compname2, prop={'size': 16})
        plt.xlabel('Temperature (Celsius) ',fontsize=14,fontweight='bold')
        plt.ylabel('Log of Equilibirum Constant',fontsize=14,fontweight='bold')
        plt.grid(True,which='both')
        plt.minorticks_on()
        plt.grid(b=True, which='major', linestyle='-', linewidth=0.5,color='k')
        plt.grid(b=True, which='minor', linestyle='-', linewidth=0.1)
        plt.spines['bottom'].set_linewidth(1.5)
        plt.spines['left'].set_linewidth(1.5)
        plt.spines['top'].set_linewidth(0.2)
        plt.spines['right'].set_linewidth(0.2)
        fig.savefig('Equilibrium constant' +'.jpg',bbox_inches='tight',dpi=(600)) 
        
    def plotMineralK(self,compname):
        gases,aqueouss,minerals = self.getComponents()
        pos = self.searchComp(compname,minerals)
        temp = [0,25,60,100,150,200,250,300]
        fig = plt.figure(figsize=(10,5))
        fig, axs = plt.subplots(1)
        values = minerals[pos[1]][1:9]
        for i in range(0,len(values)):
            values[i] = float(values[i])
        plt.plot(temp,values)
        compname2 = list(compname.split(" "))
        plt.legend(compname2, prop={'size': 16})
        plt.grid()
        plt.xlabel('Temperature (Celsius) ',fontsize=14,fontweight='bold')
        plt.ylabel('Log of Equilibirum Constant',fontsize=14,fontweight='bold')
        plt.grid(True,which='both')
        plt.minorticks_on()
        plt.grid(b=True, which='major', linestyle='-', linewidth=0.5,color='k')
        plt.grid(b=True, which='minor', linestyle='-', linewidth=0.1)
        axs.spines['bottom'].set_linewidth(1.5)
        axs.spines['left'].set_linewidth(1.5)
        axs.spines['top'].set_linewidth(0.2)
        axs.spines['right'].set_linewidth(0.2)
        fig.savefig('Equilibrium constant' +'.jpg',bbox_inches='tight',dpi=(600)) 
        
    def plotmultipleMineralK(self,compname):
        temp = [0,25,60,100,150,200,250,300]
        fig = plt.figure(figsize=(10,10))
        fig, axs = plt.subplots(1,1)
        markers = ["o","v","^","<",">","1","2","3","4","8","s","p","P","*","h","H","+","x","X","D","d","|","_"]
        if isinstance(compname, list):
            k=0
            for i in range(0,len(compname)):
                gases,aqueouss,minerals = self.getComponents()
                pos = self.searchComp(compname[i],minerals)
                values = minerals[pos[1]][1:9]
                value = self.converttofloat(values)
                plt.plot(temp,value,marker=markers[k],linewidth=2)
                plt.legend(compname, prop={'size': 9})
                k=k+1
            plt.grid()
            plt.xlabel('Temperature (Celsius) ',fontsize=14)
            plt.ylabel('Log of Equilibirum Constant',fontsize=14)
            plt.grid(True,which='both')
            plt.minorticks_on()
            plt.grid(b=True, which='major', linestyle='-', linewidth=0.5,color='k')
            plt.grid(b=True, which='minor', linestyle='-', linewidth=0.1)
            axs.spines['bottom'].set_linewidth(1.5)
            axs.spines['left'].set_linewidth(1.5)
            axs.spines['top'].set_linewidth(0.2)
            axs.spines['right'].set_linewidth(0.2)
            fig.savefig('Equilibrium constant' +'.jpg',bbox_inches='tight',dpi=(600)) 
            
            
        
