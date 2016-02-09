import os
import sys
import pandas as pd

def gen_update_files(id_list):
    for ts_id in id_list:
        streamflow = pd.read_csv("{0}_scidb.csv".format(ts_id), parse_dates=True, index_col=0, header=None)

        updated_streamflow = streamflow.copy()

        # Update only the last 10 records
        updated_streamflow[-10:] = streamflow.ix[-10:] * 1.1
        updated_streamflow.to_csv("{0}_update1.csv".format(ts_id), header = None)

        # Update only the first 10 records
        updated_streamflow[:10] = streamflow.ix[:10] * 1.1
        updated_streamflow.to_csv("{0}_update2.csv".format(ts_id), header = None)

        updated_streamflow = streamflow * 1.1
        updated_streamflow.to_csv("{0}_update3.csv".format(ts_id), header = None)

        updated_streamflow = streamflow * 1.1
        updated_streamflow.to_csv("{0}_update4.csv".format(ts_id), header = None)

