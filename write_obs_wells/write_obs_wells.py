import os
import pandas as pd
import numpy as np

class write_obs_coord:
    def __init__(self,file_name,file_path,save_file_name,save_file_path,layer_num_start,layer_num_end):
        self.summary_file = os.path.join(file_path,file_name)
        self.save_file_name = os.path.join(save_file_path,save_file_name)
        self.layer_num_start = layer_num_start
        self.layer_num_end = layer_num_end

    
    def readfile(self):
        coord = pd.read_csv(self.summary_file)
        
        self.coord = (coord[['Station_Na','UTMX','UTMY']])
        
        self.coord['Station_Na'] = self.coord.Station_Na.astype('str')
        
    def write_obs(self,x):

        with open(self.save_file_name, 'a') as fhand:
            fhand.write('Make observation well from xy \n')
            fhand.write('\t' + str(x[0]).replace(" ", "") + '\n')
            fhand.write('\t {} {} \n'.format(str(x[1]), str(x[2])))
            fhand.write('\t {} {} \n\n'.format(self.layer_num_start, self.layer_num_end))
                
    def write_hgs(self):
        try:
            os.remove(self.save_file_name)
        except OSError:
            pass

        self.coord.apply(lambda x: self.write_obs(x), axis=1)