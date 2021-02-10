# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 10:36:03 2020

@author: Mikey
"""

import matplotlib as mpl
from matplotlib import pyplot as plt, rc
import pandas as pd
import numpy as np
from pylab import cm
import matplotlib.font_manager as fm
import os

# Global parameters
font_names = [f.name for f in fm.fontManager.ttflist]
mpl.rcParams['font.family'] = 'Arial'
plt.rc('xtick', labelsize=14)
plt.rc('ytick', labelsize=14)

# Data
layers = [6,8,10,12,14,16]

surf1_eng_1 = [2302.644973,
1147.584248,
691.4174646,
458.4961629,
329.5603429,
245.340739]

surf1_eng_2 = [3595.5013793,
294.0699694,
178.8810013,
117.0136704,
85.36923009,
62.43756856]

surf2_eng_1 = [1317.55670,
658.7413295,
396.7103102,
263.0871078,
188.8051741,
140.6319483]

surf2_eng_2 = [7.476866765, 7.323578215, 7.161305084, 6.994828263]

# Plot data
fig, ax1 = plt.subplots(1)

# Colors
color1 = '#ffa600'; color2 = '#58508d'
color3 = '#003f5c'; color4 = '#bc5090'
color5 = '#ff6361'; color6 = '#de9eb2'
color7 = '#91bc50'
colors = cm.get_cmap('PuOr', 8)

# Axis
#ax1.xaxis.set_tick_params(which='major', size=7, width=1, direction='in', top='on')
#ax1.xaxis.set_tick_params(which='minor', size=7, width=1, direction='in', top='on')
#ax1.yaxis.set_tick_params(which='major', size=7, width=1, direction='in', right='on')
#ax1.yaxis.set_tick_params(which='minor', size=7, width=1, direction='in', right='on')

# Labels
plt.plot(layers, surf1_eng_1 , color=color3, marker="^", label='Double passivation')
plt.plot(layers, surf1_eng_2 , color=color2,marker=".", label='Al term single passivation')
plt.plot(layers, surf2_eng_1 , color=color1,marker=".", label='N term single passivation')
#plt.plot(layers, N_surf2_scf , color=color1,marker="^", label='N-term surface 2')
#plt.plot(layers, Al_surf2_scf , color=color4,marker="-o", label='Al-term surface 2')
plt.xlabel("Layers", fontsize=16, fontweight = 'bold')
plt.ylabel(r'Energy difference between layers (meV/atom)', fontsize=16, fontweight = 'bold')
plt.title("AlN 0001 slab layers convergence testing", fontweight='bold', fontsize=18)


#plt.xticks([100,150,200,250,300,350,400])
#plt.yticks([-100, -80, -60, -40, -20, 0, 20])
#xmin = 100; xmax = 400; ymin = -100; ymax = 100;
#xmin, xmax = plt. xlim(xmin,xmax)
#ymin, ymax = plt. ylim(ymin,ymax)
ax1.grid(linestyle='--', linewidth='0.25', color='gray')

#plt.text(3.5, -12.81, 'Energy converges ~ N = 6', color='black', 
#        bbox=dict(facecolor='#ffa600', edgecolor='black', boxstyle='round,pad=1'))
#plt.arrow(5,-12.7, 0,0.05, width=0.05)

'''
ax1.tick_params(axis='y', labelcolor='black')

ax2 = ax1.twinx()

ax2.set_ylabel('Surface energy (J/m$\mathregular{^{2}}$)', fontsize=16, fontweight = 'bold') 
plt.plot(layers, surf1_eng_2 , color=color3, marker="^", label='Surface 1')
plt.plot(layers, surf2_eng_2 , color=color2,marker=".", label='Surface 2')
ax2.tick_params(axis='y', labelcolor='black')
'''
plt.legend(frameon=False,prop={'size': 14})
#fig.tight_layout() 

