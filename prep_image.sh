scp authorized_keys scidb@${SCIDB_HOST}:.ssh/
scp authorized_keys root@${SCIDB_HOST}:.ssh/

scp Anaconda3-2.4.1-Linux-x86_64.sh scidb@${SCIDB_HOST}:
ssh scidb@${SCIDB_HOST} "bash Anaconda3-2.4.1-Linux-x86_64.sh -b"
ssh scidb@${SCIDB_HOST} "echo 'export PATH=/home/scidb/anaconda3/bin:\$PATH' >> ~/.bashrc"
ssh scidb@${SCIDB_HOST} "rm Anaconda3-2.4.1-Linux-x86_64.sh"

scp PhilDB-0.6.1.tar.gz scidb@${SCIDB_HOST}:
scp phildb_server.zip scidb@${SCIDB_HOST}:
scp phildb_client.zip scidb@${SCIDB_HOST}:
ssh scidb@${SCIDB_HOST} "pip install PhilDB-0.6.1.tar.gz"
ssh scidb@${SCIDB_HOST} "pip install phildb_server.zip"
ssh scidb@${SCIDB_HOST} "pip install phildb_client.zip"

scp scidb-py-14.10.0.tar.gz scidb@${SCIDB_HOST}:
ssh scidb@${SCIDB_HOST} "pip install scidb-py-14.10.0.tar.gz"

scp influxdb-0.9.6.1-1.x86_64.rpm root@${SCIDB_HOST}:
ssh root@${SCIDB_HOST} "yum localinstall -y influxdb-0.9.6.1-1.x86_64.rpm"
scp influxdb.conf root@${SCIDB_HOST}:/etc/influxdb/influxdb.conf
ssh root@${SCIDB_HOST} "service influxdb start"

scp influxdb-2.11.0.tar.gz scidb@${SCIDB_HOST}:
ssh scidb@${SCIDB_HOST} "pip install influxdb-2.11.0.tar.gz"

scp setup_phildb.py scidb@${SCIDB_HOST}:
scp setup_influxdb.py scidb@${SCIDB_HOST}:

scp *_scidb.csv scidb@${SCIDB_HOST}:
scp modify.py scidb@${SCIDB_HOST}:

scp station_list.txt scidb@${SCIDB_HOST}:

scp setup_scidb.py scidb@${SCIDB_HOST}:
scp setup_scidb.sh scidb@${SCIDB_HOST}:
scp clear_scidb.sh scidb@${SCIDB_HOST}:

scp read_phildb.py scidb@${SCIDB_HOST}:
scp read_phildb_client.py scidb@${SCIDB_HOST}:
scp read_scidb.py scidb@${SCIDB_HOST}:
scp read_influxdb.py scidb@${SCIDB_HOST}:

scp run_tests.py scidb@${SCIDB_HOST}:
