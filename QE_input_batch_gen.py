#=============================================================================#
#======================== QE batch input file generator ======================#
#=============================================================================#
#=============================================================================#
# This script generates a batch of input files that could be run to test the  #
# wavefunction and charge density cutoff convergence for an AlN unitcell      #
# ============================================================================#


# Import necessary libraries
import os
import re

# List of wavefunction (ecutwfc) and charge density (ecutrho) cutoff values
ecutwfc = [15.0,20.0,25.0,30.0,35.0,40.0,45.0,50.0,55.0,60.0,65.0,70.0]
ecutrho = []; 
for i in range(len(ecutwfc)):
    ecutrho.append(8*ecutwfc[i])


# Extract unit cell file information
directory1 = r"C:\Users\Mikey\Documents\DFT\location\unitcell\info"
os.chdir(directory1)
filename = "AlN_unitcell_info.txt"  # file is in the repo as an example
slab_fh = open(filename,'r')
file_list = (slab_fh.readlines())


# Change to directory where the batch files will be located
directory2 = r"C:\Users\Mikey\Documents\DFT\location\batch\input\files"
os.chdir(directory2)


# Main loop that generates an input file on each iteration
for i in range(len(ecutwfc)):
        
    input_filename = ("AlN_unitcell" + str(i) + ".in" )
    input_fh = open(input_filename, 'w', encoding='utf-8')
    
    # CONTROL 
    input_fh.write('&CONTROL\n')
    input_fh.write('\tcalculation = "scf"\n')
    input_fh.write('\tnstep = 100\n')      
    input_fh.write('\tpseudo_dir = "/home/michael/Documents/Pseudos"\n')
    input_fh.write()
    input_fh.write('/\n')  
    
    # SYSTEM
    input_fh.write('&SYSTEM\n')
    for k in range(0,5):
        input_fh.write(str(file_list[k]))
    
    input_fh.write('\tecutwfc = ')
    input_fh.write(str(ecutwfc[i]))
    input_fh.write('\n')
    input_fh.write('\tecutrho = ')
    input_fh.write(str(ecutrho[i]))
    input_fh.write('\n')
    input_fh.write('\tdegauss = 1e-2\n')
    input_fh.write('\toccupations = "smearing"\n')                           
    input_fh.write('\tsmearing = "gaussian"\n')     
    input_fh.write("/\n")
       
    # ELECTRONS
    input_fh.write('&ELECTRONS\n')
    input_fh.write('\tconv_thr = 1e-06\n')
    input_fh.write('\tdiagonalization = "david"\n')
    input_fh.write('\tmixing_mode = "plain"\n')
    input_fh.write('\tmixing_beta = 0.7')
    input_fh.write('\n\tstartingpot = "atomic"\n')                            
    input_fh.write('\tstartingwfc = "atomic+random"\n')                     
    input_fh.write('/\n')
    
    # ATOMIC_SPECIES
    input_fh.write('ATOMIC_SPECIES\n')
    input_fh.write('N      14.0067  N.pbe-n-rrkjus_psl.1.0.0.UPF\n')
    input_fh.write('Al    26.98154  Al.pbe-nl-rrkjus_psl.1.0.0.UPF\n')
    input_fh.write('\n')
       
    # ATOMIC_POSITIONS 
    input_fh.write('ATOMIC_POSITIONS {angstrom}\n')
    for j in range(7,len(file_list)):
        input_fh.write(str(file_list[j]))
    
    # K_POINTS
    input_fh.write('\n')
    input_fh.write('K_POINTS {automatic}\n')
    input_fh.write('1 1 1 0 0 0\n')

    input_fh.close()




