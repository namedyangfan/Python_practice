import pandas as pd 
import numpy as np
import os
import errno
import re, arrow
import warnings, glob
'''
time_to_numeric: convert time to excel numeric format
read_tecplot: read single zone multi columns tecplot file
read_csv: load csv and change time to numeric on the fly
colum_match: find the common row or merge data.frame
'''

def time_to_numeric(t, format='%Y-%m-%d %H:%M'):
    ''' convert time from ISO8601 format to numeric in days since 1900'''
    ref_date = '1900-01-01 00:00'

    try:
        a = pd.to_datetime(t, format = format) - pd.to_datetime(ref_date, format ='%Y-%m-%d %H:%M')
        a = a/np.timedelta64(1, 'D') + 2
    except:
        if not isinstance(t, pd.DataFrame):
            t = pd.DataFrame([t])
        start_date = arrow.get(ref_date, 'YYYY-MM-DD HH:mm')
        a = t.applymap(lambda x: (arrow.get(x, format = 'YYYY-MM-DD') - start_date).days + 2)
        a = a.values
    return(a)

def read_tecplot(file_directory, file_name, sep='\t', ldebug=False):
    ''' read tecplot as data frame
        sep: set equal to \s for space delimited
    '''
    file_path = os.path.join(file_directory, file_name)
        # Load column names
    if not os.path.exists(file_path):
        raise FileNotFoundError(
            errno.ENOENT, os.strerror(errno.ENOENT), file_path)
        
    with open(file_path, 'r') as handl:
        for num,line in enumerate(handl):
            if line.lower().startswith ("variable"):
                header = line.strip() [11:]
            if re.match(r"^\d+.*$",line):
                skip_num = num
                if ldebug: print('number of row to skip: {}'.format(skip_num))
                break

    if ldebug: print(header)

    # replace "" and seperate string to list of names 
    column_names = header.replace('"'," ").replace(','," ").split(' ')
    column_names = [x for x in column_names if x]
    if ldebug: print(column_names)
    # column_names = list(map(str.strip, column_names))
    try:
        df= pd.read_table (file_path, 
                header=None,
                sep= sep,
              skiprows = skip_num,
              engine='python'
              )
        if ldebug: print(df.shape)
    except:
        print('ERROR: unable to open file {}'.format(file_path))

    if not len(df.columns) == len(column_names):
        print('ERROR: number of columns in the data does not match with Tecplot header: {}'.format(column_names))

    df.columns = column_names
    return(df)

def read_csv(file_directory, file_name, to_exceldate= False, Date_col= 'Date', format='%Y-%m-%d'):
    file_path = os.path.join(file_directory, file_name)
    header= 'infer'
        # Load column names
    if not os.path.exists(file_path):
        raise FileNotFoundError(
            errno.ENOENT, os.strerror(errno.ENOENT), file_path)
        
    with open(file_path, 'r') as handl:
        line = handl.readline()
        if re.match(r"^\d+.*$",line):
            warnings.warn('File has no header. First line:' + line)
            header=None
                
    try:
        df= pd.read_csv (file_path, header=header)
    except:
        print('ERROR: unable to open file {}'.format(file_path))

    if to_exceldate:
        try:
            df[Date_col] = time_to_numeric(df[Date_col], format=format)
        except:
            print('ERROR: unable to open file {}'.format(file_path))

    return(df)


def colum_match(left, right, left_on = 'Date', right_on = 'Date'):
    '''
    find the the rows in dataframe which value match with numpy array m_value
    '''
    if not isinstance(left, pd.DataFrame):
        raise TypeError('ERROR: input df not instance of pd.DataFrame')

    if isinstance(right, (np.ndarray, np.generic, pd.core.series.Series)): 
        left = left.loc[~left[left_on].isin(right)]
        df_merge = left.reset_index(drop=True)
    elif isinstance(right, pd.DataFrame):
        df_merge = pd.merge(left=left, how='inner', right=right, left_on=left_on, right_on=right_on)
    else:
        raise TypeError('ERROR: right need to be dataframe or np.array')
    return (df_merge)



