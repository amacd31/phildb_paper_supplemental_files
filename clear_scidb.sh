for station in `ls -1 *_scidb.csv | cut -f1 -d'_'`
do
    #echo ${station}
    iquery -a -n -q "remove(Q${station});"
done

