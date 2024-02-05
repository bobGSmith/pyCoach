"""pyCoach

Scripts and functions for planning and tracking training. 

run scripts with the following:
    > python -m pyCoach.script_name args

scripts:
    * gen_session - take session plan data and convert it to readable txt document
        args: session_plan_data_csv_path, session_date (dd/mm/yyy), out_path.txt 
    * log_session - take a completed session plan txt doc and add it to training log csv
        args: path_to_session.txt, path_to_training_log.csv
    * find_pbs - find new PBs in the training log csv and add them to the PB csv
        args: path_to_training_log.csv, path_to_pb_data_csv
    * view_PBs - view the most up to date PBs for a given exercise 
        args: path_to_pb_data.csv
    * volume_intensity_curve - plot a curve of volume and intensity for given exercise 
        args: exercise, path_to_pb_data.csv
    
"""

from .gen_session import gen_session 
from .load_session import load_session 
from .log_session import log_session
from .add_data_to_csv import add_data_to_csv
from .find_pbs import is_pb

__version__ = "1.0.0"
__author__ = "bob g smith"
