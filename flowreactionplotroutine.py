# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:02:10 2019

@author: tajayi3
"""
import matplotlib
import matplotlib.pyplot as plt
from t2listing import *
import numpy as np
from scipy import interpolate
from scipy.interpolate import griddata

class flowreactionplotroutine(object):
    """
    This class helps in making plots for batch reactions carried out with TOUGHREACT
    
    """
    def __init__  (self,filename,gridblock,parameters):
        
        """
        An instance of this class takes in three parameters;
        
        filename --> the output file to be interpreted (in tecplot format) e.g. kddconc.tec
        gridblock ---> the total number of gridblocks in the simulations trypically should be a single block
        parameters -> parameters to be investigated (should be in a python list) e.g. ['pH','t_na+','t_ca2+']
        """
        self.filename = filename
        self.gridblock = gridblock
        self.parameters = parameters
        
    def convertlisttodict(self,parameters):
        
        """
        This method converts the list supplied to a dictionary for plot manipulations
        """
        i = 1
        param = {}
        for item in self.parameters:
            param[item] = i
            i = i+1
        return param
    
    def threeinone(self,width,height,grid,color='r--'):
        """
        This method plots three figures in a plot window and saves them with the name of the last item on the
        list
        
        width -> the width of the subplot
        height -> the height of the subplot
        grid -> the name of the block in the TOUGHREACT flow input
        color -> color is optional but if provided color of plot can be manipulated
        """
        fig = plt.figure(figsize=(width,height))
        tre = toughreact_tecplot(self.filename,self.gridblock)
        tre.last()
        a = self.parameters
        params = self.convertlisttodict(a)
        for item, number in params.items():
            ax = fig.add_subplot(1,3,number)
            data = tre.element[item]
            X = tre.element['X(m)']
            Y = tre.element['Y(m)']
            Z = tre.element['Z(m)']
            xi,yi = np.meshgrid(X,Y)
            data1 = griddata((X,Y),data,(xi,yi),method='nearest')
            #levels = [-4, -3, -2, -1, 1, 2, 3, 4]
            cs2 = plt.contourf(xi,yi,data1,10,  cmap='jet')  
            plt.colorbar()
            plt.xlabel('Distance(m)',fontsize=16)
            plt.ylabel(item,fontsize=16)
            plt.tight_layout()
            

        fig.savefig(item +'.png',bbox_inches='tight') 
    
    def sixinone(self,width,height,grid,color='r--'):
        """
        This method plots three figures in a plot window and saves them with the name of the last item on the
        list
        
        width -> the width of the subplot
        height -> the height of the subplot
        grid -> the name of the block in the TOUGHREACT flow input
        color -> color is optional but if provided color of plot can be manipulated
        """
        fig = plt.figure(figsize=(width,height))
        tre = toughreact_tecplot(self.filename,self.gridblock)
        tre.last()
        a = self.parameters
        params = self.convertlisttodict(a)
        index = [1,2,3,1,2,3]
        for item, number in params.items():
            if number == 1 or 2 or 3: j = 1
            elif number == 4 or 5 or 6: j =2
            ax = fig.add_subplot(j,3,index[number-1])
            data = tre.element[item]
            X = tre.element['X(m)']
            Y = tre.element['Y(m)']
            Z = tre.element['Z(m)']
            xi,yi = np.meshgrid(X,Y)
            data1 = griddata((X,Y),data,(xi,yi),method='nearest')
            #levels = [-4, -3, -2, -1, 1, 2, 3, 4]
            cs2 = plt.contourf(xi,yi,data1,10,  cmap='jet')  
            plt.colorbar()
            plt.xlabel('Distance(m)',fontsize=16)
            plt.ylabel(item,fontsize=16)
            plt.tight_layout()
            

        fig.savefig(item +'.png',bbox_inches='tight') 