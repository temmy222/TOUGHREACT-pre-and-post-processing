# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 18:08:03 2020

@author: AJ
"""

import csv
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import matplotlib.ticker as ticker
from random import randrange
import random
from scipy import interpolate
from scipy.interpolate import griddata

class tmvocplotting(object):
    def __init__(self,filelocation,filetitle,totalgridblocks):
        self.filelocation = filelocation
        os.chdir(self.filelocation)
        self.filetitle = filetitle
        self.totalgridblocks = totalgridblocks
        with open(self.filetitle) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
            self.file_as_list=[]
            for row in csv_reader:
                self.file_as_list.append(row)
                
    def __repr__(self):
        return 'Results from ' + self.filelocation + '\n' + self.filetitle
    
    def choplist(self,liste,number=40):
        if isinstance(liste, list):
            finallist =[]
            finallist.append(liste[0])
            newlist = liste[1:-1]
            len_newlist = len(newlist)
            ascend = list(np.linspace(1,len_newlist,len_newlist))
            randomi = random.sample(ascend,number)
            randomi.sort()
            myList = [int(x) for x in randomi]      
            for index,value in enumerate(myList):
                finallist.append(liste[value])
            finallist.append(liste[-1])
        else:
            print('Input must be a list')
        return finallist
            
    
    def get_times(self):
        time=[]
        timeraw = []
        for i in range(len(self.file_as_list)):
            if len(self.file_as_list[i])<25:
                time.append(self.file_as_list[i])
        for i in range(len(time)):
            interm = time[i][0].split()
            timeraw.append(float(interm[2]))  
        return timeraw
    
    def convert_times_year(self):
        intermediate = self.get_times()
        timeyear=[]
        for i in range(len(intermediate)):
            timeyear.append(intermediate[i]/3.154e+7)
        return timeyear
    
    def get_time_index(self):
        indextime=[]
        for index,value in enumerate(self.file_as_list):
            if len(self.file_as_list[index])<25:
                indextime.append(index)
        indextime.append(len(self.file_as_list))
        return indextime
        
    def get_elements(self):
        indextime = self.get_time_index()
        temp_file = self.file_as_list[indextime[0]+1:indextime[1]]
        elements =[]
        for i in range(len(temp_file)):
            elements.append(temp_file[i][0])
        return elements
        
    
    def resultdict(self):
        resultdict = {}
        tempdict={}  
        indextime = self.get_time_index()
        timeraw = self.get_times()
        for i in range(len(indextime)-1):
            tempdict[i] = self.file_as_list[indextime[i]+1:indextime[i+1]]  
        for i in range(len(timeraw)):
            resultdict[timeraw[i]] = tempdict[i]
        return resultdict
    
    def get_timeseries_data(self,param,gridblocknumber):
        results = self.resultdict()
        resultarray =[]
        heading= []
        heading_first = self.file_as_list[0]
        heading_first_modify =[]
        for i in heading_first:
            heading_first_modify.append(i.upper())
        for i in range(len(heading_first_modify)):
            heading.append(heading_first_modify[i].lstrip())   
        index_param = heading.index(param.upper())
        for k in results.keys():   
            resultarray.append(results[k][gridblocknumber][index_param].lstrip())
        final_data = [float(x) for x in resultarray]
        return final_data
    
    def get_element_data(self,time,param):
        timeraw = self.get_times()
        results = self.resultdict()
        heading= []
        heading_first = self.file_as_list[0]
        heading_first_modify =[]
        for i in heading_first:
            heading_first_modify.append(i.upper())
        for i in range(len(heading_first_modify)):
            heading.append(heading_first_modify[i].lstrip())   
        index_param = heading.index(param.upper())
        if time < timeraw[0]: time = timeraw[0]
        elif time > timeraw[-1]: time = timeraw[-1]
        else:
            absolute_difference_function = lambda list_value : abs(list_value - time)
            time = min(timeraw, key=absolute_difference_function)
        results_specific= results[time]
        data = []
        for i in range(len(results_specific)):
            data.append(results_specific[i][index_param].lstrip())
        final_data = [float(x) for x in data]
        return final_data
    
    def param_label_full(self,param):
        dict_param = {'PRES':'Pressure (Pa)','TEMP':'Temperature ($^o C$)','SAT_G':'Gas Saturation (-)','SAT_L':'Liquid Saturation (-)',
                      'SAT_N':'NAPL Saturation (-)','X_WATER_G':'Water Mass Fraction in Gas (-)','X_AIR_G':'Air Mass Fraction in Gas (-)',
                      'X_WATER_L':'Water Mass Fraction in Liquid (-)','X_AIR_L':'Air Mass Fraction in Liquid (-)','X_WATER_N':'Water Mass Fraction in NAPL (-)',
                      'X_AIR_N':'Air Mass Fraction in NAPL (-)','REL_G"':'Relative Permeability of Gas (-)','REL_L':'Relative Permeability of Liquid (-)',
                      'REL_N':'Relative Permeability of NAPL (-)','PCAP_GL':'Capillary Pressure of Gas in Liquid (Pa)',
                      'PCAP_GN':'Capillary Pressure of Gas in NAPL (Pa)','DEN_G':'Gas Density ($kg/m^3$)','DEN_L':'Liquid Density ($kg/m^3$)',
                      'DEN_N':'NAPL Density ($kg/m^3$)','POR':'Porosity','BIO1':'Biomass Mass Fraction(-)','BIO2':'Biomass Mass Fraction(-)',
                      'X_BENZEN_L':'Mass Fraction of Benzene in Liquid','X_TOLUEN_L':'Mass Fraction of Toluene in Liquid',
                      'X_N-DECA_L': 'Mass Fraction of Decane in Liquid','X_TOLUEN_N':'Mass Fraction of Toluene in NAPL',
                      'X_TOLUEN_G':'Mass Fraction of Toluene in Gas'}
        return dict_param[param]
    
    def plot_time(self,param,gridblocknumber):
        result_array = self.get_timeseries_data(param,gridblocknumber)
        time_year = self.convert_times_year()
        fig = plt.figure()
        fig, axs = plt.subplots(1,1)
        # result_array = self.choplist(result_array)
        # time_year = self.choplist(time_year)
        # plt.plot(time_year,result_array)
        # plt.xlabel('Time (year)')
        # plt.ylabel(self.param_label_full(param.upper()))
        # plt.spines['bottom'].set_linewidth(1.5)
        # plt.spines['left'].set_linewidth(1.5)
        # plt.spines['top'].set_linewidth(0.2)
        # plt.spines['right'].set_linewidth(0.2)
        axs.plot(time_year,result_array,marker='^',label=self.param_label_full(param.upper()))
        axs.set_xlabel('Time (year)')
        axs.set_ylabel(self.param_label_full(param.upper()))
        axs.spines['bottom'].set_linewidth(1.5)
        axs.spines['left'].set_linewidth(1.5)
        axs.spines['top'].set_linewidth(0)
        axs.spines['right'].set_linewidth(0)
        axs.legend(loc='upper right',borderpad=0.1)
        
    def multi_time_plot(self,param,gridblocknumber,style='horizontal'):
        fig = plt.figure()
        time_year = self.convert_times_year()
        j = 0
        if style.lower()=='horizontal':
            fig, axs = plt.subplots(len(param), sharex=False)
            for parameter in param:
                result_array = self.get_timeseries_data(parameter,gridblocknumber)
                axs[j].plot(time_year,result_array,marker='^',label=self.param_label_full(parameter.upper()))
                axs[j].set_ylabel(self.param_label_full(parameter.upper()),fontsize=12)
                axs[j].spines['bottom'].set_linewidth(1.5)
                axs[j].spines['left'].set_linewidth(1.5)
                axs[j].spines['top'].set_linewidth(0)
                axs[j].spines['right'].set_linewidth(0)
                # axs[j].legend(loc='best',borderpad=0.1)
                axs[j].set_xlabel('Time (year)', fontsize=12)
                axs[j].ticklabel_format(useOffset=False)
                plt.setp(axs[j].get_xticklabels(), fontsize=12)
                plt.setp(axs[j].get_yticklabels(), fontsize=12)
                j=j+1

            # plt.xlabel('Time (year)')
            plt.tight_layout()
        elif style.lower()=='vertical':
            for number in range(1,len(param)+1):
                ax = fig.add_subplot(1,len(param),number)
                result_array = self.get_timeseries_data(param[number-1],gridblocknumber)
                ax.plot(time_year,result_array,marker='^',label=self.param_label_full(param[number-1].upper()))
                ax.set_ylabel(self.param_label_full(param[number-1].upper()),fontsize=12)
                ax.spines['bottom'].set_linewidth(1.5)
                ax.spines['left'].set_linewidth(1.5)
                ax.spines['top'].set_linewidth(0)
                ax.spines['right'].set_linewidth(0)
                # ax.ticklabel_format(useOffset=False,style='plain')
                ax.ticklabel_format(useOffset=False)
                plt.setp(ax.get_xticklabels(), fontsize=12)
                plt.setp(ax.get_yticklabels(), fontsize=12)
                # ax.legend(loc='best',borderpad=0.1)
                ax.set_xlabel('Time (year)',fontsize=12)
                j=j+1
            # plt.xlabel('Time (year)')
            plt.tight_layout()

    def fmt(self,x, pos):
        a, b = '{:.2e}'.format(x).split('e')
        b = int(b)
        return r'${} \times 10^{{{}}}$'.format(a, b)
            
    def plot2D_one(self,param,timer,direction='XZ'):
        if direction=='XZ':
            fig = plt.figure()
            fig, ax = plt.subplots(1,1)
            X = self.get_element_data(timer, 'x')
            Z = self.get_element_data(timer, 'z')
            data = self.get_element_data(timer, param)
            xi,yi = np.meshgrid(X,Z)
            data1 = griddata((X,Z),data,(xi,yi),method='nearest')
            # cs2 = plt.contourf(xi,yi,data1,800,extend='neither',cmap='coolwarm')
            cs2 = plt.contourf(xi,yi,data1,800, cmap='coolwarm',vmin=min(data),vmax=max(data))
          #  ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.2e'))
            # c = ax.pcolor(xi, yi, data, cmap='RdBu')
            vmin=min(data)
            if vmin <1 or vmin >1000:
                cbar = fig.colorbar(cs2,pad=0.01,format=ticker.FuncFormatter(self.fmt))
            else:
                cbar = fig.colorbar(cs2,pad=0.01)
            cbar.ax.set_ylabel(self.param_label_full(param.upper()),fontsize=12)
            ticklabs = cbar.ax.get_yticklabels()
          #  ticklabs.set_major_formatter(mtick.FormatStrFormatter('%.2e'))
            cbar.ax.set_yticklabels(ticklabs, fontsize=12)
            plt.xlabel('Horizontal Distance(m)',fontsize=12)
            plt.ylabel('Vertical Depth (m)',fontsize=12)
            plt.tick_params(axis='x', labelsize=12)
            plt.tick_params(axis='y', labelsize=12)
            plt.tight_layout()
            
    def get_number_of_grids(self,input_list):
        output = set()
        for x in input_list:
            output.add(x)
        output = list(output)
        return len(output)
        
        
            
    def plot2D_withgrid(self,param,timer,direction='XZ'):
        if direction=='XZ':
            fig, ax = plt.subplots(1,1)
            X = self.get_element_data(timer, 'x')
            Z = self.get_element_data(timer, 'z')
            num_X = self.get_number_of_grids(X)
            num_Z = self.get_number_of_grids(Z)
            orig_data = self.get_element_data(timer, param)
            xi,yi = np.meshgrid(X,Z)
            data = np.asarray(self.get_element_data(timer, param))
            # data = data.reshape(num_Z,num_X)
            data1 = griddata((X,Z),orig_data,(xi,yi),method='nearest')
            extent = [min(X), max(X), min(Z), max(Z)]
            # cs2 = plt.pcolor(xi,yi,data1,edgecolors='k',cmap='coolwarm', linewidths=1,vmin=min(orig_data), vmax=max(orig_data))
            # ax.imshow(data,extent=extent)
            # ax.grid(color='k', linestyle='-', linewidth=2)
            # ax.set_frame_on(False)
            # cbar = fig.colorbar(cs2,ax=ax,pad=0.01)
            # cbar.ax.set_ylabel(self.param_label_full(param.upper()),fontsize=12)
            # plt.xlabel('Horizontal Distance(m)',fontsize=12)
            # plt.ylabel('Vertical Depth (m)',fontsize=12)
            # plt.tick_params(axis='x', labelsize=12)
            # plt.tick_params(axis='y', labelsize=12)
            # plt.tight_layout()
            # plt.figure()
            cs2 = plt.imshow(np.reshape(data, newshape=(num_Z,num_X)),cmap='coolwarm',
                            interpolation='none');
            ax = plt.gca();
            # Major ticks
            ax.set_xticks(np.arange(0, num_X, 6));
            ax.set_yticks(np.arange(0, num_Z, 1));
            # Labels for major ticks
            ax.set_xticklabels(np.arange(1, round(max(X))+1, 6),fontsize=12);
            ax.set_yticklabels(np.arange(abs(max(Z))+2, abs(min(Z))+3, 5),fontsize=12);
            # Minor ticks
            ax.set_xticks(np.arange(-.5, num_X, 1), minor=True);
            ax.set_yticks(np.arange(-.5,num_Z, 1), minor=True);
            # Gridlines based on minor ticks
            ax.grid(which='minor', color='k', linestyle='-', linewidth=1)
            cbar = fig.colorbar(cs2,ax=ax,pad=0.01)
            cbar.ax.set_ylabel(self.param_label_full(param.upper()),fontsize=12)
            plt.xlabel('Horizontal Distance(m)',fontsize=12)
            plt.ylabel('Vertical Depth (m)',fontsize=12)
            plt.tight_layout()
            print(abs(max(Z)),abs(min(Z)))
            
            

            
            
                
        
        
            
        
        