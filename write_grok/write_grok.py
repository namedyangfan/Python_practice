import os, glob, shutil

class Write_grok():
    def __init__(self, grok_name, grok_directory):
        ''' modify a given grok file'''
        self.grok_directory = grok_directory
        self.grok_path = os.path.join(grok_directory,grok_name)
        if not os.path.exists(self.grok_path):
            print("File not found: {0}".format(self.grok_path))
            return None
            
        self.backup_copy = self.grok_path + '.preunsat_original'
        if not os.path.exists(self.backup_copy): 
            shutil.copy(self.grok_path, self.backup_copy)
            shutil.move(self.grok_path, self.grok_path + '.backup') 

    def search_path(self, file_name, ldebug=False):
        ''' search for file name in the grok folder''' 
        filename= glob.glob(os.path.join(self.grok_directory,'**',file_name), recursive=True)
        if not filename: raise IOError(file_name)
        if len(filename)>1: print('Warning: more than one match was found. {}'.format(filename))
        if ldebug: print (filename)
        file_rela = (os.path.relpath(filename[0], self.grok_directory))
        if ldebug: print (file_rela)
        return(file_rela)

    def add_gw_wells(self, inc_file_name, overwrite=False):
        '''add include file below the ref_line'''
        ref_line = 'Data Output'
        # get the relative path of the include file
        inc_file_path = self.search_path(inc_file_name)

        with open(self.backup_copy) as fhand, open(self.grok_path, 'w') as fcopy:
            line = fhand.readline()
            while line:
                if ref_line in line:
                    # locate where command line need to be inserted
                    output_flag=True
                    while output_flag:
                        if inc_file_name in line:
                            print('file {} is already included'.format(inc_file_name))
                            output_flag = False
                        elif 'Simulation Control Parameters' in line:
                            output_flag = False
                            fcopy.write('include .\{} \n'.format(inc_file_path))
                        fcopy.write(line)
                        line=fhand.readline()
                fcopy.write(line)
                line=fhand.readline()
        if overwrite:
            shutil.copy(self.grok_path, self.backup_copy)


    def add_target_output_times(self,out_times,target_times=None,overwrite=False):
        with open(self.backup_copy) as fhand, open(self.grok_path, 'w') as fcopy:
            line = fhand.readline()
            while line:
                if line.strip().lower().startswith('output times'):
                    o_time_flag = True
                    fcopy.write(line)
                    for t in out_times: 
                        fcopy.write('{0} \n'.format(t))
                        print('{0} \n'.format(t))
                    while o_time_flag:
                        if line.strip().lower().startswith('end'):
                            o_time_flag = False
                            fcopy.write(line)
                        line=fhand.readline()
                fcopy.write(line)
                line=fhand.readline()
        if overwrite:
            shutil.copy(self.grok_path, self.backup_copy)

        with open(self.backup_copy) as fhand, open(self.grok_path, 'w') as fcopy:
            line = fhand.readline()
            while line:
                if target_times:
                    if line.strip().lower().startswith('target times'):
                        tar_time_flag = True
                        fcopy.write(line)
                        for t in target_times: fcopy.write('{0} \n'.format(t))
                        while tar_time_flag:
                            if line.strip().lower().startswith('end'):
                                tar_time_flag = False
                                fcopy.write(line)
                            line=fhand.readline()
                fcopy.write(line)
                line=fhand.readline()
        if overwrite:
            shutil.copy(self.grok_path, self.backup_copy)