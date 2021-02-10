# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 15:40:34 2020

@author: Mikey
"""

# add outdir line to files

import os
import re

name = "AlN_layers"
directory = r"C:\Users\Mikey\Documents\DFT\TechReport_Calculations\New_AlN\AlN_Batches\AlN_Batch6"
os.chdir(directory)


for filename in os.listdir(directory): 
   
    fileinfo = open(filename,'r')
    file_list = (fileinfo.readlines())
    calculation_line = '\tcalculation = "scf"\n'
    calculation_num = file_list.index(calculation_line)
    #atomic_species_line = 'ATOMIC_SPECIES\n'
    #atomic_species_num = file_list.index(atomic_species_line)
    
    # Write to file
    
    string1 = filename
    filenumber = int(re.search(r'\d+', string1).group())
    input_filename = str(name) + str(filenumber) + ".in"
    input_fh = open(input_filename, 'w', encoding='utf-8')
    
    input_fh.write('&CONTROL\n')
    input_fh.write('\tcalculation = "scf"\n')
    
    for i in range(4,len(file_list)):
        input_fh.write(str(file_list[i]))
       
    input_fh.close()

