#!/usr/bin/python

from __future__ import print_function


import sys
import argparse
from random import random


from pyspark.sql import SparkSession, functions as F, Row




def parseCommandLine():
    
    """
       Generate parser command line argument
    """

    parser = argparse.ArgumentParser(
        prog="generate",
        description="""
            Generate date for linear_move_found

        """,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("-c","--count", help="It is count generated objects.", default=10000)
    return parser.parse_args()




def generateObject(i):
   
    """
        Generate list points (x,y) 
        Points gets randome.
        There is also a condition on which the linen coordinates are obtained.
    """
   
    to_x = int(random()*100)
    to_y = int(random()*100)

    points = [Row(
                  x= to_x if to_x > 90 else (int(random()*100)),
                  y= to_y if to_y > 90 else (int(random()*100))
                 ) for x in range(0,100)]
    return Row(id=i,points=points) 
    

if __name__ == "__main__":

    args = parseCommandLine()    
   
    spark = SparkSession\
        .builder\
        .appName("Generate")\
        .getOrCreate()

    sc = spark.sparkContext
    sc.setLogLevel("WARN")
    df = spark.createDataFrame(
        sc.parallelize(range(1, args.count+1))
        .map(generateObject)
    )   
    
    df.write.json("raw.json")
    points_count = df.rdd.flatMap(lambda x : x.points).count()
    print("Generate {0} objects with {1} points".format(args.count,points_count))
    spark.stop()