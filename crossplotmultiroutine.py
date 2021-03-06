# -*- coding: utf-8 -*-
"""
Created on Wed May 27 01:39:24 2020

@author: AJ
"""

import matplotlib.pyplot as plt
from t2listing import * 
import os
import random
import pandas as pd
import matplotlib
from prepfortoughreact import *
from matplotlib.font_manager import FontProperties

class crossplotmultiroutine(object):
    """
    This class helps in making plots for batch/flow through reactions carried out with TOUGHREACT
    
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
        self.filecheck = files[0:3]
        
    def getparam(self,location):
        dictionary = {}
        lst = []
        lookup = 'CONNE'
        tre1 = prepfortoughreact(location,self.dest,self.files,lookup)
        tre1.copyallfiles()
        tre1.writetofile()
        os.chdir(self.dest)
        with open('test.txt') as f:
            br3 = f.read().splitlines()
        for file in self.filecheck:  
            tre=toughreact_tecplot(file,br3)
            tre._file.seek(0)
            line  = tre.skipto(['VARIABLES', 'Variables', 'variables'])
            eqpos = line.find('=')
            sep = ',' if ',' in line else None
            rawcols = line[eqpos+1:].strip().split(sep)
            cols = []
            for col in rawcols:
                colstrip = col.strip()
                if colstrip:
                    if col.startswith('"') and col.endswith('"'):
                        cols.append(col[1:-1].strip())
                    else:
                        cols.append(colstrip)
            dictionary[file]=cols
        return dictionary
    
    def get_dict_for_params(self,location):
        dictionary = self.getparam(location)
        final={}
        for i in range(len(self.prop)):
            for j in range(len(self.filecheck)):
                if self.prop[i] in dictionary[self.filecheck[j]]:
                    if self.filecheck[j] in final.keys():
                        final[self.filecheck[j]].append(self.prop[i])
                    else:
                        final[self.filecheck[j]] = [self.prop[i]]
        return final
    
    def find_file_for_param2(self,param,location):
        dictionary = self.getparam(location)
        final={}
        for j in range(len(self.filecheck)):
            if param in dictionary[self.filecheck[j]]:
                return self.filecheck[j]
            else:
                print("...still searching for filename...")
        
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
            for j in range(0,len(prop)):
                file_name = self.find_file_for_param2(prop[j],locations[i])
                tre=toughreact_tecplot(file_name,br3)
                tre.last()
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
                    # axs[j].legend(loc='upper right',borderpad=0.1)
                    plt.setp(axs[j].get_legend().get_texts(), fontsize='12')
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
            # handles, labels = axs.get_legend_handles_labels()
            # fig.legend(handles, labels, loc='upper center')
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
                    if self.prop[number-1].lower()=='porosity':
                        axs.set_ylabel("Porosity",fontsize=12)
                    elif self.prop[number-1].startswith("t_"):
                        axs.set_ylabel("Total Concentration (mol/L)",fontsize=12)
                    elif self.prop[number-1].startswith("pH"):
                        axs.set_ylabel("pH",fontsize=12)     
                    else:
                        # axs.set_ylabel("$\Delta$ in min vol frac ($m^3 min / m^3 solid$)",fontsize=12)
                        axs.set_ylabel("Change in volume fraction",fontsize=12)
                    axs.set_xlabel("Time (years)",fontsize=12)
                    # axs.legend(loc='upper right',borderpad=0.1)
                    # plt.setp(axs.get_legend().get_texts(), fontsize='10')
                    plt.xticks(fontsize=12)
                    plt.yticks(fontsize=12)
           #         axs.grid(True,which='both')
            #        axs.minorticks_on()
             #       plt.minorticks_on()
            #        axs.grid(b=True, which='major', linestyle='-', linewidth=0.5,color='k')
            #        axs.grid(b=True, which='minor', linestyle='-', linewidth=0.1)
                    if self.prop[number-1].startswith("t_"):
                        divider = self.prop[number-1].split("_")
                        axs.set_title(divider[1].capitalize())
                    elif self.prop[number-1].startswith("pH"):
                        axs.set_title(self.prop[number-1])
                    elif self.prop[number-1].startswith("mono"):
                        axs.set_title('Monosulfoaluminate')
                    elif self.prop[number-1].startswith("tobe"):
                        axs.set_title('Tobermorite')
                    else:
                        axs.set_title(self.prop[number-1].capitalize())
                    # axs.set_xticklabels(xlabels, fontsize=12 )
                    # axs.set_yticklabels(ylabels, fontsize=12 )
                    axs.spines['bottom'].set_linewidth(1.5)
                    axs.spines['left'].set_linewidth(1.5)
                    axs.spines['top'].set_linewidth(0.0)
                    axs.spines['right'].set_linewidth(0.0)
                    
            #        axs[0].set(xlabel="Exam score-1", ylabel="Exam score-2")
                    k=k+1
                counter =counter+1
                j=j+1
                kpansa = kpansa+2

            handles, labels = axs.get_legend_handles_labels()
            # fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(1.5, 1.05),ncol=2)
            # box = axs.get_position()
            # print(box.x0,box.y0,box.height,box.width)
            # axs.set_position([box.x0, box.y0 + box.height * 0.1,box.width, box.height * 0.1])
            # axs.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),fancybox=True, shadow=True, ncol=4)
            
            fig.tight_layout()
#           plt.setp(legend.get_title(),fontsize='xx-small')
#           plt.subplots_adjust(left  = 0.125,right = 0.9,bottom = 0.1,top = 0.9,wspace = 0.2,hspace = 0.2)
            plt.subplots_adjust(left  = 0.125,wspace = 0.4,top = 0.95)
            # axs.legend(handles , labels,loc='lower center',bbox_to_anchor=(0, -0.9),fancybox=False, shadow=False, ncol=4)
            axs.legend(handles , labels,loc='lower center',bbox_to_anchor=(-0.3, -0.9),fancybox=False, shadow=False, ncol=4)
            plt.setp(axs.get_legend().get_texts(), fontsize='12')
            os.chdir(self.locations[0])
            fig.savefig(self.prop[0] +'multiple'+'.jpg',bbox_inches='tight',dpi=(600)) 
                
        else:
            print('Style can either be horizontal or vertical or multiple')