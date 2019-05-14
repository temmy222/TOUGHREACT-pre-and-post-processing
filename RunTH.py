# -*- coding: utf-8 -*-
"""
Created on Tue May  7 10:15:31 2019

@author: sdhaka5
"""


import os
import subprocess


def run(inputfile,outputfile):
    FNULL = open(os.devnull, 'w')    #use this if you want to suppress output to stdout from the subprocess

    args = "TH.win64.exe " + "<" + inputfile + "> " + outputfile
    print(args)
    subprocess.run(args, stdout=FNULL, stderr=FNULL, shell=True, check=True)