import time
import pandas as pd
import numpy as np
from datetime import datetime
from phildb.database import PhilDB
from phildb_client import PhilDBClient

pdb = PhilDB('hrs_phildb')
pdb_client = PhilDBClient('http://localhost:8989')

phildb_client_reads = []
for ts_id in pdb.ts_list():
    phildb_client_start = time.time()
    pdb_client.read(ts_id, 'D')
    phildb_client_end = time.time()

    phildb_client_reads.append(phildb_client_end - phildb_client_start)

np.savetxt('phildb_client_reads.txt', phildb_client_reads)
