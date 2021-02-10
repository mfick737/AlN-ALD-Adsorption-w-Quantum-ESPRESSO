#=====================================================================#
#======================= QE modify input file info ===================#
#=====================================================================#

# This script was used to modify or add lines to a batch of QE input files
# Here, we change the calculation type from an scf calculation 
# The script can be edited to suit your given needs

# Import necessary libraries
import os
import re

# Specify file header name that you want to call files
fh_name = "AlN_layers"

# Changes to directory where batch of input files you want to edit are located
directory = r"C:\Users\Mikey\Documents\DFT\location\batch\inputfiles"
os.chdir(directory)

# Main loop that goes through
for filename in os.listdir(directory): 
   
    # Open and parse file
    fileinfo = open(filename,'r')
    file_list = (fileinfo.readlines())
    calculation_line = '\tcalculation = "scf"\n'
    calculation_num = file_list.index(calculation_line)
    
    # Write to file
    string1 = filename
    filenumber = int(re.search(r'\d+', string1).group())
    input_filename = str(fh_name) + str(filenumber) + ".in"
    input_fh = open(input_filename, 'w', encoding='utf-8')
    
    input_fh.write('&CONTROL\n')
    input_fh.write('\tcalculation = "scf"\n')
    
    for i in range(4,len(file_list)):
        input_fh.write(str(file_list[i]))
       
    input_fh.close()

