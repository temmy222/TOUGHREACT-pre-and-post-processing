# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 17:42:55 2020

@author: tajayi3
"""
import os
file = r"C:\Users\tajayi3\OneDrive - Louisiana State University\GOM Shale Cement flow with Batch\Gulf of Mexico Shale Cement Flow - NaCl brine"
os.chdir(file)
f = open("iter.out","r")
m = f.readlines()
data = m[15:]
for i in range(len(data)):
    data[i] = data[i].split()