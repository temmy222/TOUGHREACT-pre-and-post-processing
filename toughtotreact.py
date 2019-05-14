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
        self.location = location
        self.destination = destination
        self.filename = filename
        
    def converttotreact(self):
#        word = 'START'
        with open(self.filename, "r") as f1:
            contents = f1.readlines()
        f1.close()
        word2 = 'REACT'
        word3 = '00021'
        contents.insert(10, word2)
        contents.insert(11, word3)
        with open(self.filename, 'w') as f:
            for item in contents:
                f.write("%s" % item)
                if word2 in item:
                    f.write("\n")
                if word3 in item:
                    f.write("\n")
        f.close()
        
    def find(namer):
        for root, dirs, files in os.walk(self.destination):
            if namer in files:
                return os.path.join(root, namer)
            
    def copyfile(self,filename):
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