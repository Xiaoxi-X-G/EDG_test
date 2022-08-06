import os
from os.path import dirname, realpath

dir_root = dirname(dirname(realpath(__file__)))

dir_raw_data = dir_root+'/data/raw/'
dir_data = dir_root+'/data/'
mlrun_artifacts = dir_root+ '/mlrun/mlrun_artifacts'
mlrun_db = "sqlite:///"+dir_root+ '/mlrun/mlrun_db/mldb.sqlite'