import unittest
import sys
import os
#from ..Accelera_Test_Cases.utils import *

class TestAddition(unittest.TestCase):
    """ A class which performs addition operation

        This has two test cases
    """
    def test_1_print(self):
        """ This test case prints some text
        """
        print "Adding"
    def test_2_add(self):
        """ This test case performs addition of two numbers
        """
        a=1
        b=-3
        c=a+b
        if not c < 0 : raise AssertionError
        
def test_generate_result():
    sys.path.append("..")
    import utils
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestAddition))
    print suite
    print __file__
    utils.run(suite, __file__)
