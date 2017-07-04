from write_hydrograph_2dlist import write_hydrograph_2d

input_folder = r"D:\ARB\Mesh Generation_AlgoMesh Tutorial\Mesh_Steve_Jun_2017\hydrograph\AssnSubBsn" 
output_folder = r"D:\ARB\Mesh Generation_AlgoMesh Tutorial\Mesh_Steve_Jun_2017\hydrograph\hgs_command"
output_name = "AssnSubBsn.dat"
input_folder_rel_path = "./node_lists"

write_hydrograph_2d(input_folder, input_folder_rel_path, output_folder, output_name, ldebug=True)

input_folder = r"D:\ARB\Mesh Generation_AlgoMesh Tutorial\Mesh_Steve_Jun_2017\hydrograph\QuApp" 
output_folder = r"D:\ARB\Mesh Generation_AlgoMesh Tutorial\Mesh_Steve_Jun_2017\hydrograph\hgs_command"
output_name = "Qu_appelle.dat"
input_folder_rel_path = "./node_lists"

write_hydrograph_2d(input_folder, input_folder_rel_path, output_folder, output_name, ldebug=True)

input_folder = r"D:\ARB\Mesh Generation_AlgoMesh Tutorial\Mesh_Steve_Jun_2017\hydrograph\Sour" 
output_folder = r"D:\ARB\Mesh Generation_AlgoMesh Tutorial\Mesh_Steve_Jun_2017\hydrograph\hgs_command"
output_name = "Souris.dat"
input_folder_rel_path = "./node_lists"

write_hydrograph_2d(input_folder, input_folder_rel_path, output_folder, output_name, ldebug=True)