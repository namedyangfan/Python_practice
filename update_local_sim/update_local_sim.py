import os,  errno, shutil, glob, warnings, time, sys
import pandas as pd


class Update_local_sim():
    ''' a class that update local simulation based on remote simulation
        It is common to run multiple simulations remotely on other machines.
        Contineausly checking the status of those simulation can be time consuming. 
        This script automaticly checks the status of the simulation and print out the current time step. 
        This is done by reading the .lst in the simulation folder file.
        After the simulation is completed, this script will copy the selcted files to the local foder.

        Note: The remote simulation folder has to be maped to the local computer
    ''' 
    def __init__ (self, remote_directory, local_directory):
        ''' 
        remote_directory: the directory of remote simulation
        local_directory: the directory of the local simulation
        The remote simulation has to share the same folder name as the local simulation
        '''
        self.remote_directory = remote_directory
        self.local_directory = local_directory
        self.end_simu_flag = False
        self.timestep = 0

        #check the folder names are the same 
        base_remote_directory = os.path.basename(self.remote_directory)
        base_local_directory = os.path.basename(self.local_directory) 
        if not base_remote_directory == base_local_directory:
            raise ValueError( 'remote and local folder name does not match \n remote: {} \n local {}'
                .format(base_remote_directory, base_local_directory))

        if not os.path.exists(self.remote_directory):
            raise FileNotFoundError(
            errno.ENOENT, os.strerror(errno.ENOENT), self.remote_directory)
        if not os.path.exists(self.local_directory):
            raise FileNotFoundError(
            errno.ENOENT, os.strerror(errno.ENOENT), self.local_directory)

    def load_prefix(self, dirct):
        """ Reads batch.pfx to get the prefix name """
        # Use the os library to combine self.path with "batch.pfx" to get the full path to batch.pfx
        # Read batch.pfx, 
        batchpath= os.path.join(dirct, "batch.pfx")
        with open(batchpath, 'r') as f:
            prefix = f.readline().strip()
            prefixo = prefix + "o"
        return(prefixo)

    def load_lst_remote(self,ldebug= False):
        '''read the .lst file from the remote simulation'''
        # find the prefix of the simulation
        self.remote_prefix = self.load_prefix(dirct=self.remote_directory)
        # find the path of the .lis file
        self.remote_lst = os.path.join(self.remote_directory, self.remote_prefix + ".lst")
        if ldebug: print(self.remote_directory)
        if not os.path.exists(self.remote_lst):
            raise FileNotFoundError(
            errno.ENOENT, os.strerror(errno.ENOENT), self.remote_lst)
        if ldebug: print(self.remote_lst)

    def walk_lst_remote(self):
        ''' read the list file and print out the current timestep'''
        while not self.end_simu_flag:
            backup_copy = self.remote_lst + '.preunsat_original'
            try:
                shutil.copy(self.remote_lst, backup_copy)
            except:
                print("Not able to copy lst file")
                
            time.sleep(30)
            with open (backup_copy) as fhandl:

                for line in fhandl:
                    # print out the TIMESTEP
                    # if line.strip().startswith('SOLUTION FOR TIMESTEP'):
                    if "SOLUTION FOR TIMESTEP" in line.strip():
                        t = line.strip().split()[-1]
                        if int(t) > self.timestep: 
                            self.timestep= int(t)
                            # sys.stdout.flush()
                            # print('{}\tSOLUTION FOR TIMESTEP: {} \n'.format(os.path.basename(self.remote_directory), self.timestep))

                    elif "SIMULATION TIME REPORT" in line.strip():
                        # end_simu_flag true means simulation is completed
                        self.end_simu_flag = True
                        while line:
                            print(line)
                            line = fhandl.readline()

                print('{}\tSOLUTION FOR TIMESTEP: {} \n'.format(os.path.basename(self.remote_directory), self.timestep))
                sys.stdout.flush()

    def cp_file (self, types= ['*.lst','*.hen','*hydrograph.*', '*observation_well_flow.*', '*.grok'], ldebug=False):
        ''' After simulation is completed, move the files from remote to local'''

        # set up glob.glob pattern 
        types_path = [os.path.join(self.remote_directory, i) for i in types]
        files_grabbed=[]
        # get a list of files that need to be copied
        files_grabbed.extend(glob.glob(e) for e in types_path)
        files_grabbed = [y for x in files_grabbed for y in x]
        if ldebug: [print(files_grabbed) for x in files_grabbed]
        if len(files_grabbed) == 0: warnings.warn( 'WARNING: No file has been moved')
        [shutil.copy(x, self.local_directory) for x in files_grabbed]
        print('{} files have beens move to {} \n from '.format(len(files_grabbed), self.local_directory, self.remote_directory))

if __name__ == "__main__":
    remote_directory = r"X:\26-33-SARB_daily_47764Nodes"
    local_directory = r"D:\ARB\HGS_Simulations\Sub_Assiniboine\steve_Jun\26-33-SARB_daily_47764Nodes"
    rl = Update_local_sim (remote_directory, local_directory)
    rl.load_lst_remote(ldebug=False)
    rl.walk_lst_remote()
    rl.cp_file()