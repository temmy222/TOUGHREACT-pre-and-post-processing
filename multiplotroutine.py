# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 15:46:42 2019

@author: tajayi3
"""

import matplotlib.pyplot as plt
from t2listing import * 
import os
import random
import pandas as pd
import matplotlib
from prepfortoughreact import *

class multiplotroutine(object):
    """
    This class helps in making plots for batch reactions carried out with TOUGHREACT
    
    """
    def __init__  (self,locations,dest,files,gridblocknumber,indexa,prop):
        
        """
        An instance of this class takes in three parameters;
        
        filename --> the output file to be interpreted (in tecplot format) e.g. kddconc.tec
        gridblock ---> the total number of gridblocks in the simulations 
        parameters -> parameters to be investigated (should be in a python list) e.g. ['pH','t_na+','t_ca2+']
        """
        self.locations = locations
        self.dest = dest
        self.files = files
        self.gridblocknumber = gridblocknumber
        self.indexa = indexa
        self.prop = prop
        
    def retrievedatamulti (self,locations,dest,files,gridblocknumber,indexa,prop):
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
            for j in range(0,len(self.prop)):
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
        for state, capital in dictionary.items():
            if len(dictionary[state][0]) > 500:
                dictionary[state][0] = dictionary[state][0][::100]
        # pick minimum time for analysis                    
        for state, capital in dictionary.items():
            if 'first' in state:
                manny = dictionary[state][0]
                n = len(manny)-1
                if manny[n]<1000:
                    dictionary[state][0] = manny*3.154e+7
                    
        value1 = 10000000000000000000000000000000000000
        for state, capital in dictionary.items():
            if 'first' in state:
                manny = dictionary[state][0]
                value0 = manny[len(manny)-1]
                if value0 <= value1:
                    value1 = value0
                    
        return dictionary, lst, value1
    
    def retrievedatasingle (self,locations,dest,files,gridblocknumber,indexa,prop):
        dictionary = {}
        lst = []
        lookup = 'CONNE'
        for i in range(0,len(locations)):
            timer1 = 'first' + str(i)
            data1 = 'data' + str(i)
            lst.append(timer1)
            lst.append(data1)
            os.chdir(dest)
            tre1 = prepfortoughreact(locations[i],dest,files,lookup)
            tre1.copyallfiles()
            tre1.writetofile()
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
        for state, capital in dictionary.items():
            if len(dictionary[state][0]) > 500:
                dictionary[state][0] = dictionary[state][0][::100]

        for state, capital in dictionary.items():
            if 'first' in state:
                manny = dictionary[state][0]
                n = len(manny)-1
                if manny[n]<1000:
                    dictionary[state][0] = manny*3.154e+7
                    
        value1 = 100000000000000000000000000000000000000000000000
        for state, capital in dictionary.items():
            if 'first' in state:
                manny = dictionary[state][0]
                value0 = manny[len(manny)-1]
                if value0 <= value1:
                    value1 = value0
                    
        return dictionary, lst, value1
    
    
    def colorcoding(self,style):
        markers = ["o","v","^","<",">","1","2","3","4","8","s","p","P","*","h","H","+","x","X","D","d","|","_"]
        if style.lower()=='publication':
            colormarker = 'k' + markers[random.randint(0,(len(markers)-1))]
        elif style.lower()=='presentation':
            colormarker = 'r' + markers[random.randint(0,(len(markers)-1))]
        return colormarker
    
            
    
    def plotmultimulti (self,labels,width=12,height=8,linestyle='dashed',purpose='presentation'):
        dictionary,lst,value1 = self.retrievedatamulti(self.locations,self.dest,self.files,self.gridblocknumber,self.indexa,self.prop)
        fig = plt.figure(figsize=(width,height))
        kpansa = 0
        paralengthdouble = len(self.prop)*2
        for number in range(1,len(self.prop)+1):
            ax = fig.add_subplot(1,len(self.prop),number)
            j = 0
            colorcode = self.colorcoding(purpose)
            for i in range(kpansa,len(dictionary),paralengthdouble):   
                colorcode = self.colorcoding(purpose)
                try:
                    label=labels[j]
                except IndexError:
                    print('List provided not same with number of file')                    
                ax.plot(dictionary[lst[i]][0],dictionary[lst[i+1]][0],colorcode,linestyle=linestyle,label=labels[j])
                ax.set_xlim((0,value1))
#                ax.set_ylim((min(dictionary[lst[i]][0]),max(dictionary[lst[i+1]][0])))
                j=j+1
            kpansa = kpansa+2
            ax.legend(prop={'size': 10})
            ax.grid()
            ax.set_xlabel('Time (seconds)',fontsize=14,fontweight='bold')
            ax.set_ylabel(self.prop[number-1],fontsize=14,fontweight='bold')
            plt.tight_layout()
            fig.tight_layout()
        os.chdir(self.locations[0])
        fig.savefig(self.prop[0] +'.jpg',bbox_inches='tight',dpi=(600))
        matplotlib.style.use('default')
        
        
    def plotmultisingle(self,labels,width=12,height=8,linestyle='dashed',purpose='presentation'):
        dictionary,lst,value1 = self.retrievedatasingle(self.locations,self.dest,self.files,self.gridblocknumber,self.indexa,self.prop)
        fig = plt.figure(figsize=(width,height))
        colorcode = self.colorcoding(purpose)
        for i in range(0,len(lst),2):
            colorcode = self.colorcoding(purpose)
            plt.plot(dictionary[lst[i]][0],dictionary[lst[i+1]][0],colorcode,linestyle=linestyle)
            plt.legend(labels, prop={'size': 16})
            plt.xlim((0,value1))
        plt.grid()
        plt.xlabel('Time (seconds) ',fontsize=14,fontweight='bold')
        plt.ylabel(self.prop,fontsize=14,fontweight='bold')
        
        os.chdir(self.locations[0])
        fig.savefig(self.prop[0] +'.jpg',bbox_inches='tight',dpi=(600))
        
    def plotmulti(self,labels,width=12,height=8,linestyle='dashed',purpose='presentation'):
        if isinstance(self.prop, str):
            self.plotmultisingle(labels,width,height,linestyle,purpose)
        elif len(self.prop) >1:
            self.plotmultimulti(labels,width,height,linestyle,purpose)