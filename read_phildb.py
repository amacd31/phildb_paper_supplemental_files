import time
import pandas as pd
import numpy as np
from datetime import datetime
from phildb.database import PhilDB

def read_phildb(id_list, pdb, results_file):
    phildb_reads = []
    for ts_id in id_list:
        phildb_start = time.time()
        pdb.read(ts_id, 'D')
        phildb_end = time.time()

        phildb_reads.append(phildb_end - phildb_start)

    np.savetxt(results_file, phildb_reads)

def read_phildb_log(id_list, pdb, results_file, mod_datetime):
    phildb_reads = []
    for ts_id in id_list:
        phildb_start = time.time()
        pdb.read_log(ts_id, 'D', mod_datetime)
        phildb_end = time.time()

        phildb_reads.append(phildb_end - phildb_start)

    np.savetxt(results_file, phildb_reads)
