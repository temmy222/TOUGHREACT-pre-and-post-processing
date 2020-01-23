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
from matplotlib.font_manager import FontProperties

class multiplotroutine(object):
    """
    This class helps in making plots for batch reactions carried out with TOUGHREACT
    
    """
    def __init__  (self,locations,dest,files,gridblocknumber,indexa,prop):
        
        """
        An instance of this class takes in three parameters;
        
        locations --> Locations of files to be compared (list)
        
        dest ---> destination of folder containing the PYTOUGH classes
        
        files -> files to be compared e.g. kddconc.tec, kddmin.tec etc (list)
        
        gridblocknumber: gridblock number to be compared over time
        
        indexa - index of particular file to be compared. for example if a list of [kddconc.tec, kddmin.tec] is supplied and 
        indexa is 0, the functions are only performed on the kddconc.tec
        
        prop - properties to be plotted. should correspond to property selected above for example if kddconc.tec is selected prop
        should be [ph,tca] etc
        
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
                try:
                    mf = tre.history([(br3[gridblocknumber],prop[j])])
                except KeyError:
                    mason = prop[j].strip('t_')
                    mf = tre.history([(br3[gridblocknumber],mason)])
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
            if len(dictionary[state][0]) > 100 and len(dictionary[state][0]) < 500 :
                dictionary[state][0] = dictionary[state][0][::20]
            elif len(dictionary[state][0]) > 500 and len(dictionary[state][0]) < 2000:
                dictionary[state][0] = dictionary[state][0][::10]
            elif len(dictionary[state][0]) > 2000 and len(dictionary[state][0]) < 10000:
                dictionary[state][0] = dictionary[state][0][::500]
            elif len(dictionary[state][0]) > 10000 and len(dictionary[state][0]) < 100000:
                dictionary[state][0] = dictionary[state][0][::5000]
            elif len(dictionary[state][0]) > 100000:
                dictionary[state][0] = dictionary[state][0][::10000]                
        # pick minimum time for analysis                    
        for state, capital in dictionary.items():
            if 'first' in state:
                manny = dictionary[state][0]
                n = len(manny)-1
                if manny[n]>1000:
                    dictionary[state][0] = manny/3.154e+7
                    
        value1 = 10000000000000000000000000000000000000
        for state, capital in dictionary.items():
            if 'first' in state:
                manny = dictionary[state][0]
                value0 = manny[len(manny)-1]
                if value0 <= value1:
                    value1 = value0
                    
        return dictionary, lst, value1
    
#    def retrievedatadistance(self,locations,dest,files,gridblocknumber,indexa,prop):
    def retrievedatadistance(self,locations,direction,blocknumber):
        lst = self.prop.copy()
        tre = toughreact_tecplot(self.filename,self.gridblock)
        tre.last()
        X = tre.element['X(m)']
        Y = tre.element['Y(m)']
        Z = tre.element['Z(m)']
        lst.insert(0, 'X(m)')
        if direction.lower() == 'x':
            dictionary = {}
            for index,character in enumerate(lst): 
                if character not in dictionary.keys():
                    dictionary[character] = []
            for i in range(0,len(lst)):
                X = tre.element[lst[i]][:blocknumber]
                dictionary[lst[i]].append(X)
                
            
        elif direction.lower() == 'y':
            Y = Y[:blocknumber]
        elif direction.lower() == 'z':
            Z = Z[:blocknumber]
        
        return dictionary, lst
    
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
            try:
                mf = tre.history([(br3[gridblocknumber],prop)])
            except KeyError:
                mason = prop.strip('t_')
                mf = tre.history([(br3[gridblocknumber],mason)])
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
                if manny[n]>1000:
                    dictionary[state][0] = manny/3.154e+7
                    
        value1 = 100000000000000000000000000000000000000000000000
        for state, capital in dictionary.items():
            if 'first' in state:
                manny = dictionary[state][0]
                value0 = manny[len(manny)-1]
                if value0 <= value1:
                    value1 = value0
                    
        return dictionary, lst, value1
    
    
    def colorcoding(self,style):
        colormarker = []
        markers = ["-o","-v","-^","-<","->","-1","-2","-3","-4","-8","-s","-p","-P","-*","-h","-H","-+","-x","-X","-D","-d","-|","-_"]
#        markers = ["o","v","^","<",">","1","2","3","4","8","s","p","P","*","h","H","+","x","X","D","d","|","_"]
        for i in range(0,len(self.locations)):
            if style.lower()=='publication':
                a = markers[random.randint(0,(len(markers)-1))]
                colorm = 'k' + a
                if colorm in colormarker:
                    colormarker.remove(colorm)
                    markers.remove(a)
                    colorm = 'k' + markers[random.randint(0,(len(markers)-1))]
                colormarker.append(colorm)
            elif style.lower()=='presentation':
                colorm = 'r' + markers[random.randint(0,(len(markers)-1))]
                if colorm in colormarker:
                    colorm = 'r' + markers[random.randint(0,(len(markers)-1))]
        colormarker.append(colorm)
        return colormarker
    
    def sortcolor(self,style,number):
        colorcode = []
        markers = ["-o","-v","-^","-<","->","-1","-2","-3","-4","-8","-s","-p","-P","-*","-h","-H","-+","-x","-X","-D","-d","-|","-_"]
#        markers = ["o","v","^","<",">","1","2","3","4","8","s","p","P","*","h","H","+","x","X","D","d","|","_"]
        colors = ['b','r','g','c','m','y','k']
        if style.lower()=='publication':
            for i in range(0,number):
                m = 'k' + markers[random.randint(0,(len(markers)-1))]  
                if m in colorcode:
                    n = m.strip('k')
                    markers.remove(n)
                    m = 'k' + markers[random.randint(0,(len(markers)-1))] 
                colorcode.append(m)
        elif style.lower()=='presentation':
            for i in range(0,number):
#                m = 'r' + markers[random.randint(0,(len(markers)-1))]  
                part1 = colors[random.randint(0,(len(colors)-1))] 
                part2 = markers[random.randint(0,(len(markers)-1))]
                m = part1   + part2
                if m in colorcode:
                    stripa1 = m.strip(part1)
                    stripa2 = m.strip(part2)
                    markers.remove(stripa1)
                    colors.remove(stripa2)
                    m = colors[random.randint(0,(len(colors)-1))]  + markers[random.randint(0,(len(markers)-1))] 
                colorcode.append(m)
        return colorcode           
    
    def plotmultimulti (self,labels,width=12,height=8,linestyle='dashed',purpose='presentation',style='horizontal'):
        dictionary,lst,value1 = self.retrievedatamulti(self.locations,self.dest,self.files,self.gridblocknumber,self.indexa,self.prop)
        fig = plt.figure(figsize=(width,height))
        font = {'family' : 'normal','size'   : 18}
        matplotlib.rc('font', **font)
        kpansa = 0
        paralengthdouble = len(self.prop)*2
        colorcode = self.sortcolor(purpose,len(self.locations))
        colors=['r','royalblue','g','k','c','m','y']
        markers = ["o","v","^","<",">","1","2","3","4","8","s","p","P","*","h","H","+","x","X","D","d","|","_"]
        if style.lower()=='horizontal':
            fig, axs = plt.subplots(len(self.prop), sharex=True)
            plt.rc('legend', fontsize='small')
            j = 0
            for number in range(1,len(self.prop)+1):
                k=0
                for i in range(kpansa,len(dictionary),paralengthdouble): 
                    axs[j].plot(dictionary[lst[i]][0],dictionary[lst[i+1]][0],label=labels[k],linewidth=2,color = colors[k],marker=markers[k])
                    axs[j].legend(loc='upper right',borderpad=0.1)
                    plt.setp(axs[j].get_legend().get_texts(), fontsize='10')
                    axs[j].grid(True,which='both')
                    axs[j].minorticks_on()
                    plt.minorticks_on()
                    axs[j].grid(b=True, which='major', linestyle='-', linewidth=0.5,color='k')
                    axs[j].grid(b=True, which='minor', linestyle='-', linewidth=0.1)
                    axs[j].set_title(self.prop[number-1])
                    axs[j].spines['bottom'].set_linewidth(1.5)
                    axs[j].spines['left'].set_linewidth(1.5)
                    axs[j].spines['top'].set_linewidth(0.2)
                    axs[j].spines['right'].set_linewidth(0.2)
                    k=k+1
                j=j+1
                kpansa = kpansa+2
            fig.tight_layout()
#           plt.setp(legend.get_title(),fontsize='xx-small')
#           plt.subplots_adjust(left  = 0.125,right = 0.9,bottom = 0.1,top = 0.9,wspace = 0.2,hspace = 0.2)
            plt.subplots_adjust(left  = 0.125,wspace = 0.4,top = 0.95)
            os.chdir(self.locations[0])
            fig.savefig(self.prop[0] +'horizontal'+'.jpg',bbox_inches='tight',dpi=(600))
        elif style.lower()=='vertical':
            for number in range(1,len(self.prop)+1):
                ax = fig.add_subplot(1,len(self.prop),number)
                j = 0
                print(colorcode)
                k = 0
                for i in range(kpansa,len(dictionary),paralengthdouble):
                    try:
                        label=labels[j]
                    except IndexError:
                        print('List provided not same with number of file')                    
                    ax.plot(dictionary[lst[i]][0],dictionary[lst[i+1]][0],colors[k],marker=markers[k],label=labels[j],linewidth=2,markersize=8)
                    ax.legend(loc='upper right',borderpad=0.1)
                    plt.setp(ax.get_legend().get_texts(), fontsize='10')
                    ax.grid(True,which='both')
                    ax.minorticks_on()
                    plt.minorticks_on()
                    ax.grid(b=True, which='major', linestyle='-', linewidth=0.5,color='k')
                    ax.grid(b=True, which='minor', linestyle='-', linewidth=0.1)
                    ax.set_title(self.prop[number-1])
                    ax.spines['top'].set_linewidth(0.2)
                    ax.spines['right'].set_linewidth(0.2)
                    ax.spines['bottom'].set_linewidth(1.5)
                    ax.spines['left'].set_linewidth(1.5)
#                    ax.set_xlim((0,value1))
#                    ax.set_ylim((min(dictionary[lst[i]][0]),max(dictionary[lst[i+1]][0])))
                    j=j+1
                    k = k+1
                kpansa = kpansa+2
                ax.legend(prop={'size': 18})
                ax.grid()
                ax.set_xlabel('Time (years)',fontsize=18,fontweight='bold')
                ax.set_ylabel(self.prop[number-1].capitalize(),fontsize=18,fontweight='bold')
                plt.tight_layout()
                fig.tight_layout()
            os.chdir(self.locations[0])
            fig.savefig(self.prop[0] +'.jpg',bbox_inches='tight',dpi=(600))
            matplotlib.style.use('default')
        elif style.lower()=='multiple':
#            fig = plt.figure()
#            fig.subplots_adjust(hspace=0.4, wspace=0.4)
            plt.rc('legend', fontsize='small')
            j = 0
            counter =1
            for number in range(1,len(self.prop)+1):
                axs = plt.subplot(3,2,counter)
                k=0
                for i in range(kpansa,len(dictionary),paralengthdouble): 
                    axs.plot(dictionary[lst[i]][0],dictionary[lst[i+1]][0],label=labels[k],linewidth=2,color = colors[k],marker=markers[k])
                    axs.legend(loc='upper right',borderpad=0.1)
                    plt.setp(axs.get_legend().get_texts(), fontsize='10')
                    axs.grid(True,which='both')
                    axs.minorticks_on()
                    plt.minorticks_on()
                    axs.grid(b=True, which='major', linestyle='-', linewidth=0.5,color='k')
                    axs.grid(b=True, which='minor', linestyle='-', linewidth=0.1)
                    axs.set_title(self.prop[number-1])
                    axs.spines['bottom'].set_linewidth(1.5)
                    axs.spines['left'].set_linewidth(1.5)
                    axs.spines['top'].set_linewidth(0.2)
                    axs.spines['right'].set_linewidth(0.2)
                    k=k+1
                counter =counter+1
                j=j+1
                kpansa = kpansa+2
            fig.tight_layout()
#           plt.setp(legend.get_title(),fontsize='xx-small')
#           plt.subplots_adjust(left  = 0.125,right = 0.9,bottom = 0.1,top = 0.9,wspace = 0.2,hspace = 0.2)
            plt.subplots_adjust(left  = 0.125,wspace = 0.4,top = 0.95)
            os.chdir(self.locations[0])
            fig.savefig(self.prop[0] +'horizontal'+'.jpg',bbox_inches='tight',dpi=(600))      
        else:
            print('Style can either be horizontal or vertical or multiple')
        
        
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
        plt.xlabel('Time (years) ',fontsize=14,fontweight='bold')
        plt.ylabel(self.prop,fontsize=14,fontweight='bold')
        
        os.chdir(self.locations[0])
        fig.savefig(self.prop[0] +'.jpg',bbox_inches='tight',dpi=(600))
        
    def plotmulti(self,labels,width=12,height=8,linestyle='dashed',purpose='presentation'):
        if isinstance(self.prop, str):
            self.plotmultisingle(labels,width,height,linestyle,purpose)
        elif len(self.prop) >1:
            self.plotmultimulti(labels,width,height,linestyle,purpose)
            
    def plotmultidistance(self,labels,width=12,height=8,linestyle='solid',purpose='presentation'):
        with open('test.txt') as f:
            br3 = f.read().splitlines()
        for i in self.locations:
            m = flowreactionplotroutine(self.files[indexa],br3,self.prop,self.locations[0])
            
            
        