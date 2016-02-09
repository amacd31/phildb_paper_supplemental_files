import subprocess

def write_scidb(file_list, results_file, first_run = False, file_suffix = 'scidb'):
    if first_run:
        subprocess.call(['bash', 'setup_scidb.sh', results_file, file_suffix, 'first_run'])
    else:
        subprocess.call(['bash', 'setup_scidb.sh', results_file, file_suffix])
