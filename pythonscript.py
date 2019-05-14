# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 19:30:14 2019

@author: tajayi3
"""
#
#import pandas as pd
#sample_data = pd.read_csv('kdd_min.tec')

import pandas as pd
import re
data = [] 
with open('kdd_min.txt','r') as file:
    file_contents = file.read()
#    print(file_contents)
    line = file.readline()