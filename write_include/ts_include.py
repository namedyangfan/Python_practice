import os, glob, shutil
from convert_tecplot import hgs_loadfile as hl
import pandas as pd
import numpy as np 

class Write_asc_include():
    def __init__(self, grok_directory, inc_folder, o_folder, o_name):
        ''' build include file for PET and PCP'''
        self.grok_directory = grok_directory
        self.inc_path = os.path.join(grok_directory,inc_folder)
        self.o_directory = os.path.join(grok_directory,o_folder)
        self.o_path = os.path.join(self.o_directory,o_name)

        if not os.path.exists(self.inc_path):
            print("File not found: {0}".format(self.inc_path))
            return None
        if not os.path.exists(self.o_directory):
            print("File not found: {0}".format(self.o_directory))
            return None

    def ls_inc(self):
        ''' list the files names in the inc_folder and return a relative path  '''
        filename = glob.glob(self.inc_path + "\*")
        self.rel_path_inc = list(map(lambda x: os.path.relpath(x, self.grok_directory),filename))

    def write_include(self, rel_path_inc, dt= 86400):
        ''' write out the include file 
            wirting format "time filepath"
            rel_path_inc: a list of relative path
        '''
        with open(self.o_path, 'w') as fhandl:
            for i,path in enumerate(rel_path_inc):
                fhandl.write('{0}\t{1}\n'.format(i*dt,path))

class Write_ts_include():
    def __init__(self, inc_directory, inc_name, o_directory, o_name, Date_col='Date', value_col='Flow',format='%Y/%m/%d'):
        ''' build include file for lake inflow
            Date_col: column name that indicates the date
            value_col: column that is going to be used as flow rate
        '''
        self.inc_directory = inc_directory
        self.inc_path = glob.glob(os.path.join(inc_directory,"*" + inc_name + "*"))[0]
        if not os.path.exists(self.inc_path):
            print("File not found: {0}".format(self.inc_path))
            return None
        self.o_path = os.path.join(o_directory,o_name)
        self.df = hl.read_csv(file_directory=inc_directory, file_name=inc_name, to_exceldate= False, Date_col= Date_col, format=format)
        self.Date_col = Date_col
        self.value_col = value_col
        self.format = format

    def slice_df(self,a,b):
        ''' slice starting from a to b
            convert date to second starting from zero
            a is considered as the starting point, nomatter whether it exist in the data
        '''
        # take the Date and value columns
        df_slice = self.df[[self.Date_col,self.value_col]]
        # convert Date column to np.datatime64
        df_slice[self.Date_col] = pd.to_datetime(df_slice[self.Date_col], format=self.format)
        df_slice = df_slice[(df_slice[self.Date_col] >= a) & (df_slice[self.Date_col] <= b)]
        #prepare start_date column for calcualting dt
        df_slice['start_date'] = a
        df_slice['start_date'] = pd.to_datetime(df_slice['start_date'], format=self.format)
        #calculate dt in second
        df_slice[self.Date_col] = (df_slice[self.Date_col] - df_slice['start_date']).dt.total_seconds()
        df_slice[self.Date_col] = df_slice[self.Date_col].apply(int)
        self.df_slice = df_slice.drop('start_date', axis=1)
        
        # a = hl.time_to_numeric(a)
        # b = hl.time_to_numeric(b)
        # # slicing the columns
        # df_slice = self.df[[self.Date_col,self.value_col]]
        # # convert dtype to float
        # df_slice[self.Date_col].apply(float)
        # # selecting range from a to b
        # df_slice = df_slice[(df_slice[self.Date_col]>=a) & (df_slice[self.Date_col]<=b)]
        # df_slice[self.Date_col] = (df_slice[self.Date_col] - df_slice[self.Date_col].iloc[0]) * unit
        # print(df_slice)

    def write_include(self):
        '''
            write out the sliced data 
        '''
        ## float_format solves the problem that to_csv generate too much sigfig
        self.df_slice.to_csv(self.o_path, sep=" ", header=False, index=False, float_format='%.4f')


