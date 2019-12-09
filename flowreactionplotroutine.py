# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:02:10 2019

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
    
    def direction(self,width,height,grid,direction,color='r--'):
        if direction=='XZ':
            fig = plt.figure(figsize=(width,height))
            tre = toughreact_tecplot(self.filename,self.gridblock)
            tre.last()
            a = self.parameters
            params = self.convertlisttodict(a)
            for item, number in params.items():
                ax = fig.add_subplot(1,len(self.parameters),number)
                data = tre.element[item]
                X = tre.element['X(m)']
                Z = tre.element['Z(m)']
                xi,yi = np.meshgrid(X,Z)
                data1 = griddata((X,Z),data,(xi,yi),method='nearest')
                cs2 = plt.contourf(xi,yi,data1,100,  cmap='coolwarm',extend='both')  
                plt.colorbar()
                plt.xlabel('Distance(m)',fontsize=16)
                plt.ylabel(item,fontsize=16)
                plt.tight_layout()
        
            os.chdir(self.saveloc) 
            fig.savefig(item + str(tre.time) +'.png',bbox_inches='tight',dpi=(600))
            
        if direction=='ZX':
            fig = plt.figure(figsize=(width,height))
            tre = toughreact_tecplot(self.filename,self.gridblock)
            tre.last()
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
            tre.last()
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
            tre.last()
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
            tre.last()
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
            tre.last()
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
                plt.ylabel(item,fontsize=16)
                plt.tight_layout()
        
            os.chdir(self.saveloc) 
            fig.savefig(item + str(tre.time) +'.png',bbox_inches='tight',dpi=(600))
    
    def twoinone(self,width,height,grid,direction,color='r--'):   
            self.direction(width,height,grid,direction,color='r--')
    def threeinone(self,width,height,grid,direction,color='r--'):   
            self.direction(width,height,grid,direction,color='r--')
    def oneinone(self,width,height,grid,direction,color='r--'):   
            self.direction(width,height,grid,direction,color='r--')
    
    def plot2D(self,width,height,grid,direction,color='r--'):
        if len(self.parameters)==1:
            self.oneinone(width,height,grid,direction,color='r--')
        elif len(self.parameters)==2:
            self.twoinone(width,height,grid,direction,color='r--')
        elif len(self.parameters)==3:
            self.threeinone(width,height,grid,direction,color='r--')
            
    
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
    
    def colorcoding(self,style):
        markers = ["-o","-v","-^","-<","->","-1","-2","-3","-4","-8","-s","-p","-P","-*","-h","-H","-+","-x","-X","-D","-d","-|","-_"]
        if style.lower()=='publication':
            colormarker = 'k' + markers[random.randint(0,(len(markers)-1))]
        elif style.lower()=='presentation':
            colormarker = 'r' + markers[random.randint(0,(len(markers)-1))]
        return colormarker
    
    def retrievedatadistance2(self,face,Xaxisdirection,Xlayer,Ylayer,Zlayer,paramNum):
        tre = toughreact_tecplot(self.filename,self.gridblock)
        tre.last()
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
        plt.xlabel('Distance(m)',fontsize=16)
        plt.ylabel(self.parameters[paramNum],fontsize=16)
        os.chdir(self.saveloc) 
        fig.savefig(self.parameters[paramNum] + presenttime +'.png',bbox_inches='tight',dpi=(600))
        

    def plotdistance(self,face,Xaxisdirection,Xlayer,Ylayer,Zlayer,paramNum):
        '''
        This method makes plot of parameters with distance
        '''
        presenttime,df = self.retrievedatadistance2(face,Xaxisdirection,Xlayer,Ylayer,Zlayer,paramNum)
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
