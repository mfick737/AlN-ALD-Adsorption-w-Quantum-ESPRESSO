# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 11:01:21 2020

@author: Mikey
"""

#PBS generator second edition

#### Make PBS script ####

import os 
# PBS Directives
queue = '-q standard_sm'
processors = '-l select=10:ncpus=44:mpiprocs=1'
walltime = '-l walltime=12:00:00'
stdout = '-j oe'
accountname = '-A ARLAP01644200'
shell = '-S /bin/bash'
name1 = 'AlN_ads'
name2 = "AlN_ads"

start = 0; end = 20;

# Change to directory where you want PBS files created
os.chdir(r'C:\Users\Mikey\Documents\DFT\TechReport_Calculations\New_AlN\AlN_Batches\AlN_Batch30')
# ===========================================================================#
# ============================= Create Files ================================#
# ===========================================================================#
for i in range(start,end):
    input_filename = (name1 + str(i) + ".pbs" )
    input_fh = open(input_filename, 'w', encoding='utf-8')

    # PBS Directives
    input_fh.write('#!/bin/bash\n\n')
    input_fh.write('#PBS ')
    input_fh.write(str(accountname))
    input_fh.write('\n')
    input_fh.write('#PBS ')
    input_fh.write(str(queue))
    input_fh.write('\n')
    input_fh.write('#PBS ')
    input_fh.write(str(processors))
    input_fh.write('\n')
    input_fh.write('#PBS ')
    input_fh.write(str(walltime))
    input_fh.write('\n')
    input_fh.write('#PBS ')
    input_fh.write(str(stdout))
    input_fh.write('\n')
    input_fh.write('#PBS ')
    jobname = ("-N " + str(name1) + str(i))
    input_fh.write(str(jobname))
    input_fh.write('\n')
    input_fh.write('#PBS ')
    input_fh.write(str(shell))
    input_fh.write('\n')
    input_fh.write('#PBS -V\n')
    input_fh.write('#PBS -l application=espresso\n')
    input_fh.write('\n')
    #if (i == 0 or i == 10):
    #    input_fh.write('#PBS -m be\n')
    #    input_fh.write('#PBS -M nicholas.a.strnad.civ@mail.mil\n\n')
           
    # Comment line
    input_fh.write('#AlN_slab relax \n\n')
    
    # Change to work directory line
    input_fh.write('cd ${WORKDIR}\n\n')
    
    
    # Module load line
    input_fh.write('module load espresso/intel-19.0.1.144-mpich-7.7.4-libsci/6.4.1\n\n')
    
    # Launch line 
    input_fh.write("aprun -B '/apps/unsupported/espresso/6.4.1-intel-19.0.1.144-mpich-7.7.4/q-e-qe-6.4.1/bin/pw.x'")
    
    # Input file (can turn into loop when needed)
    inp_label = (" -inp " + str(name2) + str(i) + ".in" " > " + str(name2) + str(i) + ".out")
    input_fh.write(inp_label)

    input_fh.close()

