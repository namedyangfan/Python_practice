# HGS_tools

In order to run HydroGeoSphere (HGS), one of the most important task is data preparation. It is tedious to cleaning up and formating the input data using by hands or using Excel. 
HGS_tools is a Python package for prosessing data from variouse source to a format that can be read by HGS. The library contains two major mooduls: convert_tecplot and write_include. The convert_tecplot module can either read or write data to/from Tecplot format.
The write_include module can be used to slice and format data to HGS format.

# API Reference
  
**convert_tecplot**  
* hgs_loadfile.time_to_numeric(): convert time from ISO8601 format to excel time (numeric in days since 1900)
* hgs_loadfile.read_tecplot(): read tecplot formatted data into pandas dataframe
* hgs_loadfile.read_csv(): read in csv file and convert the date column from ISO8601 to excel time on the fly  
* csv_tecplot(): write a dataframe in tecplot format

# Example
* hgs_loadfile.time_to_numeric(df['Date'], format='%Y/%m/%d')  
* hgs_loadfile.read_tecplot(file_directory=file_directory, file_name=file_name, sep='\s', ldebug=False)

# Tests
test and test data are provided in each module 
#License
MIT