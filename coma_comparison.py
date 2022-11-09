# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 01:40:45 2022

Compare new data to our COMA data 
@author: okorn
"""
# import libraries
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# select file to export
case = '2022-08-04'

#create a directory path for us to pull from / save to
path = 'C:\\Users\\okorn\\Documents\\Data\\{}'.format(case)

#get the date in an alternate format
caseAKA = case.replace('-', '')

#load in data from COMA
#get the filename to be loaded
filename = 'acclip-COMA-CON2O_WB57_{}_RA.ict'.format(caseAKA)
#combine the paths with the filenames for each
filepath = os.path.join(path, filename)
#load in the file
coma = pd.read_csv(filepath,skiprows=35,usecols=['Time_Start','CO'])

#load in the other data for comparison
#get the filename to be loaded
filename = 'ACCLIP-GEOS_WB57_{}_RC.ict'.format(caseAKA)
#combine the paths with the filenames for each
filepath = os.path.join(path, filename)
#load in the file
other = pd.read_csv(filepath,skiprows=61,usecols=['Time_Start',' CO_GEOS'])

#load in the pressure data from MMS
path2 = 'C:\\Users\\okorn\\Documents\\Data\\_OtherData_\\'
#get the filename to be loaded
filename = 'ACCLIP-MMS-1HZ_WB57_{}_RA.ict'.format(caseAKA)
#combine the paths with the filenames for each
filepath = os.path.join(path2, filename)
#load in the file
mms = pd.read_csv(filepath,skiprows=52,usecols=['TIME_START',' G_ALT_MMS'])

#convert from seconds past midnight to HH:mm:ss
#initialize blank column to calculate in
coma_startHMS = np.empty(len(coma["Time_Start"]), dtype=datetime)
#also get the sate in datetime format
date = datetime.strptime(case,"%Y-%m-%d")
for index, row in coma.iterrows():
    #fill in the time past midnight
    coma_startHMS[index] = timedelta(seconds=coma.iloc[index,0])
#add in the date
coma_startHMS = coma_startHMS + date
    
#do the same for our other dataset
other_startHMS = np.empty(len(other["Time_Start"]), dtype=datetime)
for index, row in other.iterrows():
    #fill in the time past midnight
    other_startHMS[index] = timedelta(seconds=other.iloc[index,0])
#add in the date
other_startHMS = other_startHMS + date    

#do the same for the MMS data
mms_startHMS = np.empty(len(mms["TIME_START"]), dtype=datetime)
for index, row in mms.iterrows():
    #fill in the time past midnight
    mms_startHMS[index] = timedelta(seconds=mms.iloc[index,0])
#add in the date
mms_startHMS = mms_startHMS + date  
 
#add our new times back to each dataframe
coma['realTime'] = coma_startHMS
coma = coma.drop(columns='Time_Start')
other['realTime'] = other_startHMS
other = other.drop(columns='Time_Start')
mms['realTime'] = mms_startHMS
mms = mms.drop(columns='TIME_START')

#make this the index of each & resample to minutely
coma = coma.set_index('realTime').resample('1S').ffill()
other = other.set_index('realTime').resample('1S').ffill()
mms = mms.set_index('realTime').resample('1S').ffill()

#combine our dataframes
coma = coma.join(other)
coma = coma.join(mms)

#get rid of negatives
coma = coma.replace(-9999, 'NaN')
coma = coma[coma[' CO_GEOS'] >= 0]

#now make some plots!
fig1, ax = plt.subplots(2, 1, figsize=(8,5.5),sharex=False)

#subplot 1- COMA CO data
new = ax[0].scatter(coma.index,coma[' G_ALT_MMS'],c=coma['CO']) 
ax[0].grid('on')
ax[0].xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
ax[0].set_ylabel('Altitude (m)')
ax[0].set_xlabel('Time, UTC')
ax[0].set_ylim([0, 200000])
ax[0].title.set_text('{} COMA CO (ppb)'.format(case))
plt.colorbar(new,ax=ax[0])


new2 = ax[1].scatter(coma.index,coma[' G_ALT_MMS'],c=coma[' CO_GEOS'])
ax[1].grid('on')
ax[1].xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
ax[1].set_ylabel('Altitude (m)')
ax[1].set_xlabel('Time, UTC')
ax[1] = plt.gca()
ax[1].set_ylim([0, 200000])
ax[1].title.set_text('{} GEOS CO (mol/mol)'.format(case))
fig1.tight_layout(pad=2.0)
plt.colorbar(new2,ax=ax[1])
