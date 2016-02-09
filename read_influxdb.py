import time
import pandas as pd
import numpy as np
from datetime import datetime
from influxdb import InfluxDBClient
from phildb.database import PhilDB

pdb = PhilDB('hrs_phildb')

idb = InfluxDBClient('localhost', 8086, 'root', 'root', 'hrs_experiment')

influxdb_reads = []
for ts_id in pdb.ts_list():
    station_id = 'Q{0}'.format(ts_id)
    influxdb_start = time.time()
    idb.query('SELECT * FROM {0}'.format(station_id))
    influxdb_end = time.time()

    influxdb_reads.append(influxdb_end - influxdb_start)

np.savetxt('influxdb_reads.txt', influxdb_reads)
