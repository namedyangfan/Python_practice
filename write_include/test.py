from ts_include import Write_asc_include, Write_ts_include

# example for writing asc include file
grok_directory= r"./test_data"
inc_folder = "asc"
o_folder = "asc"
o_name = "test.inc"
inc = Write_asc_include(grok_directory,inc_folder,o_folder,o_name)
inc.ls_inc()
inc.write_include(inc.rel_path_inc)

# example for writing time series include file
dir=r"./test_data/ts"
fn = "05JG006_Daily_Flow_ts.csv"
o_name = "test.inc"
inc = Write_ts_include(inc_directory=dir, inc_name=fn, o_directory=dir, o_name=o_name, Date_col ='Date')
inc.slice_df(a="2002/01/01",b="2015/12/31")
inc.write_include()

