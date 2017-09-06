from convert_tecplot import hgs_loadfile as hl
from convert_tecplot import csv_tecplot
import os, errno, re
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class Obs_well_hgs():

    def __init__(self, file_directory, file_name):
        ''' read in Tecplot format simulated well data
            and calcualte depth of head to ground surface for each sheet
            
            To convert the block format to column format, 'HGS_obswell_Tecplot.R' can be used
        '''
        self.file_directory = file_directory
        self.file_name = file_name

    def open_obs(self):
        file_path = os.path.join(self.file_directory, self.file_name)
        self.df = hl.read_tecplot(file_directory=self.file_directory, file_name=self.file_name, sep='\s')

    def head_to_depth(self):
        head_sheets = [x for x in self.df.columns if re.search('H', x)]
        self.num_sheet = list(head_sheets[-1])[-1]
        #get the surface elevation
        top_elev_var = 'Z' + self.num_sheet
        # print(self.df[top_elev_var])
        for sheet in head_sheets:
            depth_var = 'depth_' + sheet
            self.df[depth_var] = self.df[top_elev_var] - self.df[sheet]

    def op (self, op_folder):
        csv_tecplot(df = self.df, save_folder = op_folder, zone_name = os.path.splitext(self.file_name)[0])

class Compare_simu2obs():

    def __init__(self):
        ''' 
        plot the simulated groundwater head versus the modeled groundwater head

        Assumption:
            Observed gw data:
                1. file is in tecplot format and comma seperated
                1. variable 'date' and 'DTGS' will be used
                2. file name must include or match the filename of the modeled data
                3. 'time' is in excel format
            Modeled gw data:
                1. variable 'time' and 'depth_H[1-7]' will be used 
                2. file name must be included in the file name of 
                3. 'time' is in simulation time
        '''
        self.obs_var = ['date' ,'DTGS']
        self.obs_direct = r'.\test_data\Compare_simu2obs'
        self.obs_fn = '38973_G05MH030.dat'
        self.obs_path = os.path.join(self.obs_direct, self.obs_fn)
        self.simu_direct = r'.\test_data\Compare_simu2obs'
        self.simu_fn = 'G05MH030.dat'
        self.simu_path = os.path.join(self.simu_direct, self.simu_fn)
        self.t0 = "2002/01/01"

    def read_files(self, ldebug=False):
        self.obs_df = hl.read_tecplot(file_directory=self.obs_direct, file_name=self.obs_fn, sep=',')
        if ldebug: print(self.obs_df.head())
        self.simu_df = hl.read_tecplot(file_directory=self.simu_direct, file_name=self.simu_fn, sep=',')
        if ldebug: print(self.simu_df.head())

        ## get the H_depth variable from simulated data
        ## the simulated data contain many variables, but only the depth need to be compared
        depth_var = [x for x in self.simu_df.columns if 'depth' in x]
        try: self.simu_df = self.simu_df [['time'] + depth_var]
        except: raise ValueError('Not able to read "time" from: {}'.format(self.simu_path))
        ## changde time to date
        t0_numeric = hl.time_to_numeric(self.t0, format='%Y-%m-%d')
        self.simu_df['time'] = self.simu_df['time'] /86400 + t0_numeric
        if ldebug:
            print(self.simu_df.head())
            print(self.obs_df.head())

    def plot_depth(self, o_folder):
        ''' Plot the observed versus the simulated '''
        if not os.path.exists(o_folder):
            print("Folder not found: {0}".format(o_folder))
            return None
        o_path = os.path.join(o_folder, os.path.splitext(self.obs_fn)[0])
        ## set minimum number of lines  
        minline= 50
        ## check if there is enough data to plot
        if self.obs_df.shape[0] >= minline:
            fig = plt.figure()
            plt.plot(self.obs_df['date'], self.obs_df['DTGS'])
            plt.plot(self.simu_df['time'], self.simu_df['depth_H2'])
            plt.plot(self.simu_df['time'], self.simu_df['depth_H3'])
            plt.legend()
            plt.xlabel('Date')
            plt.ylabel('Depth')
            plt.savefig(o_path)
        else:
            print('{} has less than {} lines \n no plot is generated for this station'.format(self.obs_fn, minline))


if __name__ == "__main__":
    file_directory = r'./test_data/Obs_well_hgs'
    file_name = 'G05MD001.dat'
    test = Obs_well_hgs( file_directory = file_directory, file_name=file_name)
    test.open_obs()
    test.head_to_depth()
    test.op(op_folder= r'./test_data/Obs_well_hgs/output')
    test2 = Compare_simu2obs()
    test2.read_files()
    test2.plot_depth(o_folder=r"D:\git\HGS_tools\compare_data\test_data\Compare_simu2obs")
