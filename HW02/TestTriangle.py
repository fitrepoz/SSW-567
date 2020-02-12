# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

import math

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right','5,3,4 is a Right triangle')

    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1, 1, 1),'Equilateral', '1,1,1 should be equilateral')

    #--New Tests--#
     
    def testA(self):
        self.assertEqual(classifyTriangle(20, 10, 60), 'Isosceles', '20, 10, 60 should be isosceles')
    
    def testB(self):
        self.assertEqual(classifyTriangle(2, 7, 7), 'Isosceles', '2, 7, 7 should be isosceles')
    
    def testC(self):
        self.assertEqual(classifyTriangle(3, 4, 6), 'Scalene', '3, 4, 3 should be scalene')
        
    def testD(self):
        self.assertEqual(classifyTriangle(100, 99, 102), 'Scalene', '100, 99, 102 should be scalene')
         
    def testE(self):
        self.assertEqual(classifyTriangle(10, 10, 10), 'Equilateral', '10, 10, 10 should be Equilateral')
         

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit = False, verbosity= 2)
