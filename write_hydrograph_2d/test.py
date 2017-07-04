from write_hydrograph_2dlist import write_hydrograph_2d

input_folder = r"./test" 
output_folder = r"./test"
output_name = "test.dat"
input_folder_rel_path = "./test"

write_hydrograph_2d(input_folder, input_folder_rel_path, output_folder, output_name, ldebug=True)