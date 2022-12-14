# -*- coding: utf-8 -*-
"""
Load data file from MadgeTech temperature logger
Plot against MMS and COMA data

Note that loading .xlsx file takes 5-10 seconds
"""

# %% load data
# import libraries
import pandas as pd
import numpy as np
from load_flight_functions import read_MMS
from load_flight_functions import read_COMA
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# EDIT THESE-------------------------------------------------
case = '2022-08-31'
cur_day = datetime(2021,8,6)
f_file = 'f0000' #usually f0000, will sometimes be f0002 etc.
#------------------------------------------------------------

#get the correct files to loop through for our date/case
caseAKA = case.replace('-', '')
caseAKA2 = case.replace('-', '')

filename_COMA = ['../Data/{}/n2o-co_{}_{}.txt'.format(case,case,f_file)]
filename_MMS = '../Data/_OtherData_/ACCLIP-MMS-1HZ_WB57_{}_RA.ict'.format(caseAKA)
filename_MT = '../Data/{}/{} flight Madgetech.xlsx'.format(case,case)

# set font sizes
plt.rc('axes', labelsize=12) # xaxis and yaxis labels
plt.rc('xtick', labelsize=12) # xtick labels
plt.rc('ytick', labelsize=12) # ytick labels

# load MadgeTech file
sheet = 'S06126 MultiChannel - Data'
MT = pd.read_excel(filename_MT,sheet_name=sheet,header=6)
#MT_time = [datetime.strptime(tstamp,"%Y-%m-%d %H:%M:%S") for tstamp in MT['Date']]

# load COMA file
COMA = read_COMA(filename_COMA)

ix_8 = np.ravel(np.where(COMA["      MIU_VALVE"]==8)) # inlet
ix_7 = np.ravel(np.where(COMA["      MIU_VALVE"]==7)) # inlet (lab)
ix_3 = np.ravel(np.where(COMA["      MIU_VALVE"]==3)) # high cal
ix_2 = np.ravel(np.where(COMA["      MIU_VALVE"]==2)) # low cal
ix_1 = np.ravel(np.where(COMA["      MIU_VALVE"]==1)) # flush

# load MMS
MMS = read_MMS(filename_MMS,cur_day)

# %% plot data
fig1, ax = plt.subplots(2, 1, figsize=(8,5.5),sharex=True)
#ax[0].plot(MT['Date'],MT['Thermocouple 5 (°C)'],'r.') # RF04 (before column given name)
ax[0].plot(MT['Time'],MT['InletSolen (°C)'],'r.',label = "Inlet Solenoid") # RF05
#ax[0].plot(MT['Date'],MT['Ambient Temperature 1 (°C)'])
#ax[0].plot(MT['Date'],MT['PowrSupply (°C)'])
#ax[0].plot(MT['Date'],MT['Ext Front (°C)'])
#ax[0].plot(MT['Date'],MT['Lsr_I_tran (°C)'])
#ax[0].plot(MT['Date'],MT['Lasr_I_res (°C)'])
#ax[0].plot(MT['Date'],MT['LaserBack (°C)'])
#ax[0].plot(MT['Date'],MT['CPU (°C)'])
#ax[0].plot(MT['Date'],MT['BoxFanFlow (°C)'])

ax[0].grid('on')
ax0_twin = ax[0].twinx()
ax0_twin.plot(MMS['time'],MMS['ALT'],'k.', label = "Altitude")
ax[0].xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
ax[0].set_ylabel('Temperature, C')
ax0_twin.set_ylabel('Altitude, m')
ax[0].set_xlabel('Time, UTC')
fig1.legend(loc='upper right', bbox_to_anchor=(0.304, 0.67))


ax[1].plot(COMA['time'],COMA["      GasP_torr"],'k.')
ax[1].plot(COMA['time'][ix_8],COMA["      GasP_torr"][ix_8],'b.',label = 'Probe')
ax[1].plot(COMA['time'][ix_2],COMA["      GasP_torr"][ix_2],'y.',label = 'Low Cal')
ax[1].plot(COMA['time'][ix_3],COMA["      GasP_torr"][ix_3],'m.', label = 'High Cal')
ax[1].grid('on')
ax[1].set_ylabel('Cell pressure, Torr')
ax[1].legend(loc = 'lower left')
fig1.tight_layout()

fig1.savefig('fig1.png',dpi=300)
