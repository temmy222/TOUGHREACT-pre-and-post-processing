# -*- coding: utf-8 -*-
"""
Created on Tue May  7 11:45:53 2019

@author: tajayi3
"""
import os
import shutil
import itertools

"""
copy files function
"""

class prepfortoughreact(object):
    #takes in file names as a list
    def __init__(self,location,destination,filenames,word):
        self.location = location
        self.destination = destination
        self.filenames = filenames
        self.word = word
    
    def copyfile(self,filename,location,destination):
        path = destination
        dest = location
        src_files = os.listdir(path)
        for file_name in src_files:
            full_file_name = os.path.join(path, file_name)
            if (os.path.isfile(full_file_name)):
                shutil.copy(full_file_name, dest)
            
    def copyallfiles (self):
        for i in range(0,len(self.filenames)):
            a = self.filenames[i]
            self.copyfile(a,self.location,self.destination)
        
    def findword(self,filename):
        with open(filename) as myFile:
            for num, line in enumerate(myFile, 1):
                if self.word in line:
                    print ('found at line:', num)
                    point1 = num
                    return point1
    
    def sliceofffile(self,filename):
        point1 = self.findword(filename)
        with open("test2.txt", "w") as f1:
            with open(file_name2, "r") as text_file:
                for line in itertools.islice(text_file, 1, point1-2):
                    f1.write(line)
    
    def sliceoffline(self,filename):
        with open('test2.txt') as thefile:
            lines = thefile.readlines()
            mesh = []
            for i in range(0,len(lines)):
                a = lines[i]
                b = a[0:6]
                mesh.append(b)
                return mesh
                
    def writetofile(self,filename):
        mesh = self.sliceoffline(filename)
        with open("test.txt", "w") as f1:
            for item in mesh:
                f1.write("%s\n" % item)
        f1.close()


path = r"C:\Users\tajayi3\Desktop\Research\my TOUGHREACT$TOUGH Simulations\Moving Forward\Cement Batch Reactions Gherardi Brine"
dest = r"C:\Users\tajayi3\Desktop\Research\Software\PyTOUGH-master"
file_name = "kdd_conc.tec"
file_name2 = "MESH"
lookup = 'CONNE'
myList = ["kdd_conc.tec", "kdd_gas.tec", "kdd_min.tec", "kdd_tim.tec", "MESH"]
tre = prepfortoughreact(path,dest,myList,lookup)
tre.copyallfiles()

#copyfile(file_name,path,dest)
#copyfile(file_name2,path,dest)
#point1 = findword(lookup,file_name2)



            
#with open('test2.txt') as thefile:
#    lines = thefile.readlines()
#
#mesh = []
#for i in range(0,len(lines)):
#    a = lines[i]
#    b = a[0:6]
#    mesh.append(b)
#
#
#with open("test.txt", "w") as f1:
#    for item in mesh:
#        f1.write("%s\n" % item)
#
#f1.close()