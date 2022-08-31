# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 01:40:21 2022

@author: okorn
"""
#plot cleaned ICARTT data colored by MIU value

#1st part of this code is 1st part of ICARTT file

# %% set up
# import libraries
import pandas as pd
import numpy as np
from datetime import datetime
from load_flight_functions import read_COMA
import statistics as st

# select file to export
case = '2022-08-12'

#create a directory path to save images to
path = 'C:\\Users\\Okorn\\Documents\\Data\\{}'.format(case)

if case == '2022-08-02':
    filename_COMA = ['../Data/2022-08-02/n2o-co_2022-08-02_f0000.txt']
    output_name = 'COMA_WB57_20220802_RA.ict'
    t0 = datetime(2022,8,2,1,10)
    t1 = datetime(2022,8,2,6,33)
elif case == '2022-08-04':
    filename_COMA = ['../Data/2022-08-04/n2o-co_2022-08-04_f0000.txt']
    output_name = 'COMA_WB57_20220804_RA.ict'
    t0 = datetime(2022,8,4,1,12)
    t1 = datetime(2022,8,4,6,18)
elif case == '2022-08-06':
    filename_COMA = ['../Data/2022-08-06/n2o-co_2022-08-06_f0000.txt']
    output_name = 'COMA_WB57_20220806_RA.ict'
    t0 = datetime(2022,8,6,1,0)
    t1 = datetime(2022,8,6,7,9)
elif case == '2022-08-12':
    filename_COMA = ['../Data/2022-08-12/n2o-co_2022-08-12_f0000.txt']
    output_name = 'COMA_WB57_20220812_RA.ict'
    t0 = datetime(2022,8,12,2,10)
    t1 = datetime(2022,8,12,8,0)
elif case == '2022-08-19':
    filename_COMA = ['../Data/2022-08-19/n2o-co_2022-08-19_f0000.txt']
    output_name = 'COMA_WB57_20220819_RA.ict'
    t0 = datetime(2022,8,19,0,0)
    t1 = datetime(2022,8,19,6,15)

# read COMA data
COMA = read_COMA(filename_COMA)

#remove empty spaces in data for workability
COMA.columns = COMA.columns.str.strip()


#reformat original data for convenience
COMA_original = pd.DataFrame({'time': COMA["Time"],
                    'CO_ppm': COMA["[CO]d_ppm"],
                    'N2O_ppm': COMA["[N2O]d_ppm"],
                    'CellP_torr': COMA["GasP_torr"],
                    'MIU' : COMA["MIU_VALVE"]})

#---------------------------------------------------------
#---------------------------------------------------------

#Now get what we need to plot
import matplotlib.pyplot as plt
import os


#set up structures to loop through
plots = ['CO_ppm','N2O_ppm','CellP_torr']
#loop through for each value to plot
for i in range(len(plots)):
    #get the current one to plot alone
    current_plot = plots[i]
    #plot dot for each time-stamp
    plt.scatter(COMA_original['time'], COMA_original['{}'.format(plots[i])], c = COMA_original['MIU'])
   # plt.legend()

    #plotting to initialize
    plt.xlabel("Time (s) since 0000 UTC")
    plt.ylabel("{}".format(current_plot))
    plt.title('{} {}'.format(case,current_plot))

    #final plotting & saving
    imgname = '{} {} timeseries.png'.format(case,current_plot)
    imgpath = os.path.join(path, imgname)
    plt.savefig(imgpath)
    plt.show()

