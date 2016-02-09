results_file=$1
file_suffix=$2

if [ "$3" == "first_run" ]; then
    echo "First run"
    first_run=true
else
    echo "Not first run"
    first_run=false
fi

for station in $(cat station_list.txt)
do
    csv2scidb -i ${station}_${file_suffix}.csv -o ${station}.scidb
    if [ "$first_run" = true ]; then
        #len=$(wc -l ${station}.scidb)
        iquery -q "CREATE ARRAY Q${station} <date:datetime, streamflow:double> [i=0:*,10000,0];"
    fi

    startwrite=`date +%s.%N`
    iquery -n -q "LOAD Q${station} FROM '/home/scidb/${station}.scidb';"
    endwrite=`date +%s.%N`

    python -c "print($endwrite - $startwrite, file=open('$results_file', 'a'))"
done

