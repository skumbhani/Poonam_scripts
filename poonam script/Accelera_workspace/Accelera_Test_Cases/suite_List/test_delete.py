import unittest
import sys
import os
#from ..Accelera_Test_Cases.utils import *

class TestDelete(unittest.TestCase):
    def test_1_print(self):
        global lis
        lis = [1,2,6,8,7]
        print("List before deleting element")
        print lis
    def test_2_delete(self):
        print("Deleting an element from the list")
        del lis[3]
        print("List After Deleting")
        print lis
        
def test_generate_result():
    sys.path.append("..")
    import utils
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestDelete))
    #print suite
    #print __file__
    utils.run(suite, __file__)
