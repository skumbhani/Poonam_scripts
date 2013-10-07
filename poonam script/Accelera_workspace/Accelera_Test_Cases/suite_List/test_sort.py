import unittest
import sys
import os
#from ..Accelera_Test_Cases.utils import *

class TestSort(unittest.TestCase):
    def test_1_print(self):
        global lis
        lis = [1,2,6,8,7]
        print("List before sorting")
        print lis
    def test_2_sort(self):
        print("Sorting the list")
        set(lis)
        print("List After Sorting")
        print lis
        
def test_generate_result():
    sys.path.append("..")
    import utils
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSort))
    #print suite
    #print __file__
    utils.run(suite, __file__)
