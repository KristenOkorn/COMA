# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 06:15:53 2022

@author: okorn
"""

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
case = '2022-08-19'

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

# #Replace N2O values with -9.999 if pressure not within 1 stdev of median
# COMA["[N2O]d_ppm"] = np.where((COMA["GasP_torr"] < st.median(COMA["GasP_torr"]) + (0.25*st.stdev(COMA["GasP_torr"])))&( COMA["GasP_torr"] > st.median(COMA["GasP_torr"]) - (0.25*st.stdev(COMA["GasP_torr"]))), COMA["[N2O]d_ppm"], np.nan)
#
# #When purge not used (high cal to probe), remove 20s of data
for index, row in COMA.iterrows():
#     #first make sure we don't go out of bounds
#     if index < len(COMA):
#         if COMA["MIU_VALVE"].iloc[index] == 3 or COMA["MIU_VALVE"].iloc[index] == 2 and COMA["MIU_VALVE"].iloc[index+1] == 8:
#             #if there are > 120s remaning, delete the next 20s worth of data
#             if len(COMA) - index >= 120:
#                 COMA.replace(COMA.index[index+1:index+120], np.nan)
#             #Otherwise, delete as many points as remain
#             else:
#                 COMA.replace(COMA.index[index+1:len(COMA)-index], np.nan)
#     #Remove a few points from the front of each cal to be safe
#     elif COMA["MIU_VALVE"].iloc[index] == 2 and COMA["MIU_VALVE"].iloc[index-1] != 2 :
#         #if there are >30s preceeding, delete the next 30 points
#         if index > 120:
#             COMA.replace(COMA.index[index-120:index-1], np.nan)
#         #Otherwise, delete as many points as proceeding
#         else:
#             COMA.replace(COMA.index[0:index], np.nan)
        
    
    #Convert the time from string to datetime
    COMA['Time'].iloc[index] = datetime.strptime(COMA['Time'].iloc[index], '  %m/%d/%Y %H:%M:%S.%f')
    
#Get rid of times that we aren't probe sampling
COMA["MIU_VALVE"] = np.where(COMA["MIU_VALVE"] == 8,COMA["MIU_VALVE"],np.nan)

# convert COMA to seconds after midnight
time_midnight = [(t.hour * 3600) + (t.minute * 60) + t.second + (t.microsecond / 1000000.0) for t in COMA['time']]
#Add to each of our COMA dataframes
COMA['time_midnight'] = np.array(time_midnight)

#Convert t0 to seconds after midnight
t0_midnight = (t0.hour * 3600) + (t0.minute * 60) + t0.second + (t0.microsecond / 1000000.0)
t1_midnight = (t1.hour * 3600) + (t1.minute * 60) + t1.second + (t1.microsecond / 1000000.0)

#Get rid of times before takeoff & after landing
COMA['time_midnight'] = np.where(COMA['time_midnight']<t0_midnight,np.nan,COMA['time_midnight'])
COMA['time_midnight'] = np.where(COMA['time_midnight']>t1_midnight,np.nan,COMA['time_midnight'])

#For plotting only: drop the NaNs
COMA = COMA.dropna()

#reformat original data for convenience
COMA_original = pd.DataFrame({'time': COMA["Time"],
                    'CO_ppm': COMA["[CO]d_ppm"],
                    'N2O_ppm': COMA["[N2O]d_ppm"],
                    'MIU' : COMA["MIU_VALVE"],
                    'CellP': COMA["GasP_torr"]})

#---------------------------------------------------------
#---------------------------------------------------------

# #Now get what we need to plot
# import matplotlib.pyplot as plt
# import os


# #set up structures to loop through
# plots = ['CO_ppm','N2O_ppm']
# #loop through for each value to plot
# for i in range(len(plots)):
#     #get the current one to plot alone
#     current_plot = plots[i]
#     #plot dot for each time-stamp
#     plt.scatter(COMA_original['time'], COMA_original['{}'.format(plots[i])], c = COMA_original['MIU'])
#    # plt.legend()

#     #plotting to initialize
#     plt.xlabel("Datetime")
#     plt.ylabel("{}".format(current_plot))
#     plt.title('{} {}'.format(case,current_plot))

#     #final plotting & saving
#     imgname = '{} {} timeseries_filtered_120_both.png'.format(case,current_plot)
#     imgpath = os.path.join(path, imgname)
#     plt.savefig(imgpath)
#     plt.show()

#Commented things out to just extract data for manual cleaning
import os

imgname = '2022-08-19 data'

imgpath = os.path.join(path, imgname)

COMA_original.to_csv(imgpath)