import os
import glob, warnings

def read_node(file_path, file_rel_path, output_path,ldebug):

	if os.path.exists(output_path):
		warnings.warn(' File exists {}'.format(output_path))

	for file in file_path:

		with open(file) as fin, open(output_path,'a') as fout:
			line = fin.readline()
			line = line.strip()

			#check if the first line is an integer
			try:
				int(line)
			except ValueError:
				print("\nError: '{}' is not a integer. Check file {}".format(line, file))
				return
			
			code = ('clear chosen nodes \n'
					'choose nodes top 2d-list \n'
					'\t {}/{} \n\n'.format(file_rel_path, os.path.basename(file)) + 
					'set hydrograph nodes \n'
					'\t {} \n'.format(os.path.splitext(os.path.basename(file))[0]) +
					'{:-<50} \n'.format('!')
					)

			fout.write(code)


def write_hydrograph_2d(input_folder, input_folder_rel_path, output_folder, output_name, ldebug=False):
	''' write hydrograph HGS command from .dat files in the given folder '''
	# input_folder: contains .dat files which list hydrograph 2d nodes
	# input_folder_rel_path: the relative path indicates the 2d nodes folder. This is used by grok (e.g ./hydrograph)
	# output_folder: save make hydrograph command

	if not os.path.exists(output_folder): raise IOError(output_folder)
	output_path = os.path.join( output_folder, output_name)

	stations_path = glob.glob( os.path.join(input_folder, '*.dat'))
	if len(stations_path) ==0:
		print("\nERROR: .dat file was not found in folder'{}'".format(input_folder))
		return

	if ldebug:
		print(stations_path)

	read_node(file_path=stations_path, file_rel_path=input_folder_rel_path, output_path=output_path, ldebug=ldebug)


