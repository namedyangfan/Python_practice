import os, sys
from argparse import ArgumentParser, RawDescriptionHelpFormatter
# class module
from update_local_sim import Update_local_sim

def run_update(remote_directory, local_directory, ldebug):
    # remote_directory = r"X:\26-33-SARB_daily_47764Nodes"
    # local_directory = r"D:\ARB\HGS_Simulations\Sub_Assiniboine\steve_Jun\26-33-SARB_daily_47764Nodes
    print(remote_directory)
    print(local_directory)
    rl = Update_local_sim (remote_directory, local_directory)
    rl.load_lst_remote(ldebug=ldebug)
    rl.walk_lst_remote()
    rl.cp_file()

## parse arguments

# Setup argument parser
parser = ArgumentParser(description='Update local simulation from remote')
# mprops file (only positional argument, since it is required)
parser.add_argument('remote_dirct', metavar='remote_dirct', type=str, help="directory of the remote simulation folder")
parser.add_argument('local_dirct', metavar='local_dirct', type=str, help="directory of the local simulation folder")

# misc settings
parser.add_argument("--debug", dest="debug", action="store_true", help="print debug output [default: %(default)s]")

## assign parameters
args = parser.parse_args()

# command options
remote_directory = args.remote_dirct
local_directory = args.local_dirct

# other options
ldebug = args.debug

run_update(remote_directory=remote_directory, local_directory=local_directory, ldebug=ldebug)