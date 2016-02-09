import os
import sys
import time
import datetime
import numpy as np
import pandas

from influxdb import InfluxDBClient, DataFrameClient
from influxdb.exceptions import InfluxDBClientError

client = DataFrameClient('localhost', 8086, 'root', 'root', 'hrs_experiment')

try:
    print("Drop database")
    client.drop_database('hrs_experiment')
except InfluxDBClientError:
    pass # Didn't already exist for dropping.

print("Create database")
client.create_database('hrs_experiment')

write_times = []
for i in range(1, len(sys.argv)):
    print("Processing file: ", sys.argv[i], '...')
    station_id = 'Q' + os.path.basename(sys.argv[i]).split('_')[0]
    print("Using station ID: ", station_id, '...')
    df = pandas.read_csv(sys.argv[i], parse_dates=True, index_col=0, header = None)
    print("Creating JSON data...")
    print("Writing data...")
    start = time.time()
    for k, g in df.groupby(np.arange(len(df))//100):
        client.write_points(g, station_id)
    write_times.append(time.time() - start)
    print("Data written in {0} seconds".format(write_times[-1]))
    print("Sleeping for 30 seconds...")
    time.sleep(30)

np.savetxt("influx_write_times.txt", np.array(write_times))
