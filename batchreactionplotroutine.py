# -*- coding: utf-8 -*-
"""
Created on Tue May 14 16:49:02 2019

@author: tajayi3
"""
import matplotlib
import matplotlib.pyplot as plt
from t2listing import * 
import os
import pandas as pd


class batchreactionplotroutine(object):
    """
    This class helps in making plots for batch reactions carried out with TOUGHREACT
    
    """
    def __init__  (self,filename,gridblock,parameters):
        
        """
        An instance of this class takes in three parameters;
        
        filename --> the output file to be interpreted (in tecplot format) e.g. kddconc.tec
        gridblock ---> the total number of gridblocks in the simulations 
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
        
    def sixinone(self,width,height,grid,color='r--'):
        """
        This method plots three figures in a plot window and saves them with the name of the last item on the
        list
        
        width -> the width of the subplot
        height -> the height of the subplot
        grid -> the name of the block in the TOUGHREACT flow input
        color -> color is optional but if provided color of plot can be manipulated
        """
        fig, axs = plt.subplots(2,3, figsize=(width, height), facecolor='w', edgecolor='k')
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
            
    def extractdata(self,fileloc,width,height,grid):
        i = 0
        df = pd.DataFrame()
        if not isinstance(fileloc, list): 
            print ('Input must be list of file directories containing the location of results')            
        for item in fileloc:
            try:
                os.chdir(item)
            except OSError:
                print("Can't change the Current Working Directory") 
            tre = toughreact_tecplot(self.filename,self.gridblock)
            tre.last()
            a = self.parameters
            params = self.convertlisttodict(a)
            for itema, number in params.items():
                mf = tre.history([(grid,itema)])
                time = mf[0]
                data= mf[1]
                df.insert(i,"time",time,True)
                i = i+1
                df.insert(i,itema , data, True) 
                i = i +1
        return df
    
    def plotdifferenttwo(self,fileloc,width,height,grid,labels):
        if not isinstance(labels, list): 
            print ('Label must be a list')        
        masa = self.extractdata(fileloc,width,height,grid)
        fig = plt.figure(figsize=(width,height))
        i = 0; j = 1; k = 6; l=7
        for number in range(1,4):
            ax = fig.add_subplot(1,3,number)
            try:
                ax.plot(masa.iloc[:, i],masa.iloc[:, j], 'r--',label=labels[0])
                ax.plot(masa.iloc[:, k],masa.iloc[:, l], 'b--',label=labels[1])
            except IndexError:
                print('Please enter a list of labels')
            ax.grid()
            ax.set_xlabel(masa.columns[i],fontsize=16)
            ax.set_ylabel(masa.columns[j],fontsize=16)
            legend = ax.legend(loc='upper right')
            i = i+2;j=j+2;k=k+2;l=l+2
            plt.tight_layout()
        fig.savefig(labels[0] +'.png',bbox_inches='tight')
            
    def plotdifferentthree(self,fileloc,width,height,grid,labels):
        if not isinstance(labels, list): 
            print ('Label must be a list')  
        masa = self.extractdata(fileloc,width,height,grid)
        fig = plt.figure(figsize=(width,height))
        i = 0; j = 1; k = 6; l=7;m=12;n=13
        for number in range(1,4):
            ax = fig.add_subplot(1,3,number)
            try:
                ax.plot(masa.iloc[:, i],masa.iloc[:, j], 'r--',label=labels[0])
                ax.plot(masa.iloc[:, k],masa.iloc[:, l], 'b--',label=labels[1])
                ax.plot(masa.iloc[:, m],masa.iloc[:, n], 'k--',label=labels[2])
            except IndexError:
                print('Please enter a list of labels')
            ax.grid()
            ax.set_xlabel(masa.columns[i],fontsize=16)
            ax.set_ylabel(masa.columns[j],fontsize=16)
            legend = ax.legend(loc='upper right')
            i = i+2;j=j+2;k=k+2;l=l+2;m=m+2;n=n+2
            plt.tight_layout()
        fig.savefig(labels[0] +'.png',bbox_inches='tight')

    def plotdifferentfour(self,fileloc,width,height,grid,labels):
        if not isinstance(labels, list): 
            print ('Label must be a list')  
        masa = self.extractdata(fileloc,width,height,grid)
        fig = plt.figure(figsize=(width,height))
        i = 0; j = 1; k = 6; l=7;m=12;n=13;o=18;p=19
        for number in range(1,4):
            ax = fig.add_subplot(1,3,number)
            try:
                ax.plot(masa.iloc[:, i],masa.iloc[:, j], 'r--',label=labels[0])
                ax.plot(masa.iloc[:, k],masa.iloc[:, l], 'b--',label=labels[1])
                ax.plot(masa.iloc[:, m],masa.iloc[:, n], 'k--',label=labels[2])
            except IndexError:
                print('Please enter a list of labels')
            ax.plot(masa.iloc[:, o],masa.iloc[:, p], 'm+',label=labels[3])
            ax.grid()
            ax.set_xlabel(masa.columns[i],fontsize=16)
            ax.set_ylabel(masa.columns[j],fontsize=16)
            legend = ax.legend(loc='upper right')
            i = i+2;j=j+2;k=k+2;l=l+2;m=m+2;n=n+2;o=o+2;p=p+2
            plt.tight_layout()
        fig.savefig(labels[0] +'.png',bbox_inches='tight')
        
    def plotdifferent(self,fileloc,width,height,grid,labels):
        if len(fileloc)==2:
            self.plotdifferenttwo(fileloc,width,height,grid,labels)
        elif len(fileloc)==3:
            self.plotdifferentthree(fileloc,width,height,grid,labels)
        elif len(fileloc)==4:
            self.plotdifferentfour(fileloc,width,height,grid,labels)