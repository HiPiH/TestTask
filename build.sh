#!/bin/bash

clear
echo "=================== Rm last test date ==================="
rm -rf $PWD/*.json 

echo "=================== Test ==================="
python -m unittest test_linear_move_found 
if [ $? -ne 0 ]; then
    echo "Unit test is FAILED. Exit."
    exit
fi

echo "=================== Gen date ==================="
./generate.py 

if [ $? -ne 0 ]; then
    echo "Date isn't gerated. Exit."
    exit
fi

echo "=================== Found ==================="
./linear_move_found.py  

