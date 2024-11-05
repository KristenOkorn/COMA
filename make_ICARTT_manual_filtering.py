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
import joblib

#revision date (today's date)
r_year = '2023'
r_month = '4'
r_day = '7'

# select file to export
case = '2022-07-21-2'

#pollutants (do not edit)
pollutants = ['CO','N2O']

if case == '2022-07-16':
    filename_COMA = ['../Data/2022-07-16/n2o-co_2022-07-16_f0002.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220716_R2.ict'
    t0 = datetime(2022,7,16,14,50)
    t1 = datetime(2022,7,16,15,40)
    cal_starts = {'cal_1' : datetime(2022,7,16,15,13,45),
                  }
    cal_ends = {'cal_1' : datetime(2022,7,16,15,16,15),
                }
    year = '2022'
    month = '07'
    day = '16'
    offset=3.65 #rf01
    
if case == '2022-07-18':
    filename_COMA = ['../Data/2022-07-18/n2o-co_2022-07-18_f0002.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220718_R2.ict'
    t0 = datetime(2022,7,18,15,28)
    t1 = datetime(2022,7,18,21,34)
    cal_starts = {'cal_1' : datetime(2022,7,18,15,41,45),
                  'cal_2' : datetime(2022,7,18,16,11,45),
                  'cal_3' : datetime(2022,7,18,16,41,45),
                  'cal_4' : datetime(2022,7,18,17,11,45),
                  'cal_5' : datetime(2022,7,18,17,41,45),
                  'cal_6' : datetime(2022,7,18,18,11,45),
                  'cal_7' : datetime(2022,7,18,18,41,45),
                  'cal_8' : datetime(2022,7,18,19,11,45),
                  'cal_9' : datetime(2022,7,18,19,41,45),
                  'cal_10': datetime(2022,7,18,20,11,45)
                  }
    cal_ends = {'cal_1' : datetime(2022,7,18,15,44,15),
                'cal_2' : datetime(2022,7,18,16,14,10),
                'cal_3' : datetime(2022,7,18,16,44,10),
                'cal_4' : datetime(2022,7,18,17,14,10),
                'cal_5' : datetime(2022,7,18,17,44,10),
                'cal_6' : datetime(2022,7,18,18,14,10),
                'cal_7' : datetime(2022,7,18,18,44,10),
                'cal_8' : datetime(2022,7,18,19,14,10),
                'cal_9' : datetime(2022,7,18,19,44,10),
                'cal_10': datetime(2022,7,18,20,12,45)
                }
    year = '2022'
    month = '07'
    day = '18'
    offset = 2.5 #rf02
    
elif case == '2022-07-21-1':
    filename_COMA = ['../Data/2022-07-21-1/n2o-co_2022-07-21_1_f0001.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220721_R2_1.ict'
    t0 = datetime(2022,7,21,13,30)
    t1 = datetime(2022,7,21,18,25)
    cal_starts = {'cal_1' : datetime(2022,7,21,14,12,0),
                  'cal_2' : datetime(2022,7,21,14,57,0),
                  'cal_3' : datetime(2022,7,21,15,42,0),
                  'cal_4' : datetime(2022,7,21,16,27,0),
                  'cal_5' : datetime(2022,7,21,17,12,0),
                  'cal_6' : datetime(2022,7,21,17,57,0)
                  }
    cal_ends = {'cal_1' : datetime(2022,7,21,14,14,30),
                'cal_2' : datetime(2022,7,21,14,59,30),
                'cal_3' : datetime(2022,7,21,15,44,30),
                'cal_4' : datetime(2022,7,21,16,29,30),
                'cal_5' : datetime(2022,7,21,17,14,30),
                'cal_6' : datetime(2022,7,21,17,59,30)
                }
    press_starts = {"badP_1" : datetime(2022,7,21,15,42,10)}
    press_ends = {"badP_1" : datetime(2022,7,21,15,44,22)}
    year = '2022'
    month = '07'
    day = '21'
    offset = 7 #tf01
    
elif case == '2022-07-21-2':
    filename_COMA = ['../Data/2022-07-21-2/n2o-co_2022-07-21_f0002.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220721_R2_2.ict'
    t0 = datetime(2022,7,21,21,0)
    t1 = datetime(2022,7,22,0,22)
    cal_starts = {'cal_1' : datetime(2022,7,21,21,6,55),
                  'cal_2' : datetime(2022,7,21,21,51,55),
                  'cal_3' : datetime(2022,7,21,22,36,55),
                  'cal_4' : datetime(2022,7,21,23,21,55),
                  'cal_5' : datetime(2022,7,22,0,6,55)
                 }
    cal_ends = {'cal_1' : datetime(2022,7,21,21,9,15),
                'cal_2' : datetime(2022,7,21,21,54,15),
                'cal_3' : datetime(2022,7,21,22,39,15),
                'cal_4' : datetime(2022,7,21,23,24,15),
                'cal_5' : datetime(2022,7,22,0,9,15)
               }
    year = '2022'
    month = '07'
    day = '21'
    spans_multiple_days = 'yes'
    offset = 4.45 #tf02
    
elif case == '2022-07-24':
    filename_COMA = ['../Data/2022-07-24/n2o-co_2022-07-24_f0000.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220724_R2.ict'
    t0 = datetime(2022,7,24,21,32)
    t1 = datetime(2022,7,25,0,57)
    cal_starts = {'cal_1' : datetime(2022,7,24,22,14,15),
                  'cal_2' : datetime(2022,7,24,22,59,15),
                  'cal_3' : datetime(2022,7,24,23,44,15),
                  'cal_4' : datetime(2022,7,25,0,29,15)
                 }
    cal_ends = {'cal_1' : datetime(2022,7,24,22,16,35),
                'cal_2' : datetime(2022,7,24,23,1,35),
                'cal_3' : datetime(2022,7,24,23,46,35),
                'cal_4' : datetime(2022,7,25,0,31,35)
               }
    year = '2022'
    month = '07'
    day = '24'
    spans_multiple_days = 'yes'
    offset = 4.8 #tf03

elif case == '2022-07-25':
    filename_COMA = ['../Data/2022-07-25/n2o-co_2022-07-25_f0000.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220725_R2.ict'
    t0 = datetime(2022,7,25,22,44)
    t1 = datetime(2022,7,26,4,28)
    cal_starts = {'cal_1' : datetime(2022,7,25,23,19,40),
                  'cal_2' : datetime(2022,7,26,0,4,40),
                  'cal_3' : datetime(2022,7,26,0,49,40),
                  'cal_4' : datetime(2022,7,26,1,34,40),
                  'cal_5' : datetime(2022,7,26,2,19,40),
                  'cal_6' : datetime(2022,7,26,3,4,40),
                  'cal_7' : datetime(2022,7,26,3,49,40)
                 }
    cal_ends = {'cal_1' : datetime(2022,7,25,23,22,0),
                'cal_2' : datetime(2022,7,26,0,7,0),
                'cal_3' : datetime(2022,7,26,0,52,0),
                'cal_4' : datetime(2022,7,26,1,37,0),
                'cal_5' : datetime(2022,7,26,2,22,0),
                'cal_6' : datetime(2022,7,26,3,7,0),
                'cal_7' : datetime(2022,7,26,3,52,0)
                }
    year = '2022'
    month = '07'
    day = '25'
    spans_multiple_days = 'yes'
    offset = 5.6 #tf04
    
elif case == '2022-07-27':
    filename_COMA = ['../Data/2022-07-27/n2o-co_2022-07-27_f0000.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220727_R2.ict'
    t0 = datetime(2022,7,27,1,11)
    t1 = datetime(2022,7,27,3,50)
    cal_starts = {'cal_1' : datetime(2022,7,27,1,33,40),
                  'cal_2' : datetime(2022,7,27,2,18,40),
                  'cal_3' : datetime(2022,7,27,3,3,40),
                  'cal_4' : datetime(2022,7,27,3,48,40)
                 }
    cal_ends = {'cal_1' : datetime(2022,7,27,1,36,0),
                'cal_2' : datetime(2022,7,27,2,21,0),
                'cal_3' : datetime(2022,7,27,3,6,0),
                'cal_4' : datetime(2022,7,27,3,51,0)
               }
    press_starts = {"badP_3" : datetime(2022,7,27,3,26,53)
                    }
    press_ends = {"badP_3" : datetime(2022,7,27,3,50)
                  }
    year = '2022'
    month = '07'
    day = '27'
    offset = 6.8 #tf05
    
elif case == '2022-08-02':
    filename_COMA = ['../Data/2022-08-02/n2o-co_2022-08-02_f0000.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220802_R2.ict'
    t0 = datetime(2022,8,2,1,15)
    t1 = datetime(2022,8,2,6,33)
    cal_starts = {'cal_1' : datetime(2022,8,2,1,41,0),
                  'cal_2' : datetime(2022,8,2,2,26,0),
                  'cal_3' : datetime(2022,8,2,3,11,0),
                  'cal_4' : datetime(2022,8,2,3,56,0),
                  'cal_5' : datetime(2022,8,2,4,41,0),
                  'cal_6' : datetime(2022,8,2,5,26,0),
                  'cal_7' : datetime(2022,8,2,6,11,0)
                 }
    cal_ends = {'cal_1' : datetime(2022,8,2,1,43,25),
                'cal_2' : datetime(2022,8,2,2,28,25),
                'cal_3' : datetime(2022,8,2,3,13,25),
                'cal_4' : datetime(2022,8,2,3,58,25),
                'cal_5' : datetime(2022,8,2,4,43,25),
                'cal_6' : datetime(2022,8,2,5,28,25),
                'cal_7' : datetime(2022,8,2,6,13,0)
                }
    year = '2022'
    month = '08'
    day = '02'
    offset = 2.4 #rf03
    
elif case == '2022-08-04':
    filename_COMA = ['../Data/2022-08-04/n2o-co_2022-08-04_f0000.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220804_R2.ict'
    t0 = datetime(2022,8,4,1,30)
    t1 = datetime(2022,8,4,6,18)
    cal_starts = {'cal_1' : datetime(2022,8,4,2,10,50),
                  'cal_2' : datetime(2022,8,4,2,55,50),
                  'cal_3' : datetime(2022,8,4,3,40,50),
                  'cal_4' : datetime(2022,8,4,4,27,50),
                  'cal_5' : datetime(2022,8,4,5,10,50),
                  'cal_6' : datetime(2022,8,4,5,55,50),
                  'bad_P' : datetime(2022,8,4,4,26)
                 }
    cal_ends = {'cal_1' : datetime(2022,8,4,2,13,10),
                'cal_2' : datetime(2022,8,4,2,58,10),
                'cal_3' : datetime(2022,8,4,3,43,10),
                'cal_4' : datetime(2022,8,4,4,28,10),
                'cal_5' : datetime(2022,8,4,5,13,10),
                'cal_6' : datetime(2022,8,4,5,58,10),
                'bad_P' : datetime(2022,8,4,4,27,50)
                }
    year = '2022'
    month = '08'
    day = '04'
    offset = 2.1 #rf04
    
elif case == '2022-08-06':
    filename_COMA = ['../Data/2022-08-06/n2o-co_2022-08-06_f0000.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220806_R2.ict'
    t0 = datetime(2022,8,6,1,3)
    t1 = datetime(2022,8,6,7,9)
    cal_starts = {'cal_1' : datetime(2022,8,6,1,29,0),
                  'cal_2' : datetime(2022,8,6,2,15,0),
                  'cal_3' : datetime(2022,8,6,3,1,0),
                  'cal_4' : datetime(2022,8,6,3,47,0),
                  'cal_5' : datetime(2022,8,6,4,33,0),
                  'cal_6' : datetime(2022,8,6,5,18,40),
                  'cal_7' : datetime(2022,8,6,6,5,0),
                  'cal_8' : datetime(2022,8,6,6,51,0),
                  "badP_1" : datetime(2022,8,6,6,21,27) #cut out CO also
                  }
    cal_ends = {'cal_1' : datetime(2022,8,6,1,32,10),
                'cal_2' : datetime(2022,8,6,2,18,10),
                'cal_3' : datetime(2022,8,6,3,3,50),
                'cal_4' : datetime(2022,8,6,3,50,25),
                'cal_5' : datetime(2022,8,6,4,37,5),
                'cal_6' : datetime(2022,8,6,5,22,25),
                'cal_7' : datetime(2022,8,6,6,8,25),
                'cal_8' : datetime(2022,8,6,6,55,20),
                "badP_1" : datetime(2022,8,6,6,55,12) #cut out CO also
                }
    year = '2022'
    month = '08'
    day = '06'
    offset = 2.2 #rf05
    
elif case == '2022-08-12':
    filename_COMA = ['../Data/2022-08-12/n2o-co_2022-08-12_f0000.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220812_R2.ict'
    t0 = datetime(2022,8,12,2,25)
    t1 = datetime(2022,8,12,8,0)
    cal_starts = {'cal_1' : datetime(2022,8,12,2,48,10),
                  'cal_2' : datetime(2022,8,12,3,33,10),
                  'cal_3' : datetime(2022,8,12,4,18,10),
                  'cal_4' : datetime(2022,8,12,5,3,10),
                  'cal_5' : datetime(2022,8,12,5,48,10),
                  'cal_6' : datetime(2022,8,12,6,33,10),
                  'cal_7' : datetime(2022,8,12,7,18,10)
                  }
    cal_ends = {'cal_1' : datetime(2022,8,12,2,50,25),
                'cal_2' : datetime(2022,8,12,3,35,25),
                'cal_3' : datetime(2022,8,12,4,20,25),
                'cal_4' : datetime(2022,8,12,5,5,25),
                'cal_5' : datetime(2022,8,12,5,50,25),
                'cal_6' : datetime(2022,8,12,6,35,25),
                'cal_7' : datetime(2022,8,12,7,20,25)
                }
    year = '2022'
    month = '08'
    day = '12'
    offset = 1 #rf06
    
elif case == '2022-08-13':
    filename_COMA = ['../Data/2022-08-13/n2o-co_2022-08-13_f0000.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220813_R2.ict'
    t0 = datetime(2022,8,13,1,12)
    t1 = datetime(2022,8,13,6,3)
    cal_starts = {'cal_1' : datetime(2022,8,13,1,34,30),
                  'cal_2' : datetime(2022,8,13,2,19,30),
                  'cal_3' : datetime(2022,8,13,3,4,30),
                  'cal_4' : datetime(2022,8,13,3,49,30),
                  'cal_5' : datetime(2022,8,13,4,34,30),
                  'cal_6' : datetime(2022,8,13,5,19,30),
                  "badP_2" : datetime(2022,8,13,5,11,50) #remove CO also
                  }
    cal_ends = {'cal_1' : datetime(2022,8,13,1,36,45),
                'cal_2' : datetime(2022,8,13,2,21,45),
                'cal_3' : datetime(2022,8,13,3,6,45),
                'cal_4' : datetime(2022,8,13,3,51,45),
                'cal_5' : datetime(2022,8,13,4,36,45),
                'cal_6' : datetime(2022,8,13,5,21,45),
                "badP_2" : datetime(2022,8,13,6,3,0) #remove CO also
                }
    year = '2022'
    press_starts = {"badP_1" : datetime(2022,8,13,3,40,49)}
    press_ends = {"badP_1" : datetime(2022,8,13,3,51,59)}
    year = '2022'
    month = '08'
    day = '13'
    offset = 1.2 #rf07
    
elif case == '2022-08-15':
    filename_COMA = ['../Data/2022-08-15/n2o-co_2022-08-15_combined.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220815_R2.ict'
    t0 = datetime(2022,8,15,3,35)
    t1 = datetime(2022,8,15,8,9)
    cal_starts = {'cal_1' : datetime(2022,8,15,3,56,50),
                  'cal_2' : datetime(2022,8,15,5,47,30),
                  'cal_3' : datetime(2022,8,15,6,32,30),
                  'cal_4' : datetime(2022,8,15,7,17,30),
                  'cal_5' : datetime(2022,8,15,8,2,30),
                  'sus1' : datetime(2022,8,15,4,40)
                  }
    cal_ends = {'cal_1' : datetime(2022,8,15,3,59,5),
                'cal_2' : datetime(2022,8,15,5,49,45),
                'cal_3' : datetime(2022,8,15,6,34,45),
                'cal_4' : datetime(2022,8,15,7,19,45),
                'cal_5' : datetime(2022,8,15,8,4,45),
                'sus2' : datetime(2022,8,15,4,44,40)
                }
    #also have to flag data from power cycle
    cycle_starts = {'cycle_1' : datetime(2022,8,15,4,51,22)} #only times when data doesn't exist
    cycle_ends = {'cycle_1' : datetime(2022,8,15,5,4,38)}
    other_starts = {'other_1' : datetime(2022,8,15,4,44,40),
                    'other_2' : datetime(2022,8,15,4,39),
                    'other_3' : datetime(2022,8,15,6,27) #cut out CO also during oscillations
                    } #other times to cut out (i.e. instrument warmup after power cycle)
    other_ends = {'other_1' : datetime(2022,8,15,4,51,22),
                  'other_2' : datetime(2022,8,15,4,40),
                  'other_3' : datetime(2022,8,15,7,23)
                  } #will remove both CO & N2O
    year = '2022'
    month = '08'
    day = '15'
    offset = 1.6 #rf08
    
elif case == '2022-08-16':
    filename_COMA = ['../Data/2022-08-16/n2o-co_2022-08-16_f0000.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220816_R2.ict'
    t0 = datetime(2022,8,16,3,8)
    t1 = datetime(2022,8,16,8,17)
    cal_starts = {'cal_1' : datetime(2022,8,16,3,29,10),
                  'cal_2' : datetime(2022,8,16,4,14,10),
                  'cal_3' : datetime(2022,8,16,4,59,10),
                  'cal_4' : datetime(2022,8,16,5,44,10),
                  'cal_5' : datetime(2022,8,16,6,29,10),
                  'cal_6' : datetime(2022,8,16,7,14,10),
                  'cal_7' : datetime(2022,8,16,7,59,10),
                  "badP_1" : datetime(2022,8,16,7,51,18) #also cut out CO
                  }
    cal_ends = {'cal_1' : datetime(2022,8,16,3,31,0),
                'cal_2' : datetime(2022,8,16,4,16,0),
                'cal_3' : datetime(2022,8,16,5,1,0),
                'cal_4' : datetime(2022,8,16,5,46,0),
                'cal_5' : datetime(2022,8,16,6,31,20),
                'cal_6' : datetime(2022,8,16,7,16,20),
                'cal_7' : datetime(2022,8,16,8,0,0),
                "badP_1" : datetime(2022,8,16,8,17,0)
                }
    year = '2022'
    month = '08'
    day = '16'
    offset = 2.9 #rf09
    
elif case == '2022-08-19':
    filename_COMA = ['../Data/2022-08-19/n2o-co_2022-08-19_f0000.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220819_R2.ict'
    t0 = datetime(2022,8,19,0,25)
    t1 = datetime(2022,8,19,6,15)
    cal_starts = {'cal_1' : datetime(2022,8,19,0,25,10),
                  'cal_2' : datetime(2022,8,19,1,10,10),
                  'cal_3' : datetime(2022,8,19,1,55,0),
                  'cal_4' : datetime(2022,8,19,2,40,5),
                  'cal_5' : datetime(2022,8,19,3,25,10),
                  'cal_6' : datetime(2022,8,19,4,10,10),
                  'cal_7' : datetime(2022,8,19,4,55,10),
                  'cal_8' : datetime(2022,8,19,5,40,10),
                  "badP_1" : datetime(2022,8,19,5,47,0)
                  }
    cal_ends = {'cal_1' : datetime(2022,8,19,0,27,0),
                'cal_2' : datetime(2022,8,19,1,13,0),
                'cal_3' : datetime(2022,8,19,1,57,5),
                'cal_4' : datetime(2022,8,19,2,42,10),
                'cal_5' : datetime(2022,8,19,3,27,5),
                'cal_6' : datetime(2022,8,19,4,12,25),
                'cal_7' : datetime(2022,8,19,4,57,25),
                'cal_8' : datetime(2022,8,19,5,42,30),
                "badP_1" : datetime(2022,8,19,6,15,0)
                }
    year = '2022'
    month = '08'
    day = '19'
    offset = 2.2 #rf10
    
elif case == '2022-08-21':
    filename_COMA = ['../Data/2022-08-21/n2o-co_2022-08-21_f0000.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220821_R2.ict'
    t0 = datetime(2022,8,21,1,0)
    t1 = datetime(2022,8,21,6,31)
    cal_starts = {'cal_1' : datetime(2022,8,21,1,22,5),
                  'cal_2' : datetime(2022,8,21,2,7,5),
                  'cal_3' : datetime(2022,8,21,2,52,5),
                  'cal_4' : datetime(2022,8,21,3,37,5),
                  'cal_5' : datetime(2022,8,21,4,22,5),
                  'cal_6' : datetime(2022,8,21,5,7,5),
                  'cal_7' : datetime(2022,8,21,5,52,5)
                  }
    cal_ends = {'cal_1' : datetime(2022,8,21,1,23,50),
                'cal_2' : datetime(2022,8,21,2,8,50),
                'cal_3' : datetime(2022,8,21,2,53,53),
                'cal_4' : datetime(2022,8,21,3,39,25),
                'cal_5' : datetime(2022,8,21,4,24,10),
                'cal_6' : datetime(2022,8,21,5,9,10),
                'cal_7' : datetime(2022,8,21,5,54,15)
                }
    press_starts = {"badP_1" : datetime(2022,8,21,4,22,17)}
    press_ends = {"badP_1" : datetime(2022,8,21,4,29,10)}
    year = '2022'
    month = '08'
    day = '21'
    offset = 1.8 #rf11
    
elif case == '2022-08-23':
    filename_COMA = ['../Data/2022-08-23/n2o-co_2022-08-23_f0000.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220823_R2.ict'
    t0 = datetime(2022,8,23,1,45)
    t1 = datetime(2022,8,23,7,47)
    cal_starts = {'cal_1' : datetime(2022,8,23,2,6,35),
                  'cal_2' : datetime(2022,8,23,2,51,40),
                  'cal_3' : datetime(2022,8,23,3,36,40),
                  'cal_4' : datetime(2022,8,23,4,21,40),
                  'cal_5' : datetime(2022,8,23,5,6,40),
                  'cal_6' : datetime(2022,8,23,5,51,40),
                  'cal_7' : datetime(2022,8,23,6,36,40),
                  'cal_8' : datetime(2022,8,23,7,21,40),
                  "badP_1" : datetime(2022,8,23,7,22,55)
                  }
    cal_ends = {'cal_1' : datetime(2022,8,23,2,8,33),
                'cal_2' : datetime(2022,8,23,2,53,33),
                'cal_3' : datetime(2022,8,23,3,38,28),
                'cal_4' : datetime(2022,8,23,4,23,42),
                'cal_5' : datetime(2022,8,23,5,8,47),
                'cal_6' : datetime(2022,8,23,5,53,50),
                'cal_7' : datetime(2022,8,23,6,38,45),
                'cal_8' : datetime(2022,8,23,7,23,35),
                "badP_1" : datetime(2022,8,23,7,47,0)
                }
    year = '2022'
    month = '08'
    day = '23'
    offset = 1.35 #rf12
    
elif case == '2022-08-25':
    filename_COMA = ['../Data/2022-08-25/n2o-co_2022-08-25_corrected.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220825_R2.ict'
    t0 = datetime(2022,8,25,1,0)
    t1 = datetime(2022,8,25,6,35)
    cal_starts = {'cal_1' : datetime(2022,8,25,1,22,45),
                  'cal_2' : datetime(2022,8,25,2,7,45),
                  'cal_3' : datetime(2022,8,25,2,52,45),
                  'cal_4' : datetime(2022,8,25,3,37,45),
                  'cal_5' : datetime(2022,8,25,4,22,45),
                  'cal_6' : datetime(2022,8,25,5,7,45),
                  'cal_7' : datetime(2022,8,25,5,52,45)
                  }
    cal_ends = {'cal_1' : datetime(2022,8,25,1,24,30),
                'cal_2' : datetime(2022,8,25,2,9,35),
                'cal_3' : datetime(2022,8,25,2,54,38),
                'cal_4' : datetime(2022,8,25,3,39,45),
                'cal_5' : datetime(2022,8,25,4,25,15),
                'cal_6' : datetime(2022,8,25,5,10,5),
                'cal_7' : datetime(2022,8,25,5,55,0)
                }
    year = '2022'
    month = '08'
    day = '25'
    offset = 1.9 #rf13
    
elif case == '2022-08-26':
    filename_COMA = ['../Data/2022-08-26/n2o-co_2022-08-26_f0000.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220826_R2.ict'
    t0 = datetime(2022,8,26,1,0)
    t1 = datetime(2022,8,26,6,55)
    cal_starts = {'cal_1' : datetime(2022,8,26,1,25,38),
                  'cal_2' : datetime(2022,8,26,2,10,38),
                  'cal_3' : datetime(2022,8,26,2,55,38),
                  'cal_4' : datetime(2022,8,26,3,40,38),
                  'cal_5' : datetime(2022,8,26,4,25,38),
                  'cal_6' : datetime(2022,8,26,5,10,38),
                  'cal_7' : datetime(2022,8,26,5,55,38),
                  'cal_8' : datetime(2022,8,26,6,40,38)
                  }
    cal_ends = {'cal_1' : datetime(2022,8,26,1,27,43),
                'cal_2' : datetime(2022,8,26,2,12,36),
                'cal_3' : datetime(2022,8,26,2,57,34),
                'cal_4' : datetime(2022,8,26,3,42,40),
                'cal_5' : datetime(2022,8,26,4,27,46),
                'cal_6' : datetime(2022,8,26,5,12,50),
                'cal_7' : datetime(2022,8,26,5,58,2),
                'cal_8' : datetime(2022,8,26,6,42,32),
                }
    press_starts = {"badP_1" : datetime(2022,8,26,5,55,45)}
    press_ends = {"badP_1" : datetime(2022,8,26,5,57,15)}
    year = '2022'
    month = '08'
    day = '26'
    offset = 0.8 #rf14
    
elif case == '2022-08-29':
    filename_COMA = ['../Data/2022-08-29/n2o-co_2022-08-29_f0000.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220829_R2.ict'
    t0 = datetime(2022,8,29,1,10)
    t1 = datetime(2022,8,29,7,0)
    cal_starts = {'cal_1' : datetime(2022,8,29,1,25,40),
                  'cal_2' : datetime(2022,8,29,2,10,40),
                  'cal_3' : datetime(2022,8,29,2,55,40),
                  'cal_4' : datetime(2022,8,29,3,40,40),
                  'cal_5' : datetime(2022,8,29,4,25,40),
                  'cal_6' : datetime(2022,8,29,5,10,40),
                  'cal_7' : datetime(2022,8,29,5,55,40),
                  'cal_8' : datetime(2022,8,29,6,40,40),
                  "badP_1" : datetime(2022,8,29,6,33,45)
                  }
    cal_ends = {'cal_1' : datetime(2022,8,29,1,27,37),
                'cal_2' : datetime(2022,8,29,2,12,28),
                'cal_3' : datetime(2022,8,29,2,57,33),
                'cal_4' : datetime(2022,8,29,3,42,45),
                'cal_5' : datetime(2022,8,29,4,27,56),
                'cal_6' : datetime(2022,8,29,5,12,50),
                'cal_7' : datetime(2022,8,29,5,57,55),
                'cal_8' : datetime(2022,8,29,6,42,30),
                "badP_1" : datetime(2022,8,29,7,0,0)
                }
    year = '2022'
    month = '08'
    day = '29'
    offset = 2.2 #rf15
    
elif case == '2022-08-31':
    filename_COMA = ['../Data/2022-08-31/n2o-co_2022-08-31_f0000.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220831_R2.ict'
    t0 = datetime(2022,8,31,5,7)
    t1 = datetime(2022,8,31,9,57)
    cal_starts = {'cal_1' : datetime(2022,8,31,5,35,55),
                  'cal_2' : datetime(2022,8,31,6,20,55),
                  'cal_3' : datetime(2022,8,31,7,5,40),
                  'cal_4' : datetime(2022,8,31,7,50,10),
                  'cal_5' : datetime(2022,8,31,8,35,22),
                  'cal_6' : datetime(2022,8,31,9,20,50)
                  }
    cal_ends = {'cal_1' : datetime(2022,8,31,5,37,50),
                'cal_2' : datetime(2022,8,31,6,23,0),
                'cal_3' : datetime(2022,8,31,7,7,50),
                'cal_4' : datetime(2022,8,31,7,53,18),
                'cal_5' : datetime(2022,8,31,8,38,44),
                'cal_6' : datetime(2022,8,31,9,23,38)
                }
    press_starts = {"badP_1" : datetime(2022,8,31,7,29,0),
                    "badP_2" : datetime(2022,8,31,9,21,18)
                    }
    press_ends = {"badP_1" : datetime(2022,8,31,8,16,0),
                  "badP_2" : datetime(2022,8,31,9,57,0)
                  }
    year = '2022'
    month = '08'
    day = '31'
    offset = 1.2 #rf16

elif case == '2022-09-01':
    filename_COMA = ['../Data/2022-09-01/n2o-co_2022-09-01_f0000.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220901_R2.ict'
    t0 = datetime(2022,9,1,2,52)
    t1 = datetime(2022,9,1,8,28)
    cal_starts = {'cal_1' : datetime(2022,9,1,3,20,35),
                  'cal_2' : datetime(2022,9,1,4,5,40),
                  'cal_3' : datetime(2022,9,1,4,50,15),
                  'cal_4' : datetime(2022,9,1,5,35,36),
                  'cal_5' : datetime(2022,9,1,6,20,34),
                  'cal_6' : datetime(2022,9,1,7,5,33),
                  'cal_7' : datetime(2022,9,1,7,50,40),
                  "badP_1" : datetime(2022,9,1,8,7,49)
                  }
    cal_ends = {'cal_1' : datetime(2022,9,1,3,22,40),
                'cal_2' : datetime(2022,9,1,4,7,49),
                'cal_3' : datetime(2022,9,1,4,55,4),
                'cal_4' : datetime(2022,9,1,5,38,8),
                'cal_5' : datetime(2022,9,1,6,22,59),
                'cal_6' : datetime(2022,9,1,7,8,19),
                'cal_7' : datetime(2022,9,1,7,53,20),
                "badP_1" : datetime(2022,9,1,8,28)
                }
    year = '2022'
    month = '09'
    day = '01'
    offset = 1 #rf17

elif case == '2022-09-09':
    filename_COMA = ['../Data/2022-09-09/n2o-co_2022-09-09_f0000.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220909_R2.ict'
    t0 = datetime(2022,9,9,23,40)
    t1 = datetime(2022,9,10,2,28,50)
    cal_starts = {'cal_1' : datetime(2022,9,10,0,22,50),
                  'cal_2' : datetime(2022,9,10,1,7,50),
                  'cal_3' : datetime(2022,9,10,1,52,40),
                  "badP_2" : datetime(2022,9,10,1,42,0)
                  }
    cal_ends = {'cal_1' : datetime(2022,9,10,0,25,10),
                'cal_2' : datetime(2022,9,10,1,9,55),
                'cal_3' : datetime(2022,9,10,1,55,0),
                "badP_2" : datetime(2022,9,10,2,28,50)
                }
    year = '2022'
    month = '09'
    day = '09'
    spans_multiple_days = "yes"
    offset = 6.15 #tf06

elif case == '2022-09-12':
    filename_COMA = ['../Data/2022-09-12/n2o-co_2022-09-12_f0000.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220912_R2.ict'
    t0 = datetime(2022,9,12,21,50,10)
    t1 = datetime(2022,9,13,3,19)
    cal_starts = {'cal_1' : datetime(2022,9,12,22,33,10),
                  'cal_2' : datetime(2022,9,12,23,18,10),
                  'cal_3' : datetime(2022,9,13,0,3,10),
                  'cal_4' : datetime(2022,9,13,0,48,7),
                  'cal_5' : datetime(2022,9,13,1,33,9),
                  'cal_6' : datetime(2022,9,13,2,18,7),
                  'cal_7' : datetime(2022,9,13,3,3,8)
                  }
    cal_ends = {'cal_1' : datetime(2022,9,12,22,35,10),
                'cal_2' : datetime(2022,9,12,23,20,15),
                'cal_3' : datetime(2022,9,13,0,5,16),
                'cal_4' : datetime(2022,9,13,0,50,20),
                'cal_5' : datetime(2022,9,13,1,35,20),
                'cal_6' : datetime(2022,9,13,2,20,24),
                'cal_7' : datetime(2022,9,13,3,5,12)
                }
    press_starts = {"badP_2" : datetime(2022,9,13,2,34)}
    press_ends = {"badP_2" : datetime(2022,9,13,19,9)}
    year = '2022'
    month = '09'
    day = '12'
    spans_multiple_days = "yes"
    offset = 16.65 #tf07

elif case == '2022-09-13':
    filename_COMA = ['../Data/2022-09-13/n2o-co_2022-09-13_f0000.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220913_R2.ict'
    t0 = datetime(2022,9,13,20)
    t1 = datetime(2022,9,14,1,11)
    cal_starts = {'badP_1' : datetime(2022,9,13,20,0,0),
                  'cal_1' : datetime(2022,9,13,20,19,0),
                  'cal_2' : datetime(2022,9,13,21,3,56),
                  'cal_3' : datetime(2022,9,13,21,48,54),
                  'cal_4' : datetime(2022,9,13,22,33,54),
                  'cal_5' : datetime(2022,9,13,23,18,53),
                  'cal_6' : datetime(2022,9,13,23,59,54),
                  'cal_7' : datetime(2022,9,14,0,39)
                  }
    cal_ends = {'badP_1' : datetime(2022,9,13,20,18,0),
                'cal_1' : datetime(2022,9,13,20,20,50),
                'cal_2' : datetime(2022,9,13,21,6),
                'cal_3' : datetime(2022,9,13,21,51,12),
                'cal_4' : datetime(2022,9,13,22,37),
                'cal_5' : datetime(2022,9,13,23,21),
                'cal_6' : datetime(2022,9,14,0,16),
                'cal_7' : datetime(2022,9,14,1)
                }
    year = '2022'
    month = '09'
    day = '13'
    spans_multiple_days = "yes"
    offset = 16.8 #tf08
    
elif case == '2022-09-14':
    filename_COMA = ['../Data/2022-09-14/n2o-co_2022-09-14_f0000.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220914_R2.ict'
    t0 = datetime(2022,9,14,16,16)
    t1 = datetime(2022,9,14,21)
    cal_starts = {'cal_1' : datetime(2022,9,14,16,48),
                  'cal_2' : datetime(2022,9,14,17,33),
                  'cal_3' : datetime(2022,9,14,18,18),
                  'cal_4' : datetime(2022,9,14,19,3),
                  'cal_5' : datetime(2022,9,14,19,48),
                  'cal_6' : datetime(2022,9,14,20,33)
                  }
    cal_ends = {'cal_1' : datetime(2022,9,14,16,59,58),
                'cal_2' : datetime(2022,9,14,17,44,52),
                'cal_3' : datetime(2022,9,14,18,30,45),
                'cal_4' : datetime(2022,9,14,19,15,43),
                'cal_5' : datetime(2022,9,14,20,0,30),
                'cal_6' : datetime(2022,9,14,20,44,38)
                }
    press_starts = {"badP_1" : datetime(2022,9,14,16),
                    "badP_2" : datetime(2022,9,14,19,11)
                    }
    press_ends = {"badP_1" : datetime(2022,9,14,16,44),
                  "badP_2" : datetime(2022,9,14,21)
                  }
    year = '2022'
    month = '09'
    day = '14'
    offset = 19.4 #tf09
    
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
                    'N2O': COMA['[N2O]d_ppm'][ix_flight],
                    'MIU': COMA['MIU_VALVE'][ix_flight]})

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

#If user hasn't specified cal cycles, replace based on MIU
else:
    cal_ix = np.asarray(np.where(df['MIU'] != 8)).T
    for i in cal_ix:
        df['CO'].iloc[i] = -9.999
        df['N2O'].iloc[i] = -9.999  
    
#replace N2O  with -9.999 during flagged pressure times
if 'press_starts' in locals():
    press_starts_vals = list(press_starts.values())
    press_ends_vals = list(press_ends.values())
    for i in range(len(press_starts)):
        press_ix = np.asarray(np.where((df['Time_Start']>= press_starts_vals[i]) & (df['Time_Start']<= press_ends_vals[i]))).T
        df.loc[press_ix[0,0]:press_ix[len(press_ix)-1,0],'N2O'] = -9.999

#replace CO and N2O with -9.999 during other times with issues
if 'other_starts' in locals():
    other_starts_vals = list(other_starts.values())
    other_ends_vals = list(other_ends.values())
    for i in range(len(other_starts)):
        other_ix = np.asarray(np.where((df['Time_Start']>= other_starts_vals[i]) & (df['Time_Start']<= other_ends_vals[i]))).T
        df.loc[other_ix[0,0]:other_ix[len(other_ix)-1,0],'CO'] = -9.999
        df.loc[other_ix[0,0]:other_ix[len(other_ix)-1,0],'N2O'] = -9.999
        
#If power cycled, also fill discontinuities with -9.999
if'cycle_starts' in locals():
    cycle_starts_vals = list(cycle_starts.values())
    cycle_ends_vals = list(cycle_ends.values())
    for i in range(len(cycle_starts)):
        diff = cycle_ends_vals[i] - cycle_starts_vals[i]
        num_new_pts = round(diff / timedelta(seconds=0.995)) #round to nearest integer
        for k in range(num_new_pts):
            #get a new row with the "fake" timestamp
            newrow = pd.DataFrame([cycle_starts_vals[i] + (k+1)*timedelta(seconds=0.995),
                                  cycle_starts_vals[i] + timedelta(seconds=0.4975) + (k+1)*timedelta(seconds=0.995),
                                  cycle_starts_vals[i] + timedelta(seconds = 0.994) + (k+1)*timedelta(seconds=0.995),
                                  -9.999,-9.999,9]).T
            newrow.columns =['Time_Start', 'Time_Mid', 'Time_End', 'CO', 'N2O', 'MIU']
            #add this data to our main dataframe
            df = pd.concat([df,newrow])
    
    #Fix endcap timestamps
    np.where(df['Time_Start'] == pd.to_datetime(cycle_starts_vals[i]),pd.to_datetime(cycle_starts_vals[i]) + timedelta(seconds=0.995), df['Time_End'])
    np.where(df['Time_Start'] == pd.to_datetime(cycle_starts_vals[i]),pd.to_datetime(cycle_starts_vals[i]) + timedelta(seconds=0.4975), df['Time_Mid'])
    
    #make sure our datetimes are all in ascending order        
    df = df.sort_values(by='Time_Start')  

    #reset the index to get rid of 0's where we added times in
    df = df.reset_index(drop=True)
    
#now account for the time offset
if 'offset' in locals():
    df['Time_Start'] = df['Time_Start'] - pd.Timedelta(seconds=offset)
    df['Time_Mid'] = df['Time_Mid'] - pd.Timedelta(seconds=offset)
    df['Time_End'] = df['Time_End'] - pd.Timedelta(seconds=offset)    
    
#now get ready to apply the calibration coeffiecients (oct 2024 addition)

#get the datetimes ready
#get the starting reference datetime (July 16, 2022, 00:00:00)
ref_datetime = datetime(2022, 7, 16, 0, 0, 0)
#Calculate the time difference
time_difference = df['Time_Start'] - ref_datetime
# Convert the time difference to days (including fractional part)
df['datenum'] = time_difference.dt.days + time_difference.dt.seconds / (24 * 3600)

#now do the actual correction for each pollutant
for n in range(len(pollutants)):
    #get ready for linear regression
    X = df[['{}'.format(pollutants[n]), 'datenum']]
    #rename to match what we previously used
    X.columns.values[0] = 'measured'
    #get the path of the previously fitted model
    modelPath = 'C:\\Users\\okorn\\Documents\\COMA_calibrations\\{}_multivariate_model.joblib'.format(pollutants[n])
    #load in the previously fitted model
    model = joblib.load(modelPath)
    #apply the previously fitted model
    df['{}'.format(pollutants[n])] = model.predict(X)


#delete out any timestamps where Time_end is larger than the subsequent Time_start
#for index, row in df.iterrows():
    #np.where(df['Time_End'].iloc[index] > df['Time_Start'].iloc[index+1],df.drop(index),df.iloc[index])       
 
# %% output data
    
# convert timestamp to seconds after midnight
start_time_midnight = [(t.hour * 3600) + (t.minute * 60) + t.second + (t.microsecond / 1000000.0) for t in df['Time_Start']]
mid_time_midnight = [(t.hour * 3600) + (t.minute * 60) + t.second + (t.microsecond / 1000000.0) for t in df["Time_Mid"]]
end_time_midnight = [(t.hour * 3600) + (t.minute * 60) + t.second + (t.microsecond / 1000000.0) for t in df["Time_End"]]
            
#save out a version with normal datetime stamps for easier plotting
df.to_excel('{}_cleaned_R2.xls'.format(case))

# create final DataFrame with desired variables
#convert CO and N2O to ppbv here as well
df = pd.DataFrame({'Time_Start': start_time_midnight,
                   'Time_End': end_time_midnight,
                   'Time_Mid': mid_time_midnight,
                    'CO': df['CO'] * 1000,
                    'N2O': df['N2O'] * 1000})

#if our data spans multiple days, convert it to one very long day
if 'spans_multiple_days' in locals():
    #find the index where the switch starts & get it alone as a #
    c_row = np.array(np.where(df["Time_Start"] > df["Time_End"]))[0,0]
    #correct the time end
    df.iloc[c_row,1] = df.iloc[c_row,1] + df.iloc[c_row-1,1]
    #Set the Time_End to 1 millisecond before the next Time_Start
    df.iloc[c_row,1] = df.iloc[c_row,0] + df.iloc[c_row+1,0] - 0.001
    #recalculate the time mid
    df.iloc[c_row,2] = (df.iloc[c_row,0] + df.iloc[c_row,1]) / 2
            
    #now fix the remaining rows
    for kk in range(c_row+1,len(df)):
        #correct the time start
        df.iloc[kk,0] = df.iloc[kk,0] + df.iloc[c_row,0]
    for jj in range(c_row+1,len(df)-1):
        #Set the Time_End to 1 millisecond before the next Time_Start
        df.iloc[jj,1] = df.iloc[jj+1,0] - 0.001
        #recalculate the time mid
        df.iloc[jj,2] = (df.iloc[jj,0] + df.iloc[jj,1]) / 2
    
    #delete the last row
    df = df[:-1]
                
# loop that saves string formatted (commas, decimal places) data
# create new file; overwrites if needed
with open(output_name,"w") as ofile:
     fmt = '%.1f, %.1f, %.1f, %6.2f, %6.2f'
     np.savetxt(ofile, df.values, fmt=fmt)

#create file header
# refer to ICARTT 2.0 specifications for more details
header = '38,1001,V02_2016\n' # number of lines in header, file format index
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
header += 'Time_Stop, seconds, elapsed time from 0000 UTC\n' # dependent variable short name, units, standard name
header += 'Time_Mid, seconds, elapsed time from 0000 UTC\n' # dependent variable short name, units, standard name
header += 'CO, ppbv, Gas_CO_InSitu_S_DVMR\n' # dependent variable short name, units, standard name
header += 'N2O, ppbv, Gas_N2O_InSitu_S_DVMR\n' # (repeat as necessary)
header += '0\n' # number of special comment lines (not including this line)
header += '20\n' # number of normal comment lines (not including this line)
header += 'PI_CONTACT_INFO: James.R.Podolske@nasa.gov\n'
header += 'PLATFORM: NASA WB-57F 926\n'
header += 'LOCATION: Latitude, Longitude, and Altitude included in MMS files\n'
header += 'ASSOCIATED_DATA: N/A\n'
header += 'INSTRUMENT_INFO: In-situ gas-phase CO/N2O Analyzer (LGR/ABB Serial no. 15-0251). Mounted in pallet 3.\n'
header += 'DATA_INFO: Measurements before and during takeoff, after landing, during periodic calibration cycles, and a 10 second buffer on either side of calibration cycles have been omitted. Additionally, when the measurement cell pressure deviated from the rolling median pressure for that flight by more than 0.25%, N2O data were always removed, and CO data were removed on a case-by-case basis. Time delay has been accounted for by matching signals to that of COLD2 using the median lag for each individual flight. Calibration to NOAA standards has been applied (# CC745344, #CC746190) using N2O_X2006A and WMO CO_X2014A scales.\n'
header += 'UNCERTAINTY:  Total uncertainty is determined by the square root of the sum of the squares of accuracy and precision terms. At 320 ppb N2O, total uncertainty is 2.7 ppb. At 50 ppb CO, total uncertainty is 4.1 ppb; at 200 ppb, CO total uncertainty is 5.6 ppb. If desired, total uncertainty for each measurement can be calculated from individual terms. N2O precision = 8.05E-03*N2O(ppb) – 0.247 ; CO precision = 1.79E-02*CO(ppb) + 0.500. Overall accuracy = 3.8 ppb CO. Overall accuracy in N2O is determined equally by residuals (1.0 ppb) and NOAA scale uncertainty (0.31% N2O). For additional detail, please contact the COMA team.\n'
header += 'ULOD_FLAG: -7777\n'
header += 'ULOD_VALUE: N/A\n'
header += 'LLOD_FLAG: -8888\n'
header += 'LLOD_VALUE: N/A\n'
header += 'DM_CONTACT_INFO: Laura Iraci (Laura.T.Iraci@nasa.gov)\n'
header += 'PROJECT_INFO: NASA Ames Trace Gas Data (2022 ACCLIP) https://espo.nasa.gov/acclip/\n'
header += 'STIPULATIONS_ON_USE: This data is subject to further review. Users must consult the PI and/or DM prior to use. As a matter of professional courtesy, consideration for co-authorship is expected for publications utilizing this data.\n'
header += 'OTHER_COMMENTS: N/A\n'
header += 'REVISION: R2\n'
header += 'R2: Final data; calibration applied to both N2O and CO reported values. Uncertainty estimates included.\n'
header += 'R1: Time lag applied, subject to calibration corrections and future analysis results.\n'
header += 'R0: Initial public release.\n'
header += 'Time_Start,Time_Stop,Time_Mid,CO,N2O\n'

# append the defined header to the already created data file
with open(output_name, 'r+') as f:
    content = f.read()
    f.seek(0, 0)
    f.write(header + content)      

#delete variables that might mess with our next run
if 'press_starts'in locals():
    del press_starts
if 'cal_starts'in locals():
    del cal_starts
if 'other_starts'in locals():
    del other_starts
if 'cycle_starts'in locals():
    del cycle_starts
if 'spans_multiple_days' in locals():
    del spans_multiple_days
if 'offset' in locals():
    del offset
