#!/usr/bin/python

from __future__ import print_function

import sys
import argparse

from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType




def parseCommandLine():
    
    """
       Generate parser command line argument
    """

    parser = argparse.ArgumentParser(
        prog="linear_move_found",
        description="""
            Test task for finding linear moving objects.

        """,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("-i","--input", help="Input json file.", default="raw.json")
    return parser


def found(points):
    
    """
        Found linear object 
        points -> list 
    """

    count = 1
    for x,y in points[1:]:
        if points[0][0] != x and points[0][1] != y:
            return 0
        count+=1
    return 1 if count > 1 else 0


if __name__ == "__main__":

    args = parseCommandLine().parse_args()    

    spark = SparkSession\
        .builder\
        .appName("Linear move found")\
        .getOrCreate()

    sc = spark.sparkContext
    
    input_df = spark.read.load(args.input,format="json")

    found_fn = udf(found,IntegerType())    
    new_table = input_df.withColumn("type",found_fn("points"))
    linear_objects = new_table.where(new_table.type == 1)
    linear_objects.show()
    print("Found object:",linear_objects.count())


    spark.stop()