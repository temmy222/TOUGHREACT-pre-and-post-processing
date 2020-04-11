# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 13:34:29 2020

@author: tajayi3
"""
from __future__ import print_function
import itertools
import os
import shutil
import fortranformat as ff
import numpy as np



from fixed_format_file import *
from t2grids import *
from t2incons import *
from math import ceil
import struct


data_struct = {
    'CHEMP.1': [['num_HC'], ['I5']],
    'CHEMP.2': [['HCNAME'], ['A20']],
    'CHEMP.3': [['TCRITM', 'PCRITM', 'ZCRITM', 'OMEGAM', 'DIPOLMM'], ['5E10.4']],
    'CHEMP.4': [['TBOILM', 'VPAM', 'VPBM', 'VPCM', 'VPDM'], ['5E10.4']],
    'CHEMP.5': [['AMWTM', 'CPAM', 'CPBM', 'CPCM', 'CPDDM'], ['5E10.4']],
    'CHEMP.6': [['RHOREFM', 'TDENREF', 'DIFV0M', 'TDIFREF', 'TEXPOM'], ['5E10.4']],
    'CHEMP.7': [['VLOAM', 'VLOBM', 'VLOCM', 'VLODM', 'VOLCRITM'], ['5E10.4']],
    'CHEMP.8': [['SOLAM', 'SOLBM', 'SOLCM', 'SOLDM'], ['4E10.4']],
    'CHEMP.9': [['OCKM', 'FOXM', 'ALAMM'], ['3E10.4']],
    'NCGAS': [['num_noncond_gas'], ['I5']],
    'NCGAS.2': [['NCGAS_NAMES'], ['I5']],
}  

class toughtotmvoc(object):
    def __init__  (self,location=None,destination=None,filename=None):
        
        """
        An instance of this class takes in three parameters;
        
        location --> the current direction where the simulations have been carried out
        destination ---> the directory containing PYTOUGH and its class which would be needed for 
        manipulations
        filenames -> the flow.inp file which is to be converted into TOUGHREACT
        """
        self.location = location
        self.destination = destination
        self.filename = filename
#        self.hydrocarbon = numHC
        self.componentlist = []
        self.component = {}
        
#        chemp2={'HCNAMES':self.hydrocarbon}
        
    def hasNumbers(self,inputString):
        return any(char.isdigit() for char in inputString)

    def getparamandline(self,file):
        file=self.filename
        with open(file, "r") as f1:
            contents = f1.readlines()
        for i in range(len(contents)):
            contents[i] = contents[i].split()
        teste = []
        for i in range(len(contents)):
            maxa =[]
            for j in range(len(contents[i])):
                maxa.append(self.hasNumbers(contents[i][j]))
            if True in maxa:
                teste.append(True)
            else:
                teste.append(False)
        final =[]
        for index,value in enumerate(teste):
            if value==False:
                final.append(contents[index])
    
        str_list = list(filter(None, final)) 
        indexa =[]
        for i in range(len(str_list)):
            with open(file) as f:
                content = f.readlines()   
            index = [x for x in range(len(content)) if str_list[i][0] in content[x].upper()]   
            indexa.append(index)
        macre = list(zip(str_list,indexa))
        paramkey=[]
        paramvalue=[]
        for i in macre:
            paramkey.append(i[0][0])
            paramvalue.append(i[1][0])
    
        macre_new= dict(zip(paramkey,paramvalue))
        return macre_new
        
    def add_component(self, component = None):
        """Adds a generator."""
        if component is None: component = tmvoccomponent()
        self.componentlist.append(component)
        self.component[(component.hydrocarbon_name)] = self.componentlist[-1]
            
    def write_value(self,formatt,value):
        header_line = ff.FortranRecordWriter(formatt)
        if isinstance(value,int) or isinstance(value,str):
            mane = header_line.write([value])
        else:
            mane = header_line.write(value)
        return mane
        
    def write_component(self):
        paramlocation =self.getparamandline(self.filename)
        with open(self.filename, "r") as f1:
            contents = f1.readlines()
            f1.close()
            linestart = paramlocation.get('PARAM')
            for i in chemp:
                dem = self.write_value(formatt,value)
                contents.insert(linestart,dem)
                linestart+=1
            with open('testfile2.txt', 'w') as f:
                for index,item in enumerate(contents):
                    f.write("%s" % item)
                    if index ==10 or index==11:
                        f.write("\n")
            f.close()
                
        
class tmvoccomponent(object):
    def __init__  (self,num_hydrocarbon=0,
                   hydrocarbon_name='',
                   crit_T=None,crit_P=None,crit_Z=None,pitz_acen_fact=None,chem_dipole_moment=None,
                   boil_T=None,vap_pres_const_A=None,vap_pres_const_B=None,vap_pres_const_C=None,vap_pres_const_D=None,
                   mol_weight=None,heat_cap_A=None,heat_cap_B=None,heat_cap_C=None,heat_cap_D=None,
                   liq_dens=None,ref_T=None,ref_diffusivity=None,ref_T_gas_diffusivity=None,exp_chem_diffusivity=None,
                   vis_const_A=None,vis_const_B=None,vis_const_C=None,vis_const_D=None,chem_crit_volume=None,
                   chem_solu_const_A=None,chem_solu_const_B=None,chem_solu_const_C=None,chem_solu_const_D=None,
                   partition_coef=None,frac_carb_soil=None,decay_const_biodeg=None):
        self.hydrocarbon = num_hydrocarbon
        self.hydrocarbon_name = hydrocarbon_name
        self.crit_T = crit_T
        self.crit_P=crit_P
        self.crit_Z = crit_Z
        self.pitz_acen_fact=pitz_acen_fact
        self.chem_dipole_moment = chem_dipole_moment
        self.boil_T=boil_T
        self.vap_pres_const_A = vap_pres_const_A
        self.vap_pres_const_B=vap_pres_const_B
        self.vap_pres_const_C=vap_pres_const_C
        self.vap_pres_const_D=vap_pres_const_D
        self.mol_weight =mol_weight
        self.heat_cap_A=heat_cap_A
        self.heat_cap_B=heat_cap_B
        self.heat_cap_C=heat_cap_C
        self.heat_cap_D=heat_cap_D
        self.liq_dens=liq_dens
        self.ref_T=ref_T
        self.ref_diffusivity=ref_diffusivity
        self.ref_T_gas_diffusivity =ref_T_gas_diffusivity
        self.exp_chem_diffusivity =exp_chem_diffusivity
        self.vis_const_A=vis_const_A
        self.vis_const_B=vis_const_B
        self.vis_const_C=vis_const_C
        self.vis_const_D=vis_const_D
        self.chem_crit_volume=chem_crit_volume
        self.chem_solu_const_A =chem_solu_const_A
        self.chem_solu_const_B =chem_solu_const_B
        self.chem_solu_const_C=chem_solu_const_C
        self.chem_solu_const_D=chem_solu_const_D
        self.partition_coef=partition_coef
        self.frac_carb_soil=frac_carb_soil
        self.decay_const_biodeg=decay_const_biodeg
#        self.chemp1={'numhc':self.hydrocarbon}
#        self.chemp2={'HCNAMES':self.hydrocarbon_name}
#        self.chemp3={'crit_T':self.crit_T,'crit_P':self.crit_P}
#        layers = [chemp1,chemp2,chemp3,chemp4,chemp5,chemp6,chemp7,chemp8,chemp9]
        self.chemp1=[self.hydrocarbon]
        self.chemp2=[self.hydrocarbon_name]
        self.chemp3=[self.crit_T,self.crit_P,crit_Z,pitz_acen_fact,chem_dipole_moment]
        self.chemp4=[self.boil_T,self.vap_pres_const_A,self.vap_pres_const_B,self.vap_pres_const_C,self.vap_pres_const_D]
        self.chemp5=[self.mol_weight,self.heat_cap_A,self.heat_cap_B,self.heat_cap_C,self.heat_cap_D]
        self.chemp6=[self.liq_dens,self.ref_T,self.ref_diffusivity,self.ref_T_gas_diffusivity,self.exp_chem_diffusivity]
        self.chemp7=[self.vis_const_A,self.vis_const_B,self.vis_const_C,self.vis_const_D]
        self.chemp8=[self.chem_solu_const_A,self.chem_solu_const_B,self.chem_solu_const_C,self.chem_solu_const_D]
        self.chemp9=[self.partition_coef,self.frac_carb_soil,self.decay_const_biodeg]
        self.chemp = {'chemp1':self.chemp1,'chemp2':self.chemp2,'chemp3':self.chemp3,'chemp4':self.chemp4,'chemp5':self.chemp5,
                      'chemp6':self.chemp6,'chemp7':self.chemp7,'chemp8':self.chemp8,'chemp9':self.chemp9}
    def __repr__(self): return self.hydrocarbon_name

toluene = tmvoccomponent()

'''        
def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)
def getparamandline(file):
    with open(file, "r") as f1:
        contents = f1.readlines()
    for i in range(len(contents)):
        contents[i] = contents[i].split()
    teste = []
    for i in range(len(contents)):
        maxa =[]
        for j in range(len(contents[i])):
            maxa.append(hasNumbers(contents[i][j]))
        if True in maxa:
            teste.append(True)
        else:
            teste.append(False)
    final =[]
    for index,value in enumerate(teste):
        if value==False:
            final.append(contents[index])

    str_list = list(filter(None, final)) 
    indexa =[]
    for i in range(len(str_list)):
        with open(file) as f:
            content = f.readlines()   
        index = [x for x in range(len(content)) if str_list[i][0] in content[x].upper()]   
        indexa.append(index)
    macre = list(zip(str_list,indexa))
    paramkey=[]
    paramvalue=[]
    for i in macre:
        paramkey.append(i[0][0])
        paramvalue.append(i[1][0])
    
    macre_new= dict(zip(paramkey,paramvalue))
    return macre_new



def write_value(formatt,value):
    header_line = ff.FortranRecordWriter(formatt)
    if isinstance(value,int) or isinstance(value,str):
        mane = header_line.write([value])
    else:
        mane = header_line.write(value)
    return mane
    
def editline():
    with open('testfile.txt') as fin, open('output','w') as fout:
        lines = fin.readlines()
        for line in fin:
            fout.write(line)
            if line.startswith('PARAM'):
               next_line = next(fin)
               fout.write('my_line\n')
               fout.write(next_line)
           



header_line = ff.FortranRecordWriter('(A15, A15, A15)')
header_line.write(['x', 'y', 'z'])
line =ff.FortranRecordWriter('(3F15.5)')
m = line.write([1.0, 0.0, 0.5])
n = line.write([1.1, 0.1, 0.6])          
with open('testfile2.txt', "r") as f1:
    contents = f1.readlines()
    f1.close()
    word2 = 'REACT'
    #        REACT = '00021'
    contents.insert(10, m)
    contents.insert(11, n)
    with open('testfile2.txt', 'w') as f:
        for index,item in enumerate(contents):
            f.write("%s" % item)
            if index ==10 or index==11:
                f.write("\n")
    f.close()     


values = []
with open('testfile.txt', "r") as f1:
    contents = f1.readlines()
for i in range(len(contents)):
    contents[i] = contents[i].split()
for i in range(len(contents)):
    if len(contents[i])==1 and isinstance(contents[i][0],str):
        values.append(contents[i])

#f1.close()
#word2 = 'REACT'
##        REACT = '00021'
#contents.insert(1, word2)
#contents.insert(2, line.write([1.1, 0.1, 0.6]))
#with open('testfile.txt', 'w') as f:
#    for item in contents:
#        f.write("%s" % item)
#        f.write("\n")
        

#file.seek(line_offset[n])
        
'''