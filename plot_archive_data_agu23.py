# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 10:34:48 2023

@author: okorn

Plotting for AGU 2023 poster
COMA xls files with same "final" data from archive
MMS from data archive using Levi's function

"""
# %% load libraries and files
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates
import os

from load_flight_functions import V_to_T
from load_flight_functions import read_MMS

# EDIT THESE--------------------------------------
case = '2022-08-31'
cur_day = datetime(2022,8,31)
#-------------------------------------------------
#get the correct files to loop through for our date/case
caseAKA = case.replace('-', '')

filename_COMA = 'C:\\Users\\okorn\\Documents\\COMA-main\\RB Data\\RB xls\\{}_cleaned_RB.xls'.format(case)
filename_MMS = '../Data/_OtherData_/ACCLIP-MMS-1HZ_WB57_{}_R0.ict'.format(caseAKA)
#for 8/21/22, use RA instead of R0

# %% data
# read COMA data, combining multiple files if needed
COMA = pd.read_excel(filename_COMA)
#rename time
COMA = COMA.rename(columns={'Time_Start':'time'})
#replace -9.999 with NaN
COMA = COMA.replace(to_replace=-9.999,value=np.nan)
#convert all to ppb
COMA['CO'] = COMA['CO']*1000
COMA['N2O'] = COMA['N2O']*1000

# plots involving aicraft position

# import mapping library
import cartopy.crs as ccrs
import cartopy.feature as cf

# %% load MMS and WB57 data
MMS = read_MMS(filename_MMS,cur_day)
MMS_sync = MMS.groupby(pd.Grouper(key="time", freq="1s")).mean()

COMA_sync = COMA.groupby(pd.Grouper(key="time", freq="1s")).mean()

# time-sync the data with COMA
sync_data = pd.merge(MMS_sync, COMA_sync, how='inner', on=['time'])

#----------------------------------------------------------
# %% altitude vs time scatterplot for CO
fig3, ax3 = plt.subplots(1, 1, figsize=(6, 3.5), dpi=200)
sc5 = ax3.scatter(sync_data.index, sync_data['ALT'], c=sync_data['CO'], s=15)
ax3.grid()
ax3.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
ax3.set_xlabel('Time (UTC)')
ax3.set_ylabel('Altitude, m')

#make colorbar
cb5 = plt.colorbar(sc5)
ticks = cb5.get_ticks()
# Round the ticks to 2 decimal places and convert to strings
rounded_labels = [str(np.round(tick, 2)) for tick in ticks]
cb5.ax.set_yticklabels(rounded_labels)
cb5.set_label('N2O (ppb)', fontsize=10)
cb5.ax.tick_params(labelsize=10)
fig3.tight_layout()

#save it out
savePath = 'C:\\Users\\okorn\\Documents\\COMA-main\\RB Plots - AGU\\'
#Create the full path with the figure name
savePath = os.path.join(savePath,'Altitude_timeseries_CO_{}'.format(caseAKA))
# Save the figure to a filepath
fig3.savefig(savePath)

#----------------------------------------------------------
#Now for N2O
fig2, ax2 = plt.subplots(1, 1, figsize=(6, 3.5), dpi=200)
sc4 = ax2.scatter(sync_data.index, sync_data['ALT'], c=sync_data['N2O'], s=15)
ax2.grid()
ax2.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
ax2.set_xlabel('Time (UTC)')
ax2.set_ylabel('Altitude, m')

#make colorbar
cb4 = plt.colorbar(sc4)
ticks = cb4.get_ticks()
# Round the ticks to 2 decimal places and convert to strings
rounded_labels = [str(np.round(tick, 2)) for tick in ticks]
cb4.ax.set_yticklabels(rounded_labels)
cb4.set_label('N2O (ppb)', fontsize=10)
cb4.ax.tick_params(labelsize=10)
fig2.tight_layout()

#save it out
sPath = 'C:\\Users\\okorn\\Documents\\COMA-main\\RB Data\\RB xls\\'
#Create the full path with the figure name
savePath = os.path.join(sPath,'Altitude_timeseries_N2O_{}'.format(caseAKA))
# Save the figure to a filepath
fig2.savefig(savePath)
#----------------------------------------------------------

# %% lat/lon map colored by CO
fig4 = plt.figure(4)
projection = ccrs.Mercator()

ax4 = plt.axes(projection=projection)
ax4.add_feature(cf.COASTLINE)
ax4.add_feature(cf.BORDERS)

plate = ccrs.PlateCarree()

sc2 = ax4.scatter(sync_data['LON'].values, sync_data['LAT'].values,
        c=sync_data['CO'], s=15, transform=plate)

#make colorbar
cb2 = plt.colorbar(sc2)
ticks = cb2.get_ticks()
# Round the ticks to 2 decimal places and convert to strings
rounded_labels = [str(np.round(tick, 2)) for tick in ticks]
#plot the ticks
cb2.ax.set_yticklabels(rounded_labels)
cb2.set_label('CO (ppb)', fontsize=10)
cb2.ax.tick_params(labelsize=10)
fig4.tight_layout()

#save it out
#Create the full path with the figure name
savePath = os.path.join(sPath,'Map_CO_{}'.format(caseAKA))
# Save the figure to a filepath
fig2.savefig(savePath)
    
#----------------------------------------------------------

# %% lat/lon map colored by N2O
fig = plt.figure(0)
projection = ccrs.Mercator()

ax = plt.axes(projection=projection)
ax.add_feature(cf.COASTLINE)
ax.add_feature(cf.BORDERS)

plate = ccrs.PlateCarree()

sc = ax.scatter(sync_data['LON'].values, sync_data['LAT'].values,
        c=sync_data['N2O'], s=15, transform=plate)

#make colorbar
cb = plt.colorbar(sc)
ticks = cb.get_ticks()
# Round the ticks to 2 decimal places and convert to strings
rounded_labels = [str(np.round(tick, 2)) for tick in ticks]
cb.ax.set_yticklabels(rounded_labels)
cb.set_label('N2O (ppb)', fontsize=10)
cb.ax.tick_params(labelsize=10)
fig.tight_layout()

#save it out
#Create the full path with the figure name
savePath = os.path.join(sPath,'Map_CO_{}'.format(caseAKA))
# Save the figure to a filepath
fig.savefig(savePath)
#----------------------------------------------------------
# %% vertical profile of CO colored by N2O
fig5, ax5 = plt.subplots(1, figsize=(5, 4), dpi=200)
ax5.grid()
sc2 = plt.scatter(sync_data['CO'],
        sync_data['ALT'], c=sync_data['N2O'], s=8)
plt.xlabel('CO (ppb)')
    
#make colorbar
cb2 = plt.colorbar(sc2)
ticks = cb2.get_ticks()
# Round the ticks to 2 decimal places and convert to strings
rounded_labels = [str(np.round(tick, 1)) for tick in ticks]
cb2.ax.set_yticklabels(rounded_labels)
cb2.set_label('N2O (ppb)', fontsize=10)
cb2.ax.tick_params(labelsize=10)
fig5.tight_layout()

plt.ylabel('Altitude (m)')

#save it out
#Create the full path with the figure name
savePath = os.path.join(sPath,'Altitude_CO_coloredbyN2O_{}'.format(caseAKA))
# Save the figure to a filepath
fig2.savefig(savePath)

# %% vertical profile of N2O colored by CO
fig1, ax1 = plt.subplots(1, figsize=(5, 4), dpi=200)
ax1.grid()
sc1 = plt.scatter(sync_data['N2O'],
        sync_data['ALT'], c=sync_data['CO'], s=8)
plt.xlabel('N2O (ppb)')

#make colorbar
cb1 = plt.colorbar(sc1)
ticks = cb1.get_ticks()
# Round the ticks to 2 decimal places and convert to strings
rounded_labels = [str(np.round(tick, 1)) for tick in ticks]
cb1.ax.set_yticklabels(rounded_labels)
cb1.set_label('CO (ppb)', fontsize=10)
cb1.ax.tick_params(labelsize=10)
fig1.tight_layout()

plt.ylabel('Altitude (m)')

#save it out
#Create the full path with the figure name
savePath = os.path.join(sPath,'Altitude_N2O_coloredbyCO_{}'.format(caseAKA))
# Save the figure to a filepath
fig2.savefig(savePath)