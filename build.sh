#!/bin/bash

clear
echo "=================== Rm last test date ==================="
rm -rf /data/*.json 

echo "=================== Test ==================="
python -m unittest test_linear_move_found 
if [ $? -ne 0 ]; then
    echo "Unit test is FAILED. Exit."
    exit
fi

echo "=================== Gen date ==================="
spark-submit --properties-file spark.conf \
    --conf "spark.driver.extraJavaOptions=-Dlog4j.configuration=file:log4j.properties" \
    --conf "spark.executor.extraJavaOptions=-Dlog4j.configuration=file:log4j.properties" \
    generate.py 

if [ $? -ne 0 ]; then
    echo "Date isn't gerated. Exit."
    exit
fi

echo "=================== Run task ==================="
spark-submit --properties-file spark.conf \
    --conf "spark.driver.extraJavaOptions=-Dlog4j.configuration=file:log4j.properties" \
    --conf "spark.executor.extraJavaOptions=-Dlog4j.configuration=file:log4j.properties" \
    linear_move_found.py  

