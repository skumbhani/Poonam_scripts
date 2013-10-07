import unittest
import sys
import os
#from ..Accelera_Test_Cases.utils import *

class TestDelete(unittest.TestCase):
    def test_1_print(self):
        global dictname
        dictname = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
        print("Dictionary before deleting")
        print dictname
    def test_2_delete(self):
        del dictname['Name']
        print("Dictionary after deleting a element")
        print dictname
        
def test_generate_result():
    sys.path.append("..")
    import utils
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestDelete))
    print suite
    print __file__
    utils.run(suite, __file__)
