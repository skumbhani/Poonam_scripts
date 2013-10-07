import unittest
import sys
import os
#from ..Accelera_Test_Cases.utils import *

class TestUpdate(unittest.TestCase):
    def test_1_print(self):
        global dictname
        dictname = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
        print("Dictionary before updating")
        print dictname
    def test_2_update(self):
        dictname['Age'] = 8
        dictname['School'] = "DPS School";
        print("Dictionary after updating")
        print dictname

def test_generate_result():
    sys.path.append("..")
    import utils
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestUpdate))
    print suite
    print __file__
    utils.run(suite, __file__)


        

    

