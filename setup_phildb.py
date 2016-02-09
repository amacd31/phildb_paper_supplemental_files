import os
import time
import pandas as pd
import numpy as np
from phildb.database import PhilDB

from phildb.create import create

freq = 'D'

def write_phildb(file_list, results_file, first_run = False):
    if first_run:
        create('hrs_phildb')

    db = PhilDB('hrs_phildb')

    if first_run:
        db.add_measurand('Q', 'STREAMFLOW', 'Streamflow')
        db.add_source('BOM_HRS', 'Bureau of Meteorology; Hydrological Reference Stations dataset.')

    write_times = []
    for filename in file_list:
        print("Processing file: ", filename, '...')
        station_id = os.path.basename(filename).split('_')[0]
        print("Using station ID: ", station_id, '...')
        streamflow = pd.read_csv(filename, parse_dates=True, index_col=0, header = None)
        if first_run:
            db.add_timeseries(station_id)
            db.add_timeseries_instance(station_id, freq, '', measurand = 'Q', source = 'BOM_HRS')
        start = time.time()
        db.write(station_id, freq, streamflow, measurand = 'Q', source = 'BOM_HRS')
        write_times.append(time.time() - start)

    np.savetxt(results_file, np.array(write_times))
