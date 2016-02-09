import subprocess
import pandas as pd
from datetime import datetime

import scidbpy
from phildb.database import PhilDB
from phildb_client import PhilDBClient

from modify import gen_update_files
from setup_phildb import write_phildb
from setup_scidb import write_scidb
from read_phildb import read_phildb, read_phildb_log
from read_scidb import read_scidb, read_scidb_log

id_list = pd.read_csv('station_list.txt', header=None).values[:,0]
gen_update_files(id_list)

file_list = ["{0}_scidb.csv".format(x) for x in id_list]

phildb_du_results = []
scidb_du_results = []

phildb_du_results.append('0\\thrs_phildb\\n')
scidb_du_results.append(subprocess.check_output(['du', '-s', 'scidbdata']))

write_phildb(file_list, 'phildb_initial_writes.txt', first_run = True)
# Start PhilDB server now that a phildb instance exists
subprocess.Popen(['phildb-server', '--port=8989', 'hrs_phildb'])

write_scidb(file_list, 'scidb_initial_writes.txt', first_run = True)

# Connect Python APIs
sdb = scidbpy.connect('http://localhost:8080', 'scidb', 'paradigm4')
pdb = PhilDB('hrs_phildb')
pdb_client = PhilDBClient('http://localhost:8989')

# Read the three clients, interleaving PhilDB with SciDB to try minimise
# the effects of caching
read_phildb(id_list, pdb, 'phildb_initial_reads.txt')
read_scidb(id_list, sdb, 'scidb_initial_reads.txt')
read_phildb(id_list, pdb_client, 'phildb_client_initial_reads.txt')

# Do updates
for i in range(1,5):
    # Generate file list for first update
    file_list = ["{0}_update{1}.csv".format(x, i) for x in id_list]

    mod_datetime = datetime.now()
    phildb_du_results.append(subprocess.check_output(['du', '-s', 'hrs_phildb']))
    scidb_du_results.append(subprocess.check_output(['du', '-s', 'scidbdata']))
    write_phildb(file_list, 'phildb_update{0}_writes.txt'.format(i), first_run = False)
    write_scidb(file_list, 'scidb_update{0}_writes.txt'.format(i), first_run = False, file_suffix = 'update{0}'.format(i))

    # Read the three clients, interleaving PhilDB with SciDB to try minimise
    # the effects of caching
    read_phildb(id_list, pdb, 'phildb_update{0}_reads.txt'.format(i))
    read_scidb(id_list, sdb, 'scidb_update{0}_reads.txt'.format(i))
    read_phildb_log(id_list, pdb, 'phildb_log{0}_reads.txt'.format(i), mod_datetime)
    read_phildb(id_list, pdb_client, 'phildb_client_update{0}_reads.txt'.format(i))
    read_scidb_log(id_list, sdb, 'scidb_log{0}_reads.txt'.format(i), i)

phildb_du_results.append(subprocess.check_output(['du', '-s', 'hrs_phildb']))
scidb_du_results.append(subprocess.check_output(['du', '-s', 'scidbdata']))
pd.Series(phildb_du_results).to_csv('phildb_disk_usage_results.txt')
pd.Series(scidb_du_results).to_csv('scidb_disk_usage_results.txt')
