#!/usr/bin/python

import unittest

from linear_move_found import parseCommandLine, found

class Point(object):
    def __init__(self, x ,y):
        self.x = x
        self.y = y

class TestLinearMoveFound(unittest.TestCase):
        
    def test_command_line_argument_empty(self):
        
        """
            Test command line parser without data
        """

        result = parseCommandLine().parse_args([])
        self.assertEquals(result.input, "raw.json")


    def test_command_line_argument_1(self):
        
        """
            Test command line parser with data
        """

        result = parseCommandLine().parse_args(['--input',"*"])
        self.assertEquals(result.input, "*")


    def test_command_line_any_arguments(self):
        
        """
            Test command line parser check params
        """

        result = parseCommandLine().parse_args([])
        self.assertEquals(result.__dict__.keys(),['input'])


    def test_found_list_empty(self):
        
        """
            if put list is empty  
        """

        result = found([])
        self.assertEquals(result,0)


    def test_found_list_one_item(self):
        
        """
          if put list from one item
        """

        result = found([(0,0)])
        self.assertEquals(result,0)


    def test_found_list_not_linear(self):
        
        """
            if put list not linear 
        """

        result = found([(0,0),(10,10)])   
        self.assertEquals(result,0)

    def test_found_list_linear(self):
        
        """
            if put list contain linear points
        """

        result = found([(0,0),(0,10)])   
        self.assertEquals(result,1)