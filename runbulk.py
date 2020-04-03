import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import griddata
from t2listing import * 
from t2data import *
from math import log10
import numpy as np
import scipy 
import matplotlib as mpl
from t2listing import *
from mpl_toolkits.mplot3d import Axes3D
from scipy import interpolate
from scipy.interpolate import griddata
from prepfortoughreact import *
from mpl_toolkits.axes_grid1 import make_axes_locatable
import re 
from prepfortoughreact import *
from batchreactionplotroutine import *
from flowreactionplotroutine import *
import os
import subprocess
import random
from prepfortoughreact import *
from flowreactionplotroutine import *
from batchreactionplotroutine import *
import pandas as pd
import re
from miscellaneous import *
import concurrent.futures
import time
import requests
 
folders=[]       
rootdir = r"C:\Users\tajayi3\OneDrive - Louisiana State University\test"
suffix = ">treacteos1<flow.inp"
for subdir,dirs,files in os.walk(rootdir):
    output = subdir+suffix
    os.chdir(subdir)
    if os.path.exists("chemical.inp"):
        folders.append(subdir)

#folders= ['C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\closed boundary\\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer time', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\closed boundary\\Gulf of Mexico Cement Flow - Ca injected sand equil brine Onshore - longer time', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\closed boundary\\Gulf of Mexico Cement Flow - Na acetate sand equil injected Onshore - longer time', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\closed boundary\\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - longer', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\Crack investigation\\Gulf of Mexico Sandstone Cement Flow - NaCl brine', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\Diffusivity sensitivity\\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\Diffusivity sensitivity\\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - larger', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\Diffusivity sensitivity\\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - muchlar', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\Diffusivity sensitivity\\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - smaller', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\Fast Rate all minerals\\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\Fast Rate all minerals\\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - longer', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer time', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longest', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - same high cond', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - same low cond  - longer time', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - shc - longer time', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - shc - longer time - mstogrid', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore -reduced domain', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\Gulf of Mexico Cement Flow - Ca injected sand equil brine Onshore - longer time', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\Gulf of Mexico Cement Flow - Ca injected sand equil brine Onshore - same high cond - longer time', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\Gulf of Mexico Cement Flow - Ca injected sand equil brine Onshore - same low cond - longer time', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\Gulf of Mexico Cement Flow - Na acetate sand equil injected Onshore - longer time', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\Gulf of Mexico Cement Flow - Na acetate sand equil injected Onshore - same high cond - longer time', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\Gulf of Mexico Cement Flow - Na acetate sand equil injected Onshore - same low cond  - longer time', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - longer', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - same high cond - longer time', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - same low cond', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\increased flow\\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer time', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\increased flow\\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer time2', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\more ca\\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer time', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\more ca\\Gulf of Mexico Cement Flow - Ca injected sand equil brine Onshore - longer time', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\more ca\\Gulf of Mexico Cement Flow - Na acetate sand equil injected Onshore - longer time', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\more ca\\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - longer', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\more ca\\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - longer -hightemp', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\more cl\\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer time', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\more cl\\Gulf of Mexico Cement Flow - Ca injected sand equil brine Onshore - longer time', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\more cl\\Gulf of Mexico Cement Flow - Na acetate sand equil injected Onshore - longer time', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\more cl\\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - longer', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\more cl\\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - longer -hightemp', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\more co2\\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer time', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\more na\\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer time', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\more na\\Gulf of Mexico Cement Flow - Ca injected sand equil brine Onshore - longer time', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\more na\\Gulf of Mexico Cement Flow - Na acetate sand equil injected Onshore - longer time', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\more na\\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - longer', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\more na\\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - longer -highertemp', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\Offshore Ca\\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer time', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\same RSA\\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer time', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\same RSA\\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - longer', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\Zeolites\\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer time', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\Zeolites\\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer time -add', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\Zeolites\\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer time -addnocash', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\Zeolites\\Gulf of Mexico Cement Flow - Ca injected sand equil brine Offshore - longer time -nocash', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\Zeolites\\Gulf of Mexico Cement Flow - Ca injected sand equil brine Onshore - longer time', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\Zeolites\\Gulf of Mexico Cement Flow - Ca injected sand equil brine Onshore - longer time -add', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\Zeolites\\Gulf of Mexico Cement Flow - Ca injected sand equil brine Onshore - longer time-addnocash', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\Zeolites\\Gulf of Mexico Cement Flow - Ca injected sand equil brine Onshore - longer time-nocash', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\Zeolites\\Gulf of Mexico Cement Flow - Na acetate sand equil injected Onshore - longer time', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\Zeolites\\Gulf of Mexico Cement Flow - Na acetate sand equil injected Onshore - longer time -add', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\Zeolites\\Gulf of Mexico Cement Flow - Na acetate sand equil injected Onshore - longer time-addnocash', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\Zeolites\\Gulf of Mexico Cement Flow - Na acetate sand equil injected Onshore - longer time-nocash', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\Zeolites\\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - longer', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\Zeolites\\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - longer - add', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\Zeolites\\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - longer-addnocash', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\Zeolites\\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - longer-nocash', 'C:\\Users\\tajayi3\\OneDrive - Louisiana State University\\Increased depth\\Zeolites\\Gulf of Mexico Cement Flow - NaCl sand equil brine injected Onshore - shc -add']
#import os
#os.system('cmd /k "cd {}"'.format(rootdir))

#trial=r"C:\Users\tajayi3\OneDrive - Louisiana State University\test\Gulf of Mexico Cement Flow - Ca injected sand equil brine Onshore - longer time"

def runsim(filelocation):
    os.chdir(filelocation)
    print("here")
    FNULL = open(os.devnull, 'w')    #use this if you want to suppress output to stdout from the subprocess

    args = "treacteos1.exe " + "<" + "flow.inp" 
    print(args)
    subprocess.run(args, stdout=FNULL, stderr=FNULL, shell=True, check=True)

#urls = [
#  'https://www.royalacademy.org.uk/',
#  'http://www.metmuseum.org/',
#  'http://www.artic.edu/',
#]

#def runsim(filelocation):
#    print("here")
#    
#def open_url(url):
#  print('Opening {}'.format(url))
#  time.sleep(3)
#  return requests.get(url)
    
#with concurrent.futures.ProcessPoolExecutor() as executor:
#    executor.map(open_url,urls)
    
from multiprocessing import Pool
import multiprocessing
value = int(multiprocessing.cpu_count()/2)

if __name__ == '__main__':
    pool = Pool(value)
    results = pool.map(runsim, folders)
    pool.close()
    pool.join()
    
