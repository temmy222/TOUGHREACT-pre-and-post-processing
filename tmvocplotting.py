# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 18:08:03 2020

@author: AJ
"""

import csv
import os
import numpy as np
import matplotlib.pyplot as plt

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
    
    def filetolist(self):
        pass

    
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
    
    def get_time_data(self,param,gridblocknumber):
        results = self.resultdict()
        resultarray =[]
        heading= []
        heading_first = self.file_as_list[0]
        for i in range(len(heading_first)):
            heading.append(heading_first[i].lstrip())   
        index_param = heading.index(param.upper())
        for k in results.keys():   
            resultarray.append(results[k][gridblocknumber][index_param])
        return resultarray
    
    def get_element_data(self,time,param):
        timeraw = self.get_times()
        results = self.resultdict()
        heading= []
        heading_first = self.file_as_list[0]
        for i in range(len(heading_first)):
            heading.append(heading_first[i].lstrip())   
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
        return data
    
    def param_label_full(self,param):
        dict_param = {'PRES':'Pressure (psi)'}
        if param.upper == 'PRES':
            return 'Pressure (psi)'
    
    def plot_time(self,param,gridblocknumber):
        result_array = self.get_time_data(param,gridblocknumber)
        times = self.get_times()
        plt.plot(times,result_array)
        plt.grid()
        
        
            
        
        