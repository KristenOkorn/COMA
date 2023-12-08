# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 17:47:06 2023

Load GEOS-2D for plotting

@author: okorn
"""

#import libraries
import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
import matplotlib.dates as mdates
from datetime import datetime
from load_flight_functions import V_to_T
from load_flight_functions import read_MMS

dates = ['2022-08-06','2022-08-19','2022-08-21','2022-08-31']

#-----------------------------------------------------------------------
for n in range(len(dates)):
    #get the date aka
    dateAKA = dates[n].replace('-', '')
    #get the 'current' day
    cur_day = datetime.strptime(dateAKA,'%Y%m%d')
    #load in the GOES-2D data for each date
    path = 'C:\\Users\\okorn\\Documents\\COMA-main\\GOES-2D'
    #get the filename
    filename = "ACCLIP-GEOS-2D_WB57_{}_R0.ict".format(dateAKA)
    #Create full file path for reading file
    filePath = os.path.join(path, filename)
    
    with open(filePath, 'r') as file:
        first_line = file.readline()#Read the first line
        skip=first_line[0:2]
 
    #load in the file
    temp = pd.read_csv(filePath,skiprows=int(skip)-1,header=0)
    
    #create a new column to hold the updated time data in (s)
    temp['s'] = np.nan
    
    # Find rows where the value in 2nd column (1) is 31
    info_rows = temp[temp[' NumP'] == 31]
    
    # Convert the 's' column in temp to numpy.float64
    temp['s'] = temp['s'].astype(np.float64)
    
    #now need to reformat this mess
    for i in range(len(info_rows)- 1, -1, -1): #run through backwards to not mess up row #s
        #replace the nans in 's' with whatever values is in 1st column (0)
        temp.loc[info_rows.index[i]+1:info_rows.index[i]+32, 's'] = info_rows.iloc[i,0]  
        #delete the original rows
        temp = temp.drop(info_rows.index[i])
    
    #get the initial date from our list of dates
    date = datetime.strptime('{}'.format(dates[n]), "%Y-%m-%d")
    
    #convert seconds past midnight to HH:MM:SS
    temp['datetime'] = date + pd.to_timedelta(temp['s'], unit='s')
    
    #make the datetime the index
    temp = temp.set_index('datetime')
    
    #Convert the index to a DatetimeIndex and set the nanosecond values to zero
    temp.index = pd.to_datetime(temp.index,format="%Y-%m-%d %H:%M:%S",errors='coerce')
    
    #the columns are off by 2 when imported - only keep actual pressure & CO
    temp = temp[['Time_Start',' RH_GEOS']]
    
    #rename the columns to their true name
    temp.rename(columns={'Time_Start': 'Pressure',' RH_GEOS':'GEOS CO'}, inplace=True)
    
    #-----------------------------------------------------------------------    
    #also load in our COMA data
    filename_COMA = 'C:\\Users\\okorn\\Documents\\COMA-main\\RB Data\\RB xls\\{}_cleaned_RB.xls'.format(dates[n])
    # read COMA data, combining multiple files if needed
    COMA = pd.read_excel(filename_COMA)
    #rename time
    COMA = COMA.rename(columns={'Time_Start':'datetime'})
    #make the datetime the index
    COMA= COMA.set_index('datetime')
    #Convert the index to a DatetimeIndex and set the nanosecond values to zero
    COMA.index = pd.to_datetime(COMA.index,format="%Y-%m-%d %H:%M:%S",errors='coerce')
    #replace -9.999 with NaN
    COMA = COMA.replace(to_replace=-9.999,value=np.nan)
    #convert all to ppb
    COMA['CO'] = COMA['CO']*1000
    COMA['N2O'] = COMA['N2O']*1000
    #only keep the columns we need
    COMA = COMA[['CO','N2O']]
    
    #-----------------------------------------------------------------------    
    #load in the merge data for adding a tropopause line
    acclippath = 'C:\\Users\\okorn\\Documents\\COMA-main\\Merge'
    #get the filename
    acclipfilename = "ACCLIP-mrg01-WB57_merge_{}_R0.ict".format(dateAKA)
    #Create full file path for reading file
    acclipfilePath = os.path.join(acclippath, acclipfilename)
    
    with open(acclipfilePath, 'r') as file:
        first_line = file.readline()#Read the first line
        skip=first_line[0:3]
 
    #load in the file
    acclip = pd.read_csv(acclipfilePath,skiprows=int(skip)-1,header=0)
    #convert seconds past midnight to HH:MM:SS
    acclip['datetime'] = date + pd.to_timedelta(acclip['Time_Start'], unit='s')
    #make the datetime the index
    acclip= acclip.set_index('datetime')
    #Convert the index to a DatetimeIndex and set the nanosecond values to zero
    acclip.index = pd.to_datetime(acclip.index,format="%Y-%m-%d %H:%M:%S",errors='coerce')
    #only keep the column we need - 
    acclip = acclip[[' TROPPB_GEOS']]
    #rename column
    acclip = acclip.rename(columns={' TROPPB_GEOS':'tropo_P'})
    #replace negatives with NaN
    acclip = acclip[acclip.iloc[:, 0] >= 0]
    
    #-----------------------------------------------------------------------  
    #finally load in the MMS data
    if dateAKA != '20220821': #use the normal version
        filename_MMS = '../Data/_OtherData_/ACCLIP-MMS-1HZ_WB57_{}_R0.ict'.format(dateAKA)
    else: #need to use RA file
        filename_MMS = '../Data/_OtherData_/ACCLIP-MMS-1HZ_WB57_{}_RA.ict'.format(dateAKA)
    MMS = read_MMS(filename_MMS,cur_day)
    #rename time
    MMS = MMS.rename(columns={'time':'datetime'})
    #make the datetime the index
    MMS= MMS.set_index('datetime')
    # Remove fractional seconds from the datetime index
    MMS.index = MMS.index.strftime('%Y-%m-%d %H:%M:%S')
    #Convert the index to a DatetimeIndex and set the nanosecond values to zero
    MMS.index = pd.to_datetime(MMS.index,format="%Y-%m-%d %H:%M:%S",errors='coerce')
    #only keep the columns we need
    MMS = MMS[['LAT','LON','ALT']]

    #----------------------------------------------------------------------- 
    #synchronize all our data
    merge = pd.merge(temp,COMA,left_index=True, right_index=True)
    merge = pd.merge(merge,MMS,left_index=True, right_index=True)
    merge = pd.merge(merge,acclip,left_index=True, right_index=True)
    
    # Remove rows where the GEOS CO is missing
    merge = merge[merge['GEOS CO'] >= 0]
    #----------------------------------------------------------------------- 
    
    #initialize plot
    fig3, ax3 = plt.subplots(1, 1, figsize=(6, 3.5), dpi=200)
    #background scatter
    sc5 = ax3.scatter(merge.index, merge['Pressure'], c=merge['GEOS CO'], s=15)
    #also add the tropopause on the same axes
    ax3.plot(merge.index, merge['tropo_P'], c='red')
    #now separate axes for altitude plot
    #Create a twin Axes sharing the xaxis
    ax4 = ax3.twinx()
    sc4 = ax4.scatter(merge.index, merge['ALT'], c=merge['CO'], s=15,edgecolors='grey',linewidths=0.2,)

    #Set y axes labels
    ax4.set_ylabel('Altitude (m)', fontsize=10, labelpad=-330)
    ax3.set_ylabel('Pressure (mbar)', fontsize=10, labelpad=-320)
    
    #invert the pressure axis
    ax3.invert_yaxis()
    # Move both the inverted y-axis ticks and label to the right side
    ax3.yaxis.tick_right()
    #Make sure our other axis stays on the left
    ax4.yaxis.tick_left()
    
    #format the x axis
    ax3.set_xlabel('Time (UTC)',fontsize=10)
    ax3.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    
    #Add an overall title with the date
    ax3.set_title('{}'.format(dates[n]), y=1, weight='bold')  # Adjust the vertical position (0 to 1)
    

    #make colorbar
    cb5 = plt.colorbar(sc5)
    ticks = cb5.get_ticks()
    # Round the ticks to 2 decimal places and convert to strings
    rounded_labels = [int(tick) for tick in ticks]
    cb5.ax.set_yticklabels(rounded_labels)
    cb5.set_label('GEOS CO (mol/mol)', fontsize=10)
    cb5.ax.tick_params(labelsize=10)
    fig3.tight_layout()
    # Move the colorbar to the right
    cb5.ax.set_position([0.95, 0.1, 0.02, 0.8])
    
    #save it out
    sPath = 'C:\\Users\\okorn\\Documents\\COMA-main\\RB Plots - AGU\\'
    #Create the full path with the figure name
    savePath = os.path.join(sPath,'Altitude_GEOS_CO_{}'.format(dateAKA))
    # Save the figure to a filepath
    fig3.savefig(savePath, bbox_inches='tight')
