from HGS_tools.compare_data import compare_snow
import os

obs_file_directory = r"HGS_tools\compare_data\test_data"
simu_file_directory = r"HGS_tools\compare_data\test_data"
summary_file_directory = r"HGS_tools\compare_data\test_data"
output_dirc = r"HGS_tools\compare_data\test_data\output"

simu_file_name = "Snow_Stations_Output_exceldate_10km.dat"
summary_file_name = "All_Stations.csv"

di = compare_snow.id_dict(summary_file_directory,summary_file_name)
# print(di['05AA809.csv'])

for key in di:
    print(key)
    merge_df = compare_snow.compare_snow(obs_file_directory=obs_file_directory,
                obs_file_name=key,
                simu_file_directory=simu_file_directory,
                simu_file_name=simu_file_name,
                station_name=di[key],
                ldebug=True)

    ofile_name= os.path.join(output_dirc, '{}-{}.csv'.format(os.path.splitext(key)[0],di[key]))
    print(ofile_name)
    merge_df.to_csv(ofile_name,index=False)
