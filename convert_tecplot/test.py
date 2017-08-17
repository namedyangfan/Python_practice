import hgs_loadfile as hl
import pandas as pd
import os	

file_directory = r"./test"
file_name = "05JG006_Daily_Flow_ts.csv"
file_path = os.path.join(file_directory,file_name)

#example 1
#read in the file and convert the Date to excel time
df = hl.read_csv(file_directory, file_name, to_exceldate= True, Date_col= 'Date', format='%Y/%m/%d')
print (df.head(10))

#example 2
#open file in pandas, then convert a specific column to excel time
df2 = pd.read_csv(file_path)
print (df2.head(10))
df2['Date'] = hl.time_to_numeric(df2['Date'], format='%Y/%m/%d')
print (df2.head(10))

#example 3
#open a tecplot file and read as pandas frame 
file_name = "Riceton.dat"
df_tecplot = hl.read_tecplot(file_directory=file_directory, file_name=file_name, sep='\s', ldebug=False)
print(df_tecplot.shape)
print(df_tecplot.head(10))
