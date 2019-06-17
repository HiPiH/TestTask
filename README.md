# TestTask

#For run in docker
docker build --tag testtaskimage . && docker run --rm testtaskimage 

#Run test
python -m unittest test_linear_move_found 

#Run gen data
./generate.py [count object | default 10000]

#Run task
./linear_move_found.py  [raw file | default raw.json]