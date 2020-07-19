# -*- coding: utf-8 -*-
"""
Created on Wed May  8 20:36:11 2019

@author: tajayi3
"""
import itertools
import os
import shutil

class toughtotoughreact(object):
    def __init__  (self,location,destination,filename):
        
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
        
    def converttotreact(self,REACT='00021'):
#        word = 'START'
        """
        This method converts the TOUGH2 flow.inp file into its equivalent for TOUGHREACT
        
        """
        with open(self.filename, "r") as f1:
            contents = f1.readlines()
        f1.close()
        word2 = 'REACT'
#        REACT = '00021'
        contents.insert(10, word2)
        contents.insert(11, REACT)
        with open(self.filename, 'w') as f:
            for item in contents:
                f.write("%s" % item)
                if word2 in item:
                    f.write("\n")
                if REACT in item:
                    f.write("\n")
        f.close()
        
    def converttotreactpitzer(self,REACT='0002005000020000000'):
#        word = 'START'
        """
        This method converts the TOUGH2 flow.inp file into its equivalent for TOUGHREACT
        
        """
        with open(self.filename, "r") as f1:
            contents = f1.readlines()
        f1.close()
        word2 = 'REACT'
#        REACT = '00021'
        contents.insert(10, word2)
        contents.insert(11, REACT)
        with open(self.filename, 'w') as f:
            for item in contents:
                f.write("%s" % item)
                if word2 in item:
                    f.write("\n")
                if REACT in item:
                    f.write("\n")
        f.close()
        
    def find(self,namer):
        for root, dirs, files in os.walk(self.destination):
            if namer in files:
                return os.path.join(root, namer)
            
    def copyfile(self,filename):
        """
        This method copies single file from the location to the destination folder. it takes in a a single argument
        
        filename -> the name of the file to be transferred
        """
        #copy specific file
        src_files = os.listdir(self.location)
        for file_name in src_files:
            if file_name == filename:
                full_file_name = os.path.join(self.location, file_name)
                if (os.path.isfile(full_file_name)):
                    shutil.copy(full_file_name, self.destination)



#    for num, line in enumerate(f1, 1):
#        if word in line:
#            print ('...word found...')
#            point1 = num

#f = open("flow2.inp", "w")
#contents = "".join(contents)
#f.write(contents)
#f.close()

#dest = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Cement Flow through 2 - Gherardi-Sea Water"
#
#loc = r"C:\Users\tajayi3\Desktop\Research\Software\PyTOUGH-master"
#
#filename = "flow.inp"
#
#tre = toughtotoughreact(loc,dest,filename)
#
#tre.converttotreact()
