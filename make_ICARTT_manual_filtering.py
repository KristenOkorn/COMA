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
r_month = '10'
r_day = '18'

# select file to export
case = '2022-09-14'

if case == '2022-07-16':
    filename_COMA = ['../Data/2022-07-16/n2o-co_2022-07-16_f0002.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220716_RA.ict'
    t0 = datetime(2022,7,16,14,46)
    t1 = datetime(2022,7,16,15,40)
    year = '2022'
    month = '07'
    day = '16'
    
if case == '2022-07-18':
    filename_COMA = ['../Data/2022-07-18/n2o-co_2022-07-18_f0002.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220718_RA.ict'
    t0 = datetime(2022,7,18,15,27)
    t1 = datetime(2022,7,18,21,34)
    year = '2022'
    month = '07'
    day = '18'
    
elif case == '2022-07-21-1':
    filename_COMA = ['../Data/2022-07-21-1/n2o-co_2022-07-21_1_f0001.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220721_RA_1.ict'
    t0 = datetime(2022,7,21,13,30)
    t1 = datetime(2022,7,21,18,25)
    press_starts = {"badP_1" : datetime(2022,7,21,15,42,10)}
    press_ends = {"badP_1" : datetime(2022,7,21,15,44,22)}
    year = '2022'
    month = '07'
    day = '21'
    
elif case == '2022-07-21-2':
    filename_COMA = ['../Data/2022-07-21-2/n2o-co_2022-07-21_f0002.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220721_RA_2.ict'
    t0 = datetime(2022,7,21,20,24)
    t1 = datetime(2022,7,22,0,22)
    press_starts = {"badP_1" : datetime(2022,7,21,20,24,9)}
    press_ends = {"badP_1" : datetime(2022,7,21,20,24,24)}
    year = '2022'
    month = '07'
    day = '21'
    spans_multiple_days = 'yes'
    
elif case == '2022-07-24':
    filename_COMA = ['../Data/2022-07-24/n2o-co_2022-07-24_f0000.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220724_RA.ict'
    t0 = datetime(2022,7,24,21,31)
    t1 = datetime(2022,7,25,0,57)
    press_starts = {"badP_1" : datetime(2022,7,24,21,31,27)}
    press_ends = {"badP_1" : datetime(2022,7,24,21,31,42)}
    year = '2022'
    month = '07'
    day = '24'
    spans_multiple_days = 'yes'

elif case == '2022-07-25':
    filename_COMA = ['../Data/2022-07-25/n2o-co_2022-07-25_f0000.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220725_RA.ict'
    t0 = datetime(2022,7,25,22,36)
    t1 = datetime(2022,7,26,4,28)
    press_starts = {"badP_1" : datetime(2022,7,25,22,36,51)}
    press_ends = {"badP_1" : datetime(2022,7,25,22,37,15)}
    year = '2022'
    month = '07'
    day = '25'
    spans_multiple_days = 'yes'
    
elif case == '2022-07-27':
    filename_COMA = ['../Data/2022-07-27/n2o-co_2022-07-27_f0000.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220727_RA.ict'
    t0 = datetime(2022,7,27,0,50)
    t1 = datetime(2022,7,27,3,51)
    press_starts = {"badP_1" : datetime(2022,7,27,0,50,50),
                    'badP_2' : datetime(2022,7,27,3,3,37),
                    "badP_3" : datetime(2022,7,27,3,26,53)
                    }
    press_ends = {"badP_1" : datetime(2022,7,27,1,10,23),
                  "badP_2" : datetime(2022,7,27,3,5,56),
                  "badP_3" : datetime(2022,7,27,3,49,48)
                  }
    year = '2022'
    month = '07'
    day = '27'
    
elif case == '2022-08-02':
    filename_COMA = ['../Data/2022-08-02/n2o-co_2022-08-02_f0000.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220802_RA.ict'
    t0 = datetime(2022,8,2,1,15)
    t1 = datetime(2022,8,2,6,33)
    year = '2022'
    month = '08'
    day = '02'
elif case == '2022-08-04':
    filename_COMA = ['../Data/2022-08-04/n2o-co_2022-08-04_f0000.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220804_RA.ict'
    t0 = datetime(2022,8,4,1,30)
    t1 = datetime(2022,8,4,6,18)
    #Note: removed a few stray points by hand. Refer to README.txt
    year = '2022'
    month = '08'
    day = '04'
elif case == '2022-08-06':
    filename_COMA = ['../Data/2022-08-06/n2o-co_2022-08-06_f0000.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220806_RA.ict'
    t0 = datetime(2022,8,6,1,00)
    t1 = datetime(2022,8,6,7,9)
    cal_starts = {'cal_1' : datetime(2022,8,6,1,29,10),
                  'cal_2' : datetime(2022,8,6,2,15,10),
                  'cal_3' : datetime(2022,8,6,3,1,10),
                  'cal_4' : datetime(2022,8,6,3,47,10),
                  'cal_5' : datetime(2022,8,6,4,33,10),
                  'cal_6' : datetime(2022,8,6,5,18,50),
                  'cal_7' : datetime(2022,8,6,6,5,10),
                  'cal_8' : datetime(2022,8,6,6,51,10)
                  }
    cal_ends = {'cal_1' : datetime(2022,8,6,1,32,0),
                'cal_2' : datetime(2022,8,6,2,18,0),
                'cal_3' : datetime(2022,8,6,3,3,41),
                'cal_4' : datetime(2022,8,6,3,50,15),
                'cal_5' : datetime(2022,8,6,4,36,55),
                'cal_6' : datetime(2022,8,6,5,22,15),
                'cal_7' : datetime(2022,8,6,6,8,15),
                'cal_8' : datetime(2022,8,6,6,55,10)
                }
    press_starts = {"badP_1" : datetime(2022,8,6,6,21,27)}
    press_ends = {"badP_1" : datetime(2022,8,6,6,55,12)}
    year = '2022'
    month = '08'
    day = '06'
    
elif case == '2022-08-12':
    filename_COMA = ['../Data/2022-08-12/n2o-co_2022-08-12_f0000.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220812_RA.ict'
    t0 = datetime(2022,8,12,2,21)
    t1 = datetime(2022,8,12,8,0)
    year = '2022'
    month = '08'
    day = '12'
elif case == '2022-08-13':
    filename_COMA = ['../Data/2022-08-13/n2o-co_2022-08-13_f0000.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220813_RA.ict'
    t0 = datetime(2022,8,13,1,8)
    t1 = datetime(2022,8,13,6,3)
    press_starts = {"badP_1" : datetime(2022,8,13,3,40,49),
                    "badP_2" : datetime(2022,8,13,5,11,50)
                    }
    press_ends = {"badP_1" : datetime(2022,8,13,3,51,59),
                  "badP_2" : datetime(2022,8,13,6,3,0)
                  }
    year = '2022'
    month = '08'
    day = '13'
elif case == '2022-08-15':
    filename_COMA = ['../Data/2022-08-15/n2o-co_2022-08-15_combined.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220815_RA.ict'
    t0 = datetime(2022,8,15,3,29)
    t1 = datetime(2022,8,15,8,9)
    #also have to flag data from power cycle
    cycle_starts = {'cycle_1' : datetime(2022,8,15,4,51,22)} #only times when data doesn't exist
    cycle_ends = {'cycle_1' : datetime(2022,8,15,5,4,39)}
    press_starts = {"badP_1" : datetime(2022,8,15,6,27,30)}
    press_ends = {"badP_1" : datetime(2022,8,15,6,50,30)}
    other_starts = {'other_1' : datetime(2022,8,15,4,44,40),
                    'other_2' : datetime(2022,8,15,4,39)
                    } #other times to cut out (i.e. instrument warmup after power cycle)
    other_ends = {'other_1' : datetime(2022,8,15,4,51,22),
                  'other_2' : datetime(2022,8,15,4,40)
                  } #will remove both CO & N2O
    year = '2022'
    month = '08'
    day = '15'
elif case == '2022-08-16':
    filename_COMA = ['../Data/2022-08-16/n2o-co_2022-08-16_f0000.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220816_RA.ict'
    t0 = datetime(2022,8,16,3,5)
    t1 = datetime(2022,8,16,8,17)
    cal_starts = {'cal_1' : datetime(2022,8,16,3,29,13),
                  'cal_2' : datetime(2022,8,16,4,14,13),
                  'cal_3' : datetime(2022,8,16,4,59,13),
                  'cal_4' : datetime(2022,8,16,5,44,13),
                  'cal_5' : datetime(2022,8,16,6,29,13),
                  'cal_6' : datetime(2022,8,16,7,14,13),
                  'cal_7' : datetime(2022,8,16,7,59,13)
                  }
    cal_ends = {'cal_1' : datetime(2022,8,16,3,30,45),
                'cal_2' : datetime(2022,8,16,4,15,40),
                'cal_3' : datetime(2022,8,16,5,0,45),
                'cal_4' : datetime(2022,8,16,5,45,56),
                'cal_5' : datetime(2022,8,16,6,31,9),
                'cal_6' : datetime(2022,8,16,7,16,5),
                'cal_7' : datetime(2022,8,16,8,0,53)
                }
    press_starts = {"badP_1" : datetime(2022,8,16,7,51,18)}
    press_ends = {"badP_1" : datetime(2022,8,16,8,17,0)}
    year = '2022'
    month = '08'
    day = '16'
elif case == '2022-08-19':
    filename_COMA = ['../Data/2022-08-19/n2o-co_2022-08-19_f0000.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220819_RA.ict'
    t0 = datetime(2022,8,19,0,20)
    t1 = datetime(2022,8,19,6,15)
    cal_starts = {'cal_1' : datetime(2022,8,19,0,25,17),
                  'cal_2' : datetime(2022,8,19,1,10,17),
                  'cal_3' : datetime(2022,8,19,1,55,7),
                  'cal_4' : datetime(2022,8,19,2,40,14),
                  'cal_5' : datetime(2022,8,19,3,25,17),
                  'cal_6' : datetime(2022,8,19,4,10,17),
                  'cal_7' : datetime(2022,8,19,4,55,17),
                  'cal_8' : datetime(2022,8,19,5,40,17)
                  }
    cal_ends = {'cal_1' : datetime(2022,8,19,0,26,54),
                'cal_2' : datetime(2022,8,19,1,12,0),
                'cal_3' : datetime(2022,8,19,1,56,55),
                'cal_4' : datetime(2022,8,19,2,42,0),
                'cal_5' : datetime(2022,8,19,3,26,55),
                'cal_6' : datetime(2022,8,19,4,12,15),
                'cal_7' : datetime(2022,8,19,4,57,15),
                'cal_8' : datetime(2022,8,19,5,42,20)
                }
    press_starts = {"badP_1" : datetime(2022,8,19,5,47,0)}
    press_ends = {"badP_1" : datetime(2022,8,19,6,15,0)}
    year = '2022'
    month = '08'
    day = '19'
    
elif case == '2022-08-21':
    filename_COMA = ['../Data/2022-08-21/n2o-co_2022-08-21_f0000.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220821_RA.ict'
    t0 = datetime(2022,8,21,0,53)
    t1 = datetime(2022,8,21,6,31)
    cal_starts = {'cal_1' : datetime(2022,8,21,1,22,12),
                  'cal_2' : datetime(2022,8,21,2,7,12),
                  'cal_3' : datetime(2022,8,21,2,52,12),
                  'cal_4' : datetime(2022,8,21,3,37,12),
                  'cal_5' : datetime(2022,8,21,4,22,12),
                  'cal_6' : datetime(2022,8,21,5,7,12),
                  'cal_7' : datetime(2022,8,21,5,52,12)
                  }
    cal_ends = {'cal_1' : datetime(2022,8,21,1,23,40),
                'cal_2' : datetime(2022,8,21,2,8,40),
                'cal_3' : datetime(2022,8,21,2,53,43),
                'cal_4' : datetime(2022,8,21,3,39,15),
                'cal_5' : datetime(2022,8,21,4,23,58),
                'cal_6' : datetime(2022,8,21,5,9,0),
                'cal_7' : datetime(2022,8,21,5,54,5)
                }
    press_starts = {"badP_1" : datetime(2022,8,21,4,22,17)}
    press_ends = {"badP_1" : datetime(2022,8,21,4,29,10)}
    year = '2022'
    month = '08'
    day = '21'
    
elif case == '2022-08-23':
    filename_COMA = ['../Data/2022-08-23/n2o-co_2022-08-23_f0000.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220823_RA.ict'
    t0 = datetime(2022,8,23,1,37)
    t1 = datetime(2022,8,23,7,47)
    cal_starts = {'cal_1' : datetime(2022,8,23,2,6,40),
                  'cal_2' : datetime(2022,8,23,2,51,47),
                  'cal_3' : datetime(2022,8,23,3,36,47),
                  'cal_4' : datetime(2022,8,23,4,21,47),
                  'cal_5' : datetime(2022,8,23,5,6,47),
                  'cal_6' : datetime(2022,8,23,5,51,47),
                  'cal_7' : datetime(2022,8,23,6,36,47),
                  'cal_8' : datetime(2022,8,23,7,21,47)
                  }
    cal_ends = {'cal_1' : datetime(2022,8,23,2,8,23),
                'cal_2' : datetime(2022,8,23,2,53,23),
                'cal_3' : datetime(2022,8,23,3,38,18),
                'cal_4' : datetime(2022,8,23,4,23,32),
                'cal_5' : datetime(2022,8,23,5,8,37),
                'cal_6' : datetime(2022,8,23,5,53,40),
                'cal_7' : datetime(2022,8,23,6,38,35),
                'cal_8' : datetime(2022,8,23,7,23,25)
                }
    press_starts = {"badP_1" : datetime(2022,8,23,7,22,55)}
    press_ends = {"badP_1" : datetime(2022,8,23,7,47,0)}
    year = '2022'
    month = '08'
    day = '23'
    
elif case == '2022-08-25':
    filename_COMA = ['../Data/2022-08-25/n2o-co_2022-08-25_corrected.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220825_RA.ict'
    t0 = datetime(2022,8,25,0,55)
    t1 = datetime(2022,8,25,6,35)
    cal_starts = {'cal_1' : datetime(2022,8,25,1,22,52),
                  'cal_2' : datetime(2022,8,25,2,7,52),
                  'cal_3' : datetime(2022,8,25,2,52,52),
                  'cal_4' : datetime(2022,8,25,3,37,52),
                  'cal_5' : datetime(2022,8,25,4,22,52),
                  'cal_6' : datetime(2022,8,25,5,7,52),
                  'cal_7' : datetime(2022,8,25,5,52,52)
                  }
    cal_ends = {'cal_1' : datetime(2022,8,25,1,24,20),
                'cal_2' : datetime(2022,8,25,2,9,25),
                'cal_3' : datetime(2022,8,25,2,54,28),
                'cal_4' : datetime(2022,8,25,3,39,35),
                'cal_5' : datetime(2022,8,25,4,25,2),
                'cal_6' : datetime(2022,8,25,5,9,52),
                'cal_7' : datetime(2022,8,25,5,54,48)
                }
    year = '2022'
    month = '08'
    day = '25'
    
elif case == '2022-08-26':
    filename_COMA = ['../Data/2022-08-26/n2o-co_2022-08-26_f0000.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220826_RA.ict'
    t0 = datetime(2022,8,26,0,55)
    t1 = datetime(2022,8,26,6,55)
    cal_starts = {'cal_1' : datetime(2022,8,26,1,25,48),
                  'cal_2' : datetime(2022,8,26,2,10,48),
                  'cal_3' : datetime(2022,8,26,2,55,48),
                  'cal_4' : datetime(2022,8,26,3,40,48),
                  'cal_5' : datetime(2022,8,26,4,25,48),
                  'cal_6' : datetime(2022,8,26,5,10,48),
                  'cal_7' : datetime(2022,8,26,5,55,48),
                  'cal_8' : datetime(2022,8,26,6,40,48)
                  }
    cal_ends = {'cal_1' : datetime(2022,8,26,1,27,33),
                'cal_2' : datetime(2022,8,26,2,12,26),
                'cal_3' : datetime(2022,8,26,2,57,24),
                'cal_4' : datetime(2022,8,26,3,42,30),
                'cal_5' : datetime(2022,8,26,4,27,36),
                'cal_6' : datetime(2022,8,26,5,12,40),
                'cal_7' : datetime(2022,8,26,5,57,52),
                'cal_8' : datetime(2022,8,26,6,42,22),
                }
    press_starts = {"badP_1" : datetime(2022,8,26,5,55,45)}
    press_ends = {"badP_1" : datetime(2022,8,26,5,57,15)}
    year = '2022'
    month = '08'
    day = '26'
    
elif case == '2022-08-29':
    filename_COMA = ['../Data/2022-08-29/n2o-co_2022-08-29_f0000.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220829_RA.ict'
    t0 = datetime(2022,8,29,0,56)
    t1 = datetime(2022,8,29,7,0)
    cal_starts = {'cal_1' : datetime(2022,8,29,1,25,46),
                  'cal_2' : datetime(2022,8,29,2,10,46),
                  'cal_3' : datetime(2022,8,29,2,55,46),
                  'cal_4' : datetime(2022,8,29,3,40,46),
                  'cal_5' : datetime(2022,8,29,4,25,46),
                  'cal_6' : datetime(2022,8,29,5,10,46),
                  'cal_7' : datetime(2022,8,29,5,55,46),
                  'cal_8' : datetime(2022,8,29,6,40,46)
                  }
    cal_ends = {'cal_1' : datetime(2022,8,29,1,27,27),
                'cal_2' : datetime(2022,8,29,2,12,18),
                'cal_3' : datetime(2022,8,29,2,57,23),
                'cal_4' : datetime(2022,8,29,3,42,35),
                'cal_5' : datetime(2022,8,29,4,27,46),
                'cal_6' : datetime(2022,8,29,5,12,40),
                'cal_7' : datetime(2022,8,29,5,57,45),
                'cal_8' : datetime(2022,8,29,6,42,20),
                }
    press_starts = {"badP_1" : datetime(2022,8,29,6,33,45)}
    press_ends = {"badP_1" : datetime(2022,8,29,7,0,0)}
    year = '2022'
    month = '08'
    day = '29'
    
elif case == '2022-08-31':
    filename_COMA = ['../Data/2022-08-31/n2o-co_2022-08-31_f0000.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220831_RA.ict'
    t0 = datetime(2022,8,31,5,7)
    t1 = datetime(2022,8,31,9,57)
    cal_starts = {'cal_1' : datetime(2022,8,31,5,36,3),
                  'cal_2' : datetime(2022,8,31,6,21,3),
                  'cal_3' : datetime(2022,8,31,7,5,49),
                  'cal_4' : datetime(2022,8,31,7,50,20),
                  'cal_5' : datetime(2022,8,31,8,35,32),
                  'cal_6' : datetime(2022,8,31,9,21,0)
                  }
    cal_ends = {'cal_1' : datetime(2022,8,31,5,37,39),
                'cal_2' : datetime(2022,8,31,6,22,48),
                'cal_3' : datetime(2022,8,31,7,7,40),
                'cal_4' : datetime(2022,8,31,7,53,8),
                'cal_5' : datetime(2022,8,31,8,38,34),
                'cal_6' : datetime(2022,8,31,9,23,28)
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

elif case == '2022-09-01':
    filename_COMA = ['../Data/2022-09-01/n2o-co_2022-09-01_f0000.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220901_RA.ict'
    t0 = datetime(2022,9,1,2,48)
    t1 = datetime(2022,9,1,8,28)
    cal_starts = {'cal_1' : datetime(2022,9,1,3,20,41),
                  'cal_2' : datetime(2022,9,1,4,5,48),
                  'cal_3' : datetime(2022,9,1,4,50,25),
                  'cal_4' : datetime(2022,9,1,5,35,46),
                  'cal_5' : datetime(2022,9,1,6,20,44),
                  'cal_6' : datetime(2022,9,1,7,5,43),
                  'cal_7' : datetime(2022,9,1,7,50,49)
                  }
    cal_ends = {'cal_1' : datetime(2022,9,1,3,22,30),
                'cal_2' : datetime(2022,9,1,4,7,39),
                'cal_3' : datetime(2022,9,1,4,54,54),
                'cal_4' : datetime(2022,9,1,5,37,58),
                'cal_5' : datetime(2022,9,1,6,22,49),
                'cal_6' : datetime(2022,9,1,7,8,9),
                'cal_7' : datetime(2022,9,1,7,53,10)
                }
    press_starts = {"badP_1" : datetime(2022,9,1,8,7,49)}
    press_ends = {"badP_1" : datetime(2022,9,1,8,28)}
    year = '2022'
    month = '09'
    day = '01'

elif case == '2022-09-09':
    filename_COMA = ['../Data/2022-09-09/n2o-co_2022-09-09_f0000.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220909_RA.ict'
    t0 = datetime(2022,9,9,23,39)
    t1 = datetime(2022,9,10,2,28,50)
    cal_starts = {'cal_1' : datetime(2022,9,10,0,23,0),
                  'cal_2' : datetime(2022,9,10,1,8,0),
                  'cal_3' : datetime(2022,9,10,1,52,50)
                  }
    cal_ends = {'cal_1' : datetime(2022,9,10,0,25,0),
                'cal_2' : datetime(2022,9,10,1,9,45),
                'cal_3' : datetime(2022,9,10,1,54,50)
                }
    press_starts = {"badP_1" : datetime(2022,9,9,23,39,28),
                    "badP_2" : datetime(2022,9,10,1,42,0)}
    press_ends = {"badP_1" : datetime(2022,9,9,23,40,0),
                  "badP_2" : datetime(2022,9,10,2,28,50)
                  }
    other_starts = {"other_1" : datetime(2022,9,9,23,39,28)}
    other_ends = {"other_1" : datetime(2022,9,9,23,40,0)}
    year = '2022'
    month = '09'
    day = '09'
    spans_multiple_days = "yes"

elif case == '2022-09-12':
    filename_COMA = ['../Data/2022-09-12/n2o-co_2022-09-12_f0000.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220912_RA.ict'
    t0 = datetime(2022,9,12,21,50)
    t1 = datetime(2022,9,13,3,19)
    cal_starts = {'cal_1' : datetime(2022,9,12,22,33,20),
                  'cal_2' : datetime(2022,9,12,23,18,20),
                  'cal_3' : datetime(2022,9,13,0,3,20),
                  'cal_4' : datetime(2022,9,13,0,48,17),
                  'cal_5' : datetime(2022,9,13,1,33,19),
                  'cal_6' : datetime(2022,9,13,2,18,17),
                  'cal_7' : datetime(2022,9,13,3,3,18)
                  }
    cal_ends = {'cal_1' : datetime(2022,9,12,22,35,0),
                'cal_2' : datetime(2022,9,12,23,20,5),
                'cal_3' : datetime(2022,9,13,0,5,6),
                'cal_4' : datetime(2022,9,13,0,50,10),
                'cal_5' : datetime(2022,9,13,1,35,10),
                'cal_6' : datetime(2022,9,13,2,20,14),
                'cal_7' : datetime(2022,9,13,3,5,2)
                }
    year = '2022'
    month = '09'
    day = '12'
    spans_multiple_days = "yes"

elif case == '2022-09-13':
    filename_COMA = ['../Data/2022-09-13/n2o-co_2022-09-13_f0000.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220913_RA.ict'
    t0 = datetime(2022,9,13,19,36)
    t1 = datetime(2022,9,14,1,11)
    cal_starts = {'cal_1' : datetime(2022,9,13,20,19,3),
                  'cal_2' : datetime(2022,9,13,21,4,6),
                  'cal_3' : datetime(2022,9,13,21,49,4),
                  'cal_4' : datetime(2022,9,13,22,34,4),
                  'cal_5' : datetime(2022,9,13,23,19,3),
                  'cal_6' : datetime(2022,9,14,0,4),
                  'cal_7' : datetime(2022,9,14,0,49)
                  }
    cal_ends = {'cal_1' : datetime(2022,9,13,20,20,50),
                'cal_2' : datetime(2022,9,13,21,5,49),
                'cal_3' : datetime(2022,9,13,21,51,2),
                'cal_4' : datetime(2022,9,13,22,35,59),
                'cal_5' : datetime(2022,9,13,23,20,50),
                'cal_6' : datetime(2022,9,14,0,6),
                'cal_7' : datetime(2022,9,14,0,51)
                }
    press_starts = {"badP_1" : datetime(2022,9,13,19,36)}
    press_ends = {"badP_1" : datetime(2022,9,13,20,17)}
    year = '2022'
    month = '09'
    day = '13'
    spans_multiple_days = "yes"
    
elif case == '2022-09-14':
    filename_COMA = ['../Data/2022-09-14/n2o-co_2022-09-14_f0000.txt']
    output_name = 'acclip-COMA-CON2O_WB57_20220914_RA.ict'
    t0 = datetime(2022,9,14,16,15)
    t1 = datetime(2022,9,14,21,6)
    cal_starts = {'cal_1' : datetime(2022,9,14,16,58),
                  'cal_2' : datetime(2022,9,14,17,43),
                  'cal_3' : datetime(2022,9,14,18,28),
                  'cal_4' : datetime(2022,9,14,19,13),
                  'cal_5' : datetime(2022,9,14,19,58),
                  'cal_6' : datetime(2022,9,14,20,43)
                  }
    cal_ends = {'cal_1' : datetime(2022,9,14,16,59,48),
                'cal_2' : datetime(2022,9,14,17,44,42),
                'cal_3' : datetime(2022,9,14,18,30,35),
                'cal_4' : datetime(2022,9,14,19,15,33),
                'cal_5' : datetime(2022,9,14,20,0,20),
                'cal_6' : datetime(2022,9,14,20,44,48)
                }
    press_starts = {"badP_1" : datetime(2022,9,14,16,15),
                    "badP_2" : datetime(2022,9,14,19,11)
                    }
    press_ends = {"badP_1" : datetime(2022,9,14,16,43,40),
                  "badP_2" : datetime(2022,9,14,21,6)
                  }
    year = '2022'
    month = '09'
    day = '14'
    
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

#delete out any timestamps where Time_end is larger than the subsequent Time_start
#for index, row in df.iterrows():
    #np.where(df['Time_End'].iloc[index] > df['Time_Start'].iloc[index+1],df.drop(index),df.iloc[index])       
 
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
header = '36,1001,V02_2016\n' # number of lines in header, file format index
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
header += 'CO, ppbv, CO, Gas_CO_InSitu_S_DVMR\n' # dependent variable short name, units, standard name
header += 'N2O, ppbv, N2O, Gas_N2O_InSitu_S_DVMR\n' # (repeat as necessary)
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
