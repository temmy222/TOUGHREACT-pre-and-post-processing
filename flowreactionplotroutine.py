# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:02:10 2019

@author: tajayi3
"""
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from t2listing import *
import numpy as np
import os
from scipy import interpolate
from scipy.interpolate import griddata
import random
import pandas as pd
import decimal

class flowreactionplotroutine(object):
    """
    This class helps in making plots for batch reactions carried out with TOUGHREACT
    
    """
    def __init__  (self,filename,gridblock,parameters,saveloc):
        
        """
        An instance of this class takes in three parameters;
        
        filename --> the output file to be interpreted (in tecplot format) e.g. kddconc.tec
        gridblock ---> the total number of gridblocks in the simulations trypically should be a single block
        parameters -> parameters to be investigated (should be in a python list) e.g. ['pH','t_na+','t_ca2+']
        saveloc -> location to save results images
        """
        self.filename = filename
        self.gridblock = gridblock
        self.parameters = parameters
        self.saveloc = saveloc
        
        
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
    
    def direction(self,width,height,grid,direction,timer,color):
        if direction=='XZ':
            fig = plt.figure(figsize=(width,height))
            tre = toughreact_tecplot(self.filename,self.gridblock)
            if timer == None:
                tre.last()
            else:
                tre.set_time(timer)
            if color ==None:
                color ='r'
            a = self.parameters
            params = self.convertlisttodict(a)
            for item, number in params.items():
                ax = fig.add_subplot(1,len(self.parameters),number)
                data = tre.element[item]
                X = tre.element['X(m)']
                Z = tre.element['Z(m)']
                xi,yi = np.meshgrid(X,Z)
                data1 = griddata((X,Z),data,(xi,yi),method='nearest')
                import matplotlib.colors as mc
                cbar_min = np.min(data1)
                cbar_max = np.max(data1)+0.01
#                cbarlabels = np.linspace(np.floor(cbar_min), np.ceil(cbar_max), num=5, endpoint=True)
                levels = np.linspace(cbar_min, cbar_max, 3) 
#                norm = mc.BoundaryNorm(levels, 256)
                print(timer)
             #   cs2 = plt.contourf(xi,yi,data1,levels, cmap='coolwarm',norm=norm)
                # cs2 = plt.contourf(xi,yi,data1,10,  cmap='coolwarm',vmin=8.5,vmax=8.9)
                cs2 = plt.contourf(xi,yi,data1,800,extend='neither',cmap='coolwarm')
                # cs2=ax.imshow(data1,interpolation='bilinear', cmap=plt.cm.coolwarm,origin='lower',aspect='auto', extent=[X.min(), X.max(), Z.min(), Z.max()])
                # plt.imshow(data1,origin='lower')
                # cbaxes = fig.add_axes([0.9, 0.2, 0.01, 0.7]) 
                cbar = fig.colorbar(cs2,pad=0.01)
                cbar.ax.set_ylabel(item,fontsize=16)
                ticklabs = cbar.ax.get_yticklabels()
                cbar.ax.set_yticklabels(ticklabs, fontsize=12)
                # plt.colorbar()
#                if gridding == 'on':
#                    plt.grid(b=True, which='major', linestyle='-', linewidth=0.5,color='k')
#                    plt.grid(b=True, which='minor', linestyle='-', linewidth=0.5,color='k')
##                    plt.clim(min(data),max(data)) 
                plt.xlabel('Horizontal Distance(m)',fontsize=16)
                plt.ylabel('Vertical Depth (m)',fontsize=16)
                plt.tick_params(axis='x', labelsize=12)
                plt.tick_params(axis='y', labelsize=12)
                # plt.clabel(cs2,fontsize=20)
                plt.tight_layout()
                
            
            # return data1,xi,yi
            os.chdir(self.saveloc) 
            fig.savefig(item + str(tre.time) +'.png',bbox_inches='tight',dpi=(600))
            
        if direction=='ZX':
            fig = plt.figure(figsize=(width,height))
            tre = toughreact_tecplot(self.filename,self.gridblock)
            if timer == None:
                tre.last()
            else:
                tre.set_time(timer)
            a = self.parameters
            params = self.convertlisttodict(a)
            for item, number in params.items():
                ax = fig.add_subplot(1,len(self.parameters),number)
                data = tre.element[item]
                X = tre.element['X(m)']
                Z = tre.element['Z(m)']
                xi,yi = np.meshgrid(Z,X)
                data1 = griddata((Z,X),data,(xi,yi),method='nearest')
                cs2 = plt.contourf(xi,yi,data1,100,  cmap='jet',extend='both')  
                plt.colorbar()
                plt.xlabel('Distance(m)',fontsize=16)
                plt.ylabel(item,fontsize=16)
                plt.tight_layout()
        
            os.chdir(self.saveloc) 
            fig.savefig(item + str(tre.time) +'.png',bbox_inches='tight',dpi=(600))
            
        if direction=='XY':
            fig = plt.figure(figsize=(width,height))
            tre = toughreact_tecplot(self.filename,self.gridblock)
            if timer == None:
                tre.last()
            else:
                tre.set_time(timer)
            a = self.parameters
            params = self.convertlisttodict(a)
            for item, number in params.items():
                ax = fig.add_subplot(1,len(self.parameters),number)
                data = tre.element[item]
                X = tre.element['X(m)']
                Y = tre.element['Y(m)']
                xi,yi = np.meshgrid(X,Y)
                data1 = griddata((X,Y),data,(xi,yi),method='nearest')
                cs2 = plt.contourf(xi,yi,data1,100,  cmap='jet',extend='both')  
                plt.colorbar()
                plt.xlabel('Distance(m)',fontsize=16)
                plt.ylabel(item,fontsize=16)
                plt.tight_layout()
        
            os.chdir(self.saveloc) 
            fig.savefig(item + str(tre.time) +'.png',bbox_inches='tight',dpi=(600))
            
        if direction=='YX':
            fig = plt.figure(figsize=(width,height))
            tre = toughreact_tecplot(self.filename,self.gridblock)
            if timer == None:
                tre.last()
            else:
                tre.set_time(timer)
            a = self.parameters
            params = self.convertlisttodict(a)
            for item, number in params.items():
                ax = fig.add_subplot(1,len(self.parameters),number)
                data = tre.element[item]
                X = tre.element['X(m)']
                Y = tre.element['Y(m)']
                xi,yi = np.meshgrid(Y,X)
                data1 = griddata((Y,X),data,(xi,yi),method='nearest')
                cs2 = plt.contourf(xi,yi,data1,100,  cmap='jet',extend='both')  
                plt.colorbar()
                plt.xlabel('Distance(m)',fontsize=16)
                plt.ylabel(item,fontsize=16)
                plt.tight_layout()
        
            os.chdir(self.saveloc) 
            fig.savefig(item + str(tre.time) +'.png',bbox_inches='tight',dpi=(600))
            
        if direction=='YZ':
            fig = plt.figure(figsize=(width,height))
            tre = toughreact_tecplot(self.filename,self.gridblock)
            if timer == None:
                tre.last()
            else:
                tre.set_time(timer)
            a = self.parameters
            params = self.convertlisttodict(a)
            for item, number in params.items():
                ax = fig.add_subplot(1,len(self.parameters),number)
                data = tre.element[item]
                Y = tre.element['Y(m)']
                Z = tre.element['Z(m)']
                xi,yi = np.meshgrid(Y,Z)
                data1 = griddata((Y,Z),data,(xi,yi),method='nearest')
                cs2 = plt.contourf(xi,yi,data1,100,  cmap='jet',extend='both')  
                plt.colorbar()
                plt.xlabel('Distance(m)',fontsize=16)
                plt.ylabel(item,fontsize=16)
                plt.tight_layout()
        
            os.chdir(self.saveloc) 
            fig.savefig(item + str(tre.time) +'.png',bbox_inches='tight',dpi=(600))
            
        if direction=='ZY':
            fig = plt.figure(figsize=(width,height))
            tre = toughreact_tecplot(self.filename,self.gridblock)
            if timer == None:
                tre.last()
            else:
                tre.set_time(timer)
            a = self.parameters
            params = self.convertlisttodict(a)
            for item, number in params.items():
                ax = fig.add_subplot(1,len(self.parameters),number)
                data = tre.element[item]
                Y = tre.element['Y(m)']
                Z = tre.element['Z(m)']
                xi,yi = np.meshgrid(Z,Y)
                data1 = griddata((Z,Y),data,(xi,yi),method='nearest')
                cs2 = plt.contourf(xi,yi,data1,100,  cmap='jet',extend='both')  
                plt.colorbar()
                plt.xlabel('Distance(m)',fontsize=16)
                plt.ylabel('Vertical Depth (m)',fontsize=16)
                plt.tight_layout()
        
            os.chdir(self.saveloc) 
            fig.savefig(item + str(tre.time) +'.png',bbox_inches='tight',dpi=(600))
    
    def twoinone(self,width,height,grid,direction,timer,color):   
            self.direction(width,height,grid,direction,timer,color)
    def threeinone(self,width,height,grid,direction,timer,color):   
            self.direction(width,height,grid,direction,timer,color)
    def oneinone(self,width,height,grid,direction,timer,color):   
            self.direction(width,height,grid,direction,timer,color)
    
    
    def plot2D(self,width,height,grid,direction,timer=None,color=None):
        if len(self.parameters)==1:
            self.oneinone(width,height,grid,direction,timer,color)
            #print(gridding)
        elif len(self.parameters)==2:
            self.twoinone(width,height,grid,direction,timer,color)
        elif len(self.parameters)==3:
            self.threeinone(width,height,grid,direction,timer,color)
            
    def getgridnumber(self,df,direction):
        X = df[direction]
        d ={}
        for i in X:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        m = list(d.keys())
        return m, len(d) 
    
    def cust_range(self,*args, rtol=1e-05, atol=1e-08, include=[True, False]):
        """
        Combines numpy.arange and numpy.isclose to mimic
        open, half-open and closed intervals.
        Avoids also floating point rounding errors as with
        >>> numpy.arange(1, 1.3, 0.1)
        array([1. , 1.1, 1.2, 1.3])
    
        args: [start, ]stop, [step, ]
            as in numpy.arange
        rtol, atol: floats
            floating point tolerance as in numpy.isclose
        include: boolean list-like, length 2
            if start and end point are included
        """
        # process arguments
        if len(args) == 1:
            start = 0
            stop = args[0]
            step = 1
        elif len(args) == 2:
            start, stop = args
            step = 1
        else:
            assert len(args) == 3
            start, stop, step = tuple(args)
    
        # determine number of segments
        n = (stop-start)/step + 1
    
        # do rounding for n
        if np.isclose(n, np.round(n), rtol=rtol, atol=atol):
            n = np.round(n)
    
        # correct for start/end is exluded
        if not include[0]:
            n -= 1
            start += step
        if not include[1]:
            n -= 1
            stop -= step
    
        return np.linspace(start, stop, int(n))

    def crange(self,*args, **kwargs):
        return self.cust_range(*args, **kwargs, include=[True, True])
    
    def orange(self,*args, **kwargs):
        return self.cust_range(*args, **kwargs, include=[True, False])
            
    def plot2D_withgrid(self,param,timer,direction='XZ'):
        if direction=='XZ':
            fig, ax = plt.subplots(1,1)
            tre = toughreact_tecplot(self.filename,self.gridblock)
            if timer == None:
                tre.last()
            else:
                print('yes')
                tre.set_time(timer)
            X = tre.element['X(m)']
            Y = tre.element['Y(m)']
            Z = tre.element['Z(m)']
            presenttime = str(tre.time)
            # param = tre.element[self.parameters[paramNum]]
            df = pd.DataFrame(index=range(len(X)))
            df['X'] = X
            df['Y'] = Y
            df['Z'] = Z
            Zvalues,Ztotal = self.getgridnumber(df,'Z')
            Yvalues,Ytotal = self.getgridnumber(df,'Y')
            Xvalues,Xtotal = self.getgridnumber(df,'X')
            xi,yi = np.meshgrid(X,Z)
            orig_data = tre.element[param]
            data = np.asarray(tre.element[param])
            data = data.reshape(Ztotal,Xtotal)
            data1 = griddata((X,Z),orig_data,(xi,yi),method='nearest')
            extent = [min(X), max(X), min(Z), max(Z)]
            cs2 = plt.imshow(np.reshape(data, newshape=(Ztotal,Xtotal)),cmap='coolwarm',interpolation='none');
            ax = plt.gca();
            # Major ticks
            x_tick = np.arange(0, Xtotal, 4)
            z_tick = np.arange(0, Ztotal, 1)
            Z_array = np.asarray(Z)
            Z_array = np.abs(Z_array)
            ax.set_xticks(x_tick)
            num_tick_x = len(x_tick)
            num_tick_z = len(z_tick)
            ax.set_yticks(z_tick)
            # Labels for major ticks
            tick_x = max(X)-min(X)
            tick_z = max(Z)-min(Z)
            ax.set_xticklabels(np.round(self.crange(min(X),max(X),tick_x/(num_tick_x-1)),2),fontsize=8);
            ax.set_yticklabels(np.round(self.crange(min(Z_array),max(Z_array),tick_z/(num_tick_z-1)),2),fontsize=8);
            # Minor ticks
            ax.set_xticks(np.arange(-.5, Xtotal, 1), minor=True);
            ax.set_yticks(np.arange(-.5,Ztotal, 1), minor=True);
            # Gridlines based on minor ticks
            ax.grid(which='minor', color='k', linestyle='-', linewidth=1)
            cbar = fig.colorbar(cs2,ax=ax,pad=0.2,orientation="horizontal")
            # cbar.ax.set_ylabel(param,fontsize=8)
            cbar.ax.set_title(param,fontsize=8)
            cbar.ax.tick_params(labelsize=8)
            cbar.ax.locator_params(nbins=7)
            plt.xlabel('Horizontal Distance(m)',fontsize=8)
            plt.ylabel('Vertical Depth (m)',fontsize=8)
            plt.tight_layout()
            print(presenttime)
            os.chdir(self.saveloc) 
            fig.savefig('Grid' +'.png',bbox_inches='tight',dpi=(600))
    
    def retrievedatadistance(self,direction,blocknumber):
        lst = self.parameters.copy()
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

    
    def colorcoding(self,style):
        markers = ["-o","-v","-^","-<","->","-1","-2","-3","-4","-8","-s","-p","-P","-*","-h","-H","-+","-x","-X","-D","-d","-|","-_"]
        if style.lower()=='publication':
            colormarker = 'k' + markers[random.randint(0,(len(markers)-1))]
        elif style.lower()=='presentation':
            colormarker = 'r' + markers[random.randint(0,(len(markers)-1))]
        return colormarker
    
    def retrievedatadistance2(self,face,Xaxisdirection,Xlayer,Ylayer,Zlayer,paramNum,timer):
        tre = toughreact_tecplot(self.filename,self.gridblock)
        if timer == None:
            tre.last()
        else:
            tre.set_time(timer)
        X = tre.element['X(m)']
        Y = tre.element['Y(m)']
        Z = tre.element['Z(m)']
        presenttime = str(tre.time)
        param = tre.element[self.parameters[paramNum]]
        df = pd.DataFrame(index=range(len(X)))
        df['X'] = X
        df['Y'] = Y
        df['Z'] = Z
        df[self.parameters[paramNum]] = param
        Z1,Z2 = self.getgridnumber(df,'Z')
        Y1,Y2 = self.getgridnumber(df,'Y')
        X1,X2 = self.getgridnumber(df,'X')
        if face == 'Z':  
            m = []
            n = []
            for index, row in df.iterrows():
                if df.iloc[index,2]!=Z1[Zlayer-1]:
                    m.append(index)
            df.drop(m, inplace=True)
            df = df.reset_index(drop=True)
            if Xaxisdirection == 'X':
                for index, row in df.iterrows():
                    if df.iloc[index,1]!=Y1[Ylayer-1]:
                        n.append(index)
                df.drop(n, inplace=True)
                df = df.reset_index(drop=True)
            if Xaxisdirection == 'Y':
                for index, row in df.iterrows():
                    if df.iloc[index,0]!=X1[Xlayer-1]:
                        n.append(index)
                df.drop(n, inplace=True)
                df = df.reset_index(drop=True)
        if face == 'Y':  
            m = []
            n = []
            for index, row in df.iterrows():
                if df.iloc[index,1]!=Y1[Ylayer-1]:
                    m.append(index)
            df.drop(m, inplace=True)
            df = df.reset_index(drop=True)
            if Xaxisdirection == 'X':
                for index, row in df.iterrows():
                    if df.iloc[index,2]!=Z1[Zlayer-1]:
                        n.append(index)
                df.drop(n, inplace=True)
                df = df.reset_index(drop=True)
            if Xaxisdirection == 'Z':
                for index, row in df.iterrows():
                    if df.iloc[index,0]!=X1[Xlayer-1]:
                        n.append(index)
                df.drop(n, inplace=True)
                df = df.reset_index(drop=True)
                
        if face == 'X':
            m = []
            n = []
            for index, row in df.iterrows():
                if df.iloc[index,0]!=X1[Xlayer-1]:
                    m.append(index)
            df.drop(m, inplace=True)
            df = df.reset_index(drop=True)
            if Xaxisdirection == 'Z':
                for index, row in df.iterrows():
                    if df.iloc[index,1]!=Y1[Ylayer-1]:
                        n.append(index)
                df.drop(n, inplace=True)
                df = df.reset_index(drop=True)
            if Xaxisdirection == 'Y':
                for index, row in df.iterrows():
                    if df.iloc[index,2]!=Z1[Zlayer-1]:
                        n.append(index)
                df.drop(n, inplace=True)
                df = df.reset_index(drop=True)
                
        return presenttime,df
    
    def plotstylingdistance(self,df,Xdirection,paramNum,presenttime,width=8,height=8):
        
        '''
        This method styles distance plots
        '''
        matplotlib.rc('xtick', labelsize=14) 
        matplotlib.rc('ytick', labelsize=14)
        fig = plt.figure(figsize=(width,height))
        plt.plot(df[Xdirection],df[self.parameters[paramNum]])
        plt.grid()
        plt.xlim(min(df[Xdirection]),min(df[Xdirection])+1)
        plt.xlabel('Distance(m)',fontsize=16)
        plt.ylabel(self.parameters[paramNum],fontsize=16)
        os.chdir(self.saveloc) 
        fig.savefig(self.parameters[paramNum] + presenttime +'.png',bbox_inches='tight',dpi=(600))
        

    def plotdistance(self,face,Xaxisdirection,Xlayer,Ylayer,Zlayer,paramNum,timer=None):
        '''
        This method makes plot of parameters with distance
        '''
        presenttime,df = self.retrievedatadistance2(face,Xaxisdirection,Xlayer,Ylayer,Zlayer,paramNum,timer)
        print('time is ' + str(timer))
        if face == 'Z': 
            if Xaxisdirection == 'X':
                self.plotstylingdistance(df,Xaxisdirection,paramNum,presenttime)
            if Xaxisdirection == 'Y':
                self.plotstylingdistance(df,Xaxisdirection,paramNum,presenttime)
        if face == 'Y': 
            if Xaxisdirection == 'X':
                self.plotstylingdistance(df,Xaxisdirection,paramNum,presenttime)
            if Xaxisdirection == 'Z':
                self.plotstylingdistance(df,Xaxisdirection,paramNum,presenttime)
        if face == 'X': 
            if Xaxisdirection == 'Z':
                self.plotstylingdistance(df,Xaxisdirection,paramNum,presenttime)
            if Xaxisdirection == 'Y':
                self.plotstylingdistance(df,Xaxisdirection,paramNum,presenttime)
                
    def plotdistancemultiple(self,face,Xaxisdirection,Xlayer,Ylayer,Zlayer,timer=None):
        width = 8
        height = 8
        fig = plt.figure(figsize=(width,height))
        axs = plt.subplot(1,1,1)
        for i in range(0,len(self.parameters)):
            presenttime,df = self.retrievedatadistance2(face,Xaxisdirection,Xlayer,Ylayer,Zlayer,i,timer)
            matplotlib.rc('xtick', labelsize=14) 
            matplotlib.rc('ytick', labelsize=14)
            axs.plot(df[Xaxisdirection],df[self.parameters[i]])
            plt.xlabel('Distance(m)',fontsize=16)
            plt.ylabel('Change in volume fraction ',fontsize=16)
#            plt.setp(axs.get_legend().get_texts(), fontsize='10')
            axs.grid(True,which='both')
            # axs.minorticks_on()
            # plt.minorticks_on()
            # axs.grid(b=True, which='major', linestyle='-', linewidth=0.5,color='k')
            # axs.grid(b=True, which='minor', linestyle='-', linewidth=0.1)
#            axs.set_title(self.prop[number-1])
            axs.spines['bottom'].set_linewidth(1.5)
            axs.spines['left'].set_linewidth(1.5)
            axs.spines['top'].set_linewidth(0)
            axs.spines['right'].set_linewidth(0)
            plt.legend(self.parameters.capitalize(), prop={'size': 16})
            plt.grid()
            os.chdir(self.saveloc) 
        fig.savefig(self.parameters[i] + presenttime +'.png',bbox_inches='tight',dpi=(600))
        
    def plotdistancemultiplefiles(self,face,Xaxisdirection,Xlayer,Ylayer,Zlayer,locations,labels,timer=None):
#        plt.rc('legend', fontsize='small')
        j = 0
        fontP = FontProperties()
        fontP.set_size(10)
        width = 12
        height = 8
        colors=['r','royalblue','g','k','c','m','y']
        markers = ["o","v","^","<",">","1","2","3","4","8","s","p","P","*","h","H","+","x","X","D","d","|","_"]
#        fig = plt.figure(figsize=(width,height))
        fig = plt.figure(figsize=(width,height))
#        font = {'family' : 'normal','size'   : 10}
#        matplotlib.rc('font', **font)
        counter =1
        for file in locations:
            axs = plt.subplot(3,2,counter)
            k=0
            l=0
            os.chdir(file)    
            # print(file)
            lama =self.parameters.copy()
            for i in range(0,len(self.parameters)): 
                presenttime,df = self.retrievedatadistance2(face,Xaxisdirection,Xlayer,Ylayer,Zlayer,i,timer)
                # matplotlib.rc('xtick', labelsize=8) 
                # matplotlib.rc('ytick', labelsize=8)
                if i<len(self.parameters)-1:
                    axs.plot(df[Xaxisdirection],df[self.parameters[i]],color =colors[l],marker=markers[l],label=self.parameters[i].capitalize())
                    plt.xticks(fontsize=12)
                    plt.yticks(fontsize=12)
                    plt.xlabel('Distance(m)',fontsize=12)
                    plt.ylabel('Change in volume fraction ',fontsize=12)
                else:
                    axs2 = axs.twinx()
                    axs2.plot(df[Xaxisdirection],df[self.parameters[i]],color =colors[l],marker=markers[l],label=self.parameters[i].capitalize())
                    plt.xticks(fontsize=12)
                    plt.yticks(fontsize=12)
                    plt.xlabel('Distance(m)',fontsize=12)
                    # Get the y limits
                    ymin, ymax = min(df[self.parameters[i]]), max(df[self.parameters[i]])
                    
                    # Set the y limits making the maximum 5% greater
                    # plt.ylim(ymin, 1.05 * ymax)
                    plt.ylim(0.2, 0.45)
                    plt.ylabel(self.parameters[i],fontsize=12)
                    # axs2.legend(loc='best',prop=fontP)
                    axs2.spines['left'].set_linewidth(1.5)
                    axs2.spines['top'].set_linewidth(0)
                    axs2.spines['right'].set_linewidth(1.5)
                    axs2.spines['bottom'].set_linewidth(1.5)
                    # axs2.grid(b=False)
                # plt.setp(axs.get_legend().get_texts(), fontsize='10')
                # axs.grid(True,which='both')
                # axs.minorticks_on()
                # plt.minorticks_on()
                # axs.grid(b=True, which='major', linestyle='-', linewidth=0.5,color='k')
                # axs.grid(b=True, which='minor', linestyle='-', linewidth=0.1)
#               axs.set_title(self.prop[number-1])
                axs.spines['bottom'].set_linewidth(1.5)
                axs.set_title(labels[j], fontsize='14')
                lama[i]=lama[i].capitalize()
                axs.spines['left'].set_linewidth(1.5)
                axs.spines['top'].set_linewidth(0)
                axs.spines['right'].set_linewidth(0)
                # axs.legend(loc='center right',prop=fontP)
                # plt.legend(lama, prop={'size': 10})
                # plt.grid()
                l=l+1
            j=j+1
            counter =counter+1
            fig.tight_layout()
            k=k+1
        plt.subplots_adjust(left  = 0.125,wspace = 0.4,top = 0.95)
        os.chdir(self.saveloc) 
        handles, labels = axs.get_legend_handles_labels()
        handles2, labels2 = axs2.get_legend_handles_labels()
        handles.append(handles2[0])
        labels.append(labels2[0])
        # print(type(labels),handles)
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
        fig.savefig(self.parameters[i] + presenttime +'.png',bbox_inches='tight',dpi=(600)) 
        

            
    def plotsingle(self,direction,blocknumber,width=8,height=8,linestyle='dashed',purpose='presentation'):
        matplotlib.rc('xtick', labelsize=14) 
        matplotlib.rc('ytick', labelsize=14)
        dictionary,lst = self.retrievedatadistance(direction,blocknumber)
        fig = plt.figure(figsize=(width,height))
        colorcode = self.colorcoding(purpose)
        for i in range(0,len(lst)-1):
            colorcode = self.colorcoding(purpose)
            mana = dictionary[lst[0]]
            mana2 = dictionary[lst[i+1]]
            plt.plot(mana[0],mana2[0],colorcode,linestyle=linestyle)
            plt.legend(lst[1:len(lst)-1], prop={'size': 16})
        plt.grid()
#        plt.xlabel('Distance (meters) ',fontsize=14,fontweight='bold')
#        plt.ylabel('property',fontsize=14,fontweight='bold')
        os.chdir(self.saveloc) 
        fig.savefig(lst[i]+'.png',bbox_inches='tight',dpi=(600))
        
    def forparaview(self,geo):
        filenamepara = 'trial.pvd'
        tre = toughreact_tecplot(self.filename,self.gridblock)
        tre.write_vtk(geo, filenamepara)
        
        
    def threeinonepitz(self,width,height,grid,color='r--'):
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
            X = tre.element['X']
            Y = tre.element['Y']
            Z = tre.element['Z']
            xi,yi = np.meshgrid(X,Y)
            data1 = griddata((X,Y),data,(xi,yi),method='linear')
            #levels = [-4, -3, -2, -1, 1, 2, 3, 4]
            cs2 = plt.contourf(xi,yi,data1,100,  cmap='jet',extend='both') 
            plt.axis('tight') 
            plt.colorbar()
            plt.xlabel('Distance(m)',fontsize=16)
            plt.ylabel(item,fontsize=16)
            plt.tight_layout()
            
        os.chdir(self.saveloc) 

        fig.savefig(item +'.png',bbox_inches='tight',dpi=(600))
    
    def sixinone(self,width,height,grid,color='r--'):
        """
        This method plots six figures in a plot window and saves them with the name of the last item on the
        list
        flowr
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
            
        os.chdir(self.saveloc) 

        fig.savefig(item +'.png',bbox_inches='tight',dpi=(600)) 
        
        
"""
# commented former code

#    def threeinone(self,width,height,grid,color='r--'):
#        
"""
#        This method plots three figures in a plot window and saves them with the name of the last item on the
#        list
#        
#        width -> the width of the subplot
#        height -> the height of the subplot
#        grid -> the name of the block in the TOUGHREACT flow input
#        color -> color is optional but if provided color of plot can be manipulated
#        """
#        fig = plt.figure(figsize=(width,height))
#        tre = toughreact_tecplot(self.filename,self.gridblock)
#        tre.last()
#        tre.time
#        a = self.parameters
#        params = self.convertlisttodict(a)
#        for item, number in params.items():
#            ax = fig.add_subplot(1,3,number)
#            data = tre.element[item]
#            X = tre.element['X(m)']
#            Y = tre.element['Y(m)']
#            Z = tre.element['Z(m)']
#            Z = Z[::-1]
#            xi,yi = np.meshgrid(X,Z)
#            data1 = griddata((X,Z),data,(xi,yi),method='nearest')
#            #levels = [-4, -3, -2, -1, 1, 2, 3, 4]
#            cs2 = plt.contourf(xi,yi,data1,100,  cmap='jet',extend='both')  
#            plt.colorbar()
#            plt.xlabel('Distance(m)',fontsize=16)
#            plt.ylabel(item,fontsize=16)
#            plt.gca().invert_yaxis()
#            plt.tight_layout()
#            
#        os.chdir(self.saveloc) 
#        fig.savefig(item +'.png',bbox_inches='tight',dpi=(600)) 
        

        
#    def twoinone(self,width,height,grid,color='r--'):
#        """
#        This method plots three figures in a plot window and saves them with the name of the last item on the
#        list
#        
#        width -> the width of the subplot
#        height -> the height of the subplot
#        grid -> the name of the block in the TOUGHREACT flow input
#        color -> color is optional but if provided color of plot can be manipulated
#        """
#        fig = plt.figure(figsize=(width,height))
#        tre = toughreact_tecplot(self.filename,self.gridblock)
#        tre.last()
#        tre.time
#        a = self.parameters
#        params = self.convertlisttodict(a)
#        for item, number in params.items():
#            ax = fig.add_subplot(1,2,number)
#            data = tre.element[item]
#            X = tre.element['X(m)']
#            Y = tre.element['Y(m)']
#            Z = tre.element['Z(m)']
#            Z = Z[::-1]
#            xi,yi = np.meshgrid(X,Z)
#            data1 = griddata((X,Z),data,(xi,yi),method='nearest')
#            #levels = [-4, -3, -2, -1, 1, 2, 3, 4]
#            cs2 = plt.contourf(xi,yi,data1,100,  cmap='jet',extend='both')  
#            plt.colorbar()
#            plt.xlabel('Distance(m)',fontsize=16)
#            plt.ylabel(item,fontsize=16)
#            plt.gca().invert_yaxis()
#            plt.tight_layout()
#            
#        os.chdir(self.saveloc) 
#        fig.savefig(item +'.png',bbox_inches='tight',dpi=(600))
        
#    def oneinone(self,width,height,grid,color='r--'):
#        """
#        This method plots three figures in a plot window and saves them with the name of the last item on the
#        list
#        
#        width -> the width of the subplot
#        height -> the height of the subplot
#        grid -> the name of the block in the TOUGHREACT flow input
#        color -> color is optional but if provided color of plot can be manipulated
#        """
#        fig = plt.figure(figsize=(width,height))
#        tre = toughreact_tecplot(self.filename,self.gridblock)
#        tre.last()
#        tre.time
#        a = self.parameters
#        params = self.convertlisttodict(a)
#        for item, number in params.items():
#            data = tre.element[item]
#            X = tre.element['X(m)']
#            Y = tre.element['Y(m)']
#            Z = tre.element['Z(m)']
#            Z = Z[::-1]
#            xi,yi = np.meshgrid(X,Z)
#            data1 = griddata((X,Z),data,(xi,yi),method='nearest')
#            #levels = [-4, -3, -2, -1, 1, 2, 3, 4]
#            cs2 = plt.contourf(xi,yi,data1,100,  cmap='jet',extend='both')  
#            plt.colorbar()
#            plt.xlabel('Distance(m)',fontsize=16)
#            plt.ylabel(item,fontsize=16)
#            plt.gca().invert_yaxis()
#            plt.tight_layout()
#            
#        os.chdir(self.saveloc) 
#        fig.savefig(item +'.png',bbox_inches='tight',dpi=(600))
