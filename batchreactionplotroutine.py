# -*- coding: utf-8 -*-
"""
Created on Tue May 14 16:49:02 2019

@author: tajayi3
"""
import matplotlib
import matplotlib.pyplot as plt
from t2listing import * 

class batchreactionplotroutine(object):
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
        i = 0
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
        fig, axs = plt.subplots(1,3, figsize=(width, height), facecolor='w', edgecolor='k')
        axs = axs.ravel()
        tre = toughreact_tecplot(self.filename,self.gridblock)
        tre.last()
        a = self.parameters
        params = self.convertlisttodict(a)
        for item, number in params.items():
            mf = tre.history([(grid,item)])
            time = mf[0]
            data= mf[1]
            axs[number].plot(time,data,color, marker='x')
            axs[number].grid()
            axs[number].set_ylabel(item)
            axs[number].set_xlabel('Time (seconds)')
            plt.tight_layout()
        fig.savefig(item +'.png',bbox_inches='tight') 