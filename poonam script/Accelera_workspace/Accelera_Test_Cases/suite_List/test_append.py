import unittest
import sys
import os

class TestAppend(unittest.TestCase):
    def test_1_print(self):
        global lis
        lis = [1,2,6,8,7]
        print("List before appending")
        print lis
    def test_2_append(self):
        print("Appeding the list")
        lis.append('a')
        print("List After appending")
        print lis
        
def test_generate_result():
    sys.path.append("..")
    import utils
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestAppend))
    #print suite
    #print __file__
    utils.run(suite, __file__)
