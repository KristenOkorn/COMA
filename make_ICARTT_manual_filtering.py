# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 06:21:07 2022

@author: okorn
"""

# -*- coding: utf-8 -*-
"""
Output manually data to archive format for NASA DAAC

- Can look up flight start & end times here: https://catalog.eol.ucar.edu/acclip/missions
Before adding to DAAC:
- apply calibration factor to CO, N2O
- verify format of ICARTT header
"""

#***************
#acclip-COMA-CON2O_WB57_20220806_RA.ict'
# %% set up
# import libraries
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from load_flight_functions import read_COMA

#revision date (today's date)
r_year = '2022'
r_month = '08'
r_day = '31'

# select file to export
case = '2022-08-16'

if case == '2022-08-02':
    filename_COMA = ['../Data/2022-08-02/n2o-co_2022-08-02_f0000.txt']
    output_name = 'COMA_WB57_20220802_RA.ict'
    t0 = datetime(2022,8,2,1,10)
    t1 = datetime(2022,8,2,6,33)
    year = '2022'
    month = '08'
    day = '02'
elif case == '2022-08-04':
    filename_COMA = ['../Data/2022-08-04/n2o-co_2022-08-04_f0000.txt']
    output_name = 'COMA_WB57_20220804_RA.ict'
    t0 = datetime(2022,8,4,1,12)
    t1 = datetime(2022,8,4,6,18)
    year = '2022'
    month = '08'
    day = '04'
elif case == '2022-08-06':
    filename_COMA = ['../Data/2022-08-06/n2o-co_2022-08-06_f0000.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220806_RA.ict'
    t0 = datetime(2022,8,6,1,15)
    t1 = datetime(2022,8,6,7,9)
    cal_starts = {'cal_1' : datetime(2022,8,6,1,29,11),
                  'cal_2' : datetime(2022,8,6,2,15,13),
                  'cal_3' : datetime(2022,8,6,3,1,14),
                  'cal_4' : datetime(2022,8,6,3,47,14),
                  'cal_5' : datetime(2022,8,6,4,33,15),
                  'cal_6' : datetime(2022,8,6,5,19,13),
                  'cal_7' : datetime(2022,8,6,6,5,10),
                  'cal_8' : datetime(2022,8,6,6,51,10)
                  }
    cal_ends = {'cal_1' : datetime(2022,8,6,1,31,57),
                'cal_2' : datetime(2022,8,6,2,17,59),
                'cal_3' : datetime(2022,8,6,3,3,38),
                'cal_4' : datetime(2022,8,6,3,49,42),
                'cal_5' : datetime(2022,8,6,4,36,12),
                'cal_6' : datetime(2022,8,6,5,22,12),
                'cal_7' : datetime(2022,8,6,6,8,12),
                'cal_8' : datetime(2022,8,6,6,55,6)
                }
    press_starts = {"badP_1" : datetime(2022,8,6,6,21,27)}
    press_ends = {"badP_1" : datetime(2022,8,6,6,55,12)}
    year = '2022'
    month = '08'
    day = '06'
elif case == '2022-08-12':
    filename_COMA = ['../Data/2022-08-12/n2o-co_2022-08-12_f0000.txt']
    output_name = 'COMA_WB57_20220812_RA.ict'
    t0 = datetime(2022,8,12,2,10)
    t1 = datetime(2022,8,12,8,0)
    year = '2022'
    month = '08'
    day = '12'
elif case == '2022-08-15':
    filename_COMA = ['../Data/2022-08-15/n2o-co_2022-08-15_f0000.txt']
    output_name = 'COMA_WB57_20220815_RA.ict'
    t0 = datetime(2022,8,15,3,29)
    t1 = datetime(2022,8,15,8,9)
    year = '2022'
    month = '08'
    day = '15'
elif case == '2022-08-16':
    filename_COMA = ['../Data/2022-08-16/n2o-co_2022-08-16_f0000.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220816_RA.ict'
    t0 = datetime(2022,8,16,3,10)
    t1 = datetime(2022,8,16,8,17)
    cal_starts = {'cal_1' : datetime(2022,8,16,3,29,13),
                  'cal_2' : datetime(2022,8,16,4,14,13),
                  'cal_3' : datetime(2022,8,16,4,59,13),
                  'cal_4' : datetime(2022,8,16,5,44,13),
                  'cal_5' : datetime(2022,8,16,6,29,13),
                  'cal_6' : datetime(2022,8,16,7,14,13),
                  'cal_7' : datetime(2022,8,16,7,59,13)
                  }
    cal_ends = {'cal_1' : datetime(2022,8,16,3,30,37),
                'cal_2' : datetime(2022,8,16,4,15,36),
                'cal_3' : datetime(2022,8,16,5,0,40),
                'cal_4' : datetime(2022,8,16,5,45,44),
                'cal_5' : datetime(2022,8,16,6,31,4),
                'cal_6' : datetime(2022,8,16,7,15,58),
                'cal_7' : datetime(2022,8,16,8,0,38)
                }
    press_starts = {"badP_1" : datetime(2022,8,16,7,51,18)}
    press_ends = {"badP_1" : datetime(2022,8,16,8,17,0)}
    year = '2022'
    month = '08'
    day = '16'
elif case == '2022-08-19':
    filename_COMA = ['../Data/2022-08-19/n2o-co_2022-08-19_f0000.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220819_RA.ict'
    t0 = datetime(2022,8,19,0,30)
    t1 = datetime(2022,8,19,6,15)
    cal_starts = {#'cal_1' : datetime(2022,8,19,0,25,17),
                  'cal_2' : datetime(2022,8,19,1,10,17),
                  'cal_3' : datetime(2022,8,19,1,55,17),
                  'cal_4' : datetime(2022,8,19,2,40,17),
                  'cal_5' : datetime(2022,8,19,3,25,17),
                  'cal_6' : datetime(2022,8,19,4,10,17),
                  'cal_7' : datetime(2022,8,19,4,55,17),
                  'cal_8' : datetime(2022,8,19,5,40,17)
                  }
    cal_ends = {#'cal_1' : datetime(2022,8,19,0,26,54),
                'cal_2' : datetime(2022,8,19,1,11,49),
                'cal_3' : datetime(2022,8,19,1,56,45),
                'cal_4' : datetime(2022,8,19,2,41,49),
                'cal_5' : datetime(2022,8,19,3,26,49),
                'cal_6' : datetime(2022,8,19,4,12,1),
                'cal_7' : datetime(2022,8,19,4,57,11),
                'cal_8' : datetime(2022,8,19,5,42,11)
                }
    press_starts = {"badP_1" : datetime(2022,8,19,5,47,0)}
    press_ends = {"badP_1" : datetime(2022,8,19,6,15,0)}
    year = '2022'
    month = '08'
    day = '19'
elif case == '2022-08-21':
    filename_COMA = ['../Data/2022-08-21/n2o-co_2022-08-21_f0000.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220821_RA.ict'
    t0 = datetime(2022,8,21,0,35)
    t1 = datetime(2022,8,21,6,31)
    cal_starts = {'cal_1' : datetime(2022,8,21,1,22,12),
                  'cal_2' : datetime(2022,8,21,2,7,12),
                  'cal_3' : datetime(2022,8,21,2,52,12),
                  'cal_4' : datetime(2022,8,21,3,37,12),
                  'cal_5' : datetime(2022,8,21,4,22,12),
                  'cal_6' : datetime(2022,8,21,5,7,12),
                  'cal_7' : datetime(2022,8,21,5,52,12)
                  }
    cal_ends = {'cal_1' : datetime(2022,8,21,1,23,35),
                'cal_2' : datetime(2022,8,21,2,8,38),
                'cal_3' : datetime(2022,8,21,2,53,38),
                'cal_4' : datetime(2022,8,21,3,39,11),
                'cal_5' : datetime(2022,8,21,4,23,53),
                'cal_6' : datetime(2022,8,21,5,8,56),
                'cal_7' : datetime(2022,8,21,5,53,54)
                }
    press_starts = {"badP_1" : datetime(2022,8,21,4,22,17),
                    "badP_2" : datetime(2022,8,21,0,38,40)
                    }
    press_ends = {"badP_1" : datetime(2022,8,21,4,29,10),
                  "badP_2" : datetime(2022,8,21,0,52,44)
                  }
    year = '2022'
    month = '08'
    day = '21'
elif case == '2022-08-25':
    filename_COMA = ['../Data/2022-08-25/n2o-co_2022-08-25_corrected.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220825_RA.ict'
    t0 = datetime(2022,8,25,1,00)
    t1 = datetime(2022,8,25,6,35)
    cal_starts = {'cal_1' : datetime(2022,8,25,1,22,53),
                  'cal_2' : datetime(2022,8,25,2,7,53),
                  'cal_3' : datetime(2022,8,25,2,52,53),
                  'cal_4' : datetime(2022,8,25,3,37,53),
                  'cal_5' : datetime(2022,8,25,4,22,53),
                  'cal_6' : datetime(2022,8,25,5,7,53),
                  'cal_7' : datetime(2022,8,25,5,52,53)
                  }
    cal_ends = {'cal_1' : datetime(2022,8,25,1,24,16),
                'cal_2' : datetime(2022,8,25,2,9,18),
                'cal_3' : datetime(2022,8,25,2,54,18),
                'cal_4' : datetime(2022,8,25,3,39,25),
                'cal_5' : datetime(2022,8,25,4,24,46),
                'cal_6' : datetime(2022,8,25,5,9,37),
                'cal_7' : datetime(2022,8,25,5,54,36)
                }
    year = '2022'
    month = '08'
    day = '25'
elif case == '2022-08-26':
    filename_COMA = ['../Data/2022-08-26/n2o-co_2022-08-26_f0000.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220826_RA.ict'
    t0 = datetime(2022,8,26,0,55)
    t1 = datetime(2022,8,26,6,55)
    cal_starts = {'cal_1' : datetime(2022,8,26,1,25,49),
                  'cal_2' : datetime(2022,8,26,2,10,49),
                  'cal_3' : datetime(2022,8,26,2,55,49),
                  'cal_4' : datetime(2022,8,26,3,40,49),
                  'cal_5' : datetime(2022,8,26,4,25,49),
                  'cal_6' : datetime(2022,8,26,5,10,49),
                  'cal_7' : datetime(2022,8,26,5,55,49),
                  'cal_8' : datetime(2022,8,26,6,40,49)
                  }
    cal_ends = {'cal_1' : datetime(2022,8,26,1,27,13),
                'cal_2' : datetime(2022,8,26,2,12,16),
                'cal_3' : datetime(2022,8,26,2,57,14),
                'cal_4' : datetime(2022,8,26,3,42,20),
                'cal_5' : datetime(2022,8,26,4,27,26),
                'cal_6' : datetime(2022,8,26,5,12,34),
                'cal_7' : datetime(2022,8,26,5,57,42),
                'cal_8' : datetime(2022,8,26,6,42,15),
                }
    press_starts = {"badP_1" : datetime(2022,8,26,5,55,45)}
    press_ends = {"badP_1" : datetime(2022,8,26,5,57,15)}
    year = '2022'
    month = '08'
    day = '26'

# read COMA data
COMA = read_COMA(filename_COMA)

#remove empty spaces in data for workability
COMA.columns = COMA.columns.str.strip()

#make sure our time column was imported as a datetime (w fractional seconds)
COMA['Time']= pd.to_datetime(COMA['Time'],infer_datetime_format=True)
                             #format='%m/%d/%Y %H:%M:%S.%f')

# filter to between takeoff (t0) and landing (t1)
ix_flight = np.ravel( np.where((COMA["time"]>t0) & 
                               (COMA["time"]<t1)) )

# create DataFrame with desired variables
#initialize new time variables here
df = pd.DataFrame({'Time_Start': COMA["Time"][ix_flight],
                   'Time_Mid':np.empty((len(COMA["Time"][ix_flight]),), dtype=datetime),
                   'Time_End':np.empty((len(COMA["Time"][ix_flight]),), dtype=datetime),
                    'CO': COMA['[CO]d_ppm'][ix_flight],
                    'N2O': COMA['[N2O]d_ppm'][ix_flight]})

#make sure our time columns were imported as datetimes (w fractional seconds) (again)
df['Time_Start']= pd.to_datetime(df['Time_Start'],infer_datetime_format=True)
df['Time_Mid']= pd.to_datetime(df['Time_Mid'],infer_datetime_format=True)
df['Time_End']= pd.to_datetime(df['Time_End'],infer_datetime_format=True)

#reset the index to make it start at 0
df = df.reset_index(drop=True)

#now populate time_mid and time_end
for index, row in df.iterrows():
    #first make sure we don't go out of bounds
    if index < len(df) -1:
        #Set the Time_End to 1 millisecond before the next Time_Start
        df.iloc[index,2] = df.iloc[index+1,0] - timedelta(milliseconds=1)
        #Set the Time_Mid to the midpoint of Time_Start and Time_End
        df.iloc[index,1] = df.iloc[index,0] +0.5 * (df.iloc[index,2] - df.iloc[index,0])
    #for final row, assume an end time
    else:
        #Assume an end time of 1s after Time_Start
        df.iloc[index,2] = df.iloc[index,0] + timedelta(milliseconds=1000)
        #Set the midpoint to 0.5s after Time_Start
        df.iloc[index,1] = df.iloc[index,0] +0.5 * timedelta(milliseconds=1000)

#replace CO and N2O with -9.999 during calibration cycle times
if 'cal_starts' in locals():
    cal_starts_vals = list(cal_starts.values())
    cal_ends_vals = list(cal_ends.values())
    for i in range(len(cal_starts)):
        cal_ix = np.asarray(np.where((df['Time_Start']>= cal_starts_vals[i]) & (df['Time_Start']<= cal_ends_vals[i]))).T
        df.loc[cal_ix[0,0]:cal_ix[len(cal_ix)-1,0],'CO'] = -9.999
        df.loc[cal_ix[0,0]:cal_ix[len(cal_ix)-1,0],'N2O'] = -9.999

#replace N2O  with -9.999 during flagged pressure times
if 'press_starts' in locals():
    press_starts_vals = list(press_starts.values())
    press_ends_vals = list(press_ends.values())
    for i in range(len(press_starts)):
        press_ix = np.asarray(np.where((df['Time_Start']>= press_starts_vals[i]) & (df['Time_Start']<= press_ends_vals[i]))).T
        df.loc[press_ix[0,0]:press_ix[len(press_ix)-1,0],'N2O'] = -9.999

# %% output data
# convert timestamp to seconds after midnight
start_time_midnight = [(t.hour * 3600) + (t.minute * 60) + t.second + (t.microsecond / 1000000.0) for t in df['Time_Start']]
mid_time_midnight = [(t.hour * 3600) + (t.minute * 60) + t.second + (t.microsecond / 1000000.0) for t in df["Time_Mid"]]
end_time_midnight = [(t.hour * 3600) + (t.minute * 60) + t.second + (t.microsecond / 1000000.0) for t in df["Time_End"]]

#save out a version with normal datetime stamps for easier plotting
df.to_excel('{}_cleaned.xls'.format(case))

# create final DataFrame with desired variables
#convert CO and N2O to ppbv here as well
df = pd.DataFrame({'Time_Start': start_time_midnight,
                   'Time_Mid': mid_time_midnight,
                   'Time_End': end_time_midnight,
                    'CO': df['CO'] * 1000,
                    'N2O': df['N2O'] * 1000})


# loop that saves string formatted (commas, decimal places) data
# create new file; overwrites if needed
with open(output_name,"w") as ofile:
     fmt = '%.1f, %.1f, %.1f, %6.2f, %6.2f'
     np.savetxt(ofile, df.values, fmt=fmt)

#create file header
# refer to ICARTT 2.0 specifications for more details
header = '36,V02_2016\n' # number of lines in header, file format index
header += 'Podolske, James\n' # PI name
header += 'NASA Ames Research Center\n' # PI affiliation
header += 'Carbon monOxide Measurement from Ames (COMA)\n' # data source description
header += 'ACCLIP 2022\n' # mission name
header += '1,1\n' # file volume number, total number of file volumes
header += '{}, {}, {}, {}, {}, {}\n'.format(year,month,day,r_year,r_month,r_day) # date of data collection, date of most recent revision
header += '0\n' # data interval code
header += 'Time_Start, seconds, elapsed time from 0000 UTC   \n' # name of independent variable, units of variable
header += '4\n' # number of dependent variables
header += '1,1,1,1\n' # scale factors of dependent variables
header += '-9999.00,-9999.00,-9999.00,-9999.00\n' # missing data flags of dependent variables
header += 'Time_Mid, seconds, elapsed time from 0000 UTC\n' # dependent variable short name, units, standard name
header += 'Time_End, seconds, elapsed time from 0000 UTC\n' # dependent variable short name, units, standard name
header += 'CO, ppbv, Gas_CO_InSitu_S_DVMR\n' # dependent variable short name, units, standard name
header += 'N2O, ppbv, Gas_N2O_InSitu_S_DVMR\n' # (repeat as necessary)
header += '0\n' # number of special comment lines (not including this line)
header += '18\n' # number of normal comment lines (not including this line)
header += 'PI_CONTACT_INFO: James.R.Podolske@nasa.gov\n'
header += 'PLATFORM: NASA WB-57F 926\n'
header += 'LOCATION: Latitude, Longitude, and Altitude included in MMS files\n'
header += 'ASSOCIATED_DATA: N/A\n'
header += 'INSTRUMENT_INFO: In-situ gas-phase CO/N2O Analyzer (LGR/ABB Serial no. 15-0251). Mounted in pallet 3.\n'
header += 'DATA_INFO: Measurements before takeoff, after landing, and during periodic calibration cycles have been omitted. Additionally, N2O data were removed during periods when the measurement cell pressure deviated from the set point (52.8 Torr) by more than 0.25%.\n'
header += 'UNCERTAINTY: to be specified in R0 release\n'
header += 'ULOD_FLAG: -7777\n'
header += 'ULOD_VALUE: N/A\n'
header += 'LLOD_FLAG: -8888\n'
header += 'LLOD_VALUE: N/A\n'
header += 'DM_CONTACT_INFO: James Podolske (James.R.Podolske@nasa.gov)\n'
header += 'PROJECT_INFO: NASA Ames Trace Gas Data (2022 ACCLIP) https://espo.nasa.gov/acclip/\n'
header += 'STIPULATIONS_ON_USE: This is PRELIMINARY data. Users must consult the PI and/or DM prior to use. As a matter of professional courtesy, consideration for co-authorship is expected for publications utilizing this data.\n'
header += 'OTHER_COMMENTS: N/A\n'
header += 'REVISION: RA\n'
header += 'RA: preliminary field data, subject to corrections due to calibrations, time lags, and future analysis results\n'
header += 'Time_Start,Time_Mid,Time_End,CO,N2O\n'

# append the defined header to the already created data file
with open(output_name, 'r+') as f:
    content = f.read()
    f.seek(0, 0)
    f.write(header + content)      

#also save as a csv to re-plot
df.to_csv('edited.csv')  

#delete variables that might mess with our next run
if 'press_starts'in locals():
    del press_starts
if 'cal_starts'in locals():
    del cal_starts
