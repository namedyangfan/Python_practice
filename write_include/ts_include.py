import os, glob, shutil

class Write_include():
    def __init__(self, grok_directory, inc_folder, o_folder, o_name):
        ''' build include file for PET and PCP'''
        self.inc_path = os.path.join(grok_directory,inc_folder)
        self.o_directory = os.path.join(grok_directory,o_folder)
        self.o_path = os.path.join(o_directory,o_name)

        if not os.path.exists(self.inc_path):
            print("File not found: {0}".format(self.grok_path))
            return None
        if not os.path.exists(self.o_directory):
            print("File not found: {0}".format(self.o_directory))
            return None
    def ls_inc(self):
        filename= glob.glob(self.o_directory)
        print(filename)
        
        

