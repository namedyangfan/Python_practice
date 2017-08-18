import os
import pandas as pd 
import numpy as np



def csv_tecplot(df, save_folder, zone_name, save_name=False, ldebug=False):
    ''' convert csv to tecplot format
        df: as dataframe
        column name is used as variable  
    '''
    if not save_name:
        save_name = zone_name
    if not os.path.exists(save_folder):
        raise IOError('ERROR: directory does not exist: %s' % save_folder)

    save_path = os.path.join(save_folder, save_name)
    
    if  ldebug: print(save_path)
    
    tecplot_header = 'variables='
    for i in range(0, len(df.columns)):
        tecplot_header = '{} ,"{}"'.format(tecplot_header,df.columns[i])

    code = (tecplot_header + 
            '\n zone t= "{}" \n\n'.format(zone_name))

    with open(save_path + '.dat', 'w') as f:
        f.write( code )    
        df.to_csv(f, index = False, header = False)

