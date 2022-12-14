# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 14:30:48 2022
@author: okorn
"""
#Import helpful toolboxes etc
import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
import seaborn as sns
import scipy.io

#Need to get the pod data in timetable, retimed format
#Load this data into excel first

#create a directory path for us to pull from / save to
path = 'C:\\Users\\okorn\\Documents\\Data\\2022-08-19\\'

    
#initialize a dataframe to add the concentrations of each to
newdata = pd.DataFrame()

#set up variables (columns) to loop through
pods = ['      [CO]d_ppm','     [N2O]d_ppm','      GasP_torr','           AIN5','            Gnd','          Peak0']

#plotting to initialize
plt.xlabel("Datetime")
#add string + variable for y axis
y = 'Methane (ppm)'
plt.ylabel(y)
#add string + variable for plot title
titl = 'Landfill Methane'
plt.title(titl)

#loop through for each location
for i in range(5):
    #get the current pod
    currentpod = pods[i]
        
    #get the filename to be loaded
    filename = "YPOD{}.xlsx".format(currentpod)
    #combine the paths with the filenames for each
    filepath = os.path.join(path, filename)
    #load in the matlab data from excel
    mat = pd.read_excel(filepath, index_col=0)  

    plt.plot(mat['CH4'], label = pods[i])
    plt.legend()

#final plotting & saving
imgname = 'CH4podtimeseries.png'
imgpath = os.path.join(path, imgname)
plt.savefig(imgpath)
plt.show()
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
You have no unread notifications