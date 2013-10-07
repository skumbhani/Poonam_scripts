import unittest
import sys
import os
#from ..Accelera_Test_Cases.utils import *

class TestAddition(unittest.TestCase):
    def test_1_print(self):
        print "Adding"
    def test_2_add(self):
        a=1
        b=3
        c=a+b
        print("Addition is %d" % c)
        
def test_generate_result():
    sys.path.append("..")
    import utils
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestAddition))
    print suite
    print __file__
    utils.run(suite, __file__)
