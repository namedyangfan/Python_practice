from convert_tecplot import hgs_loadfile as hl
from convert_tecplot import csv_tecplot
import os, errno, re

class Obs_well_hgs():

    def __init__(self, file_directory, file_name):
        ''' read in Tecplot format simulated well data
            and calcualte depth of head to ground surface
            
            To convert the block format to column format, 'HGS_obswell_Tecplot.R' can be used
        '''
        self.file_directory = file_directory
        self.file_name = file_name

    def open_obs(self):
        file_path = os.path.join(self.file_directory, self.file_name)
        self.df = hl.read_tecplot(file_directory=file_directory, file_name=file_name, sep='\s')

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


if __name__ == "__main__":
    file_directory = r'./test_data'
    file_name = 'G05MD001.dat'
    test = Obs_well_hgs( file_directory = file_directory, file_name=file_name)
    test.open_obs()
    test.head_to_depth()
    test.op(op_folder= r'./test_data/output')
    # df.to_csv("test",index=None)