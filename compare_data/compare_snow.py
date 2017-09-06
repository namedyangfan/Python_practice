import pandas as pd 
import numpy as np
import os
import errno
import re
from .convert_tecplot import hgs_loadfile

def compare_snow(obs_file_directory, obs_file_name, simu_file_directory, simu_file_name, station_name, obs_col= ['Date','SWE.m.'], ldebug=False):
    '''
    merge the observed the simulated data based on Date
    there are many stations in the simulated data file, only the one which contain the same name as the observed station is selected
    
    Parameter
    ------------
    obs_file: dataframe
        this file should have less time stamps than the obserced
    simu_file: dataframe
        this file may contain 'Date' and multiple columns for other stations
    station_name: string
        station_name is used to select the stations in the simu_file which match with the obs_file
    '''
    obs_file_path = os.path.join(obs_file_directory,obs_file_name)
    if not os.path.exists(obs_file_path):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), obs_file_path)
    simu_file_path = os.path.join(simu_file_directory,simu_file_name)
    if not os.path.exists(simu_file_path):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), simu_file_path)

    df_obs = hgs_loadfile.read_csv(obs_file_directory,obs_file_name, to_exceldate=True, Date_col= 'Date')
    if ldebug: print(df_obs[obs_col].tail(10))

    df_simu = hgs_loadfile.read_tecplot(simu_file_directory,simu_file_name, sep=',')
    simu_station_name = list(filter(lambda x: x in station_name or station_name in x, df_simu.columns))
    simu_col_name = ['Date'] + simu_station_name
    if ldebug:print (df_simu[simu_col_name].tail(5))

    match_df = hgs_loadfile.colum_match(left=df_simu[simu_col_name],
                                right=df_obs[obs_col], 
                                left_on ='Date', 
                                right_on='Date')
    if ldebug: print(match_df.tail(3))

    return(match_df)

def id_dict(summary_file_directory,summary_file_name):
    '''
    create a dictionary with key: stationID.csv value: station name
    Assume the first column is the stationID and the third column is the station name
    '''
    id_name = hgs_loadfile.read_csv(summary_file_directory,summary_file_name)
    id_name.iloc[:,0]=id_name.iloc[:,0]+'.csv'
    di =dict(zip(id_name.iloc[:,0],id_name.iloc[:,2]))
    return(di)