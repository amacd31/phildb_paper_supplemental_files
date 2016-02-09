import os
import sys

import pandas as pd

for fname in sys.argv[1:]:
    station_id = os.path.basename(fname).split('_')[0]
    df = pd.read_csv(fname, parse_dates=True, index_col='Date', skiprows=26)

    df['Flow (ML)'].to_csv('{0}_scidb.csv'.format(station_id), header = False)
