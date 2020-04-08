# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 13:34:29 2020

@author: tajayi3
"""

import itertools
import os
import shutil

class toughtotmvoc(object):
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
        
import fortranformat as ff
header_line = ff.FortranRecordWriter('(A15, A15, A15)')
header_line.write(['x', 'y', 'z'])
line =ff.FortranRecordWriter('(3F15.3)')
line.write([1.0, 0.0, 0.5])
line.write([1.1, 0.1, 0.6])
with open('testfile.txt', "r") as f1:
    contents = f1.readlines()
f1.close()
word2 = 'REACT'
#        REACT = '00021'
contents.insert(1, word2)
contents.insert(2, line.write([1.1, 0.1, 0.6]))
with open('testfile.txt', 'w') as f:
    for item in contents:
        f.write("%s" % item)
        f.write("\n")