# -*- coding: utf-8 -*-
"""
Created on Tue May  7 10:43:10 2019

@author: tajayi3
"""

import fileinput
filename = 'chemical.inp'
text_to_search = 'co2'
replacement_text =  "'h2o'"

outfile= open("chemical.inp","w+")
outfile.write('#Title\n')
outfile.write('Transport of NaCl solution\n\n')
outfile.write("'h2o'  0 \n")
outfile.write("'na+'  0 \n")
outfile.write("'cl-'  0 \n")
outfile.write("'*'  0 \n")
outfile.write("'*'  0 \n")
outfile.write("'*'  0 \n")
outfile.write("'*'  0 \n")
outfile.write("co2(g)  1 \n")
outfile.close()


if 'Kaolinite' in open('thddem1214r3_hs.dat').read():
    print("true")
    
    


with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace(text_to_search, replacement_text), end='')