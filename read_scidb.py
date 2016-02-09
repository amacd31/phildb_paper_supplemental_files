import time
import pandas as pd
import numpy as np
from datetime import datetime

def read_scidb(id_list, sdb, results_file):
    scidb_reads = []
    for ts_id in id_list:
        qid = 'Q' + ts_id
        scidb_start = time.time()
        sdb.wrap_array(qid).todataframe()
        scidb_end = time.time()

        scidb_reads.append(scidb_end - scidb_start)

    np.savetxt(results_file, scidb_reads)

def read_scidb_log(id_list, sdb, results_file, version):
    scidb_reads = []
    for ts_id in id_list:
        qid = 'Q{0}@{1}'.format(ts_id, version)
        scidb_start = time.time()
        sdb.wrap_array(qid).todataframe()
        scidb_end = time.time()

        scidb_reads.append(scidb_end - scidb_start)

    np.savetxt(results_file, scidb_reads)
