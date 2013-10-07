import unittest
import sys
import os
#import utils

class Testsubtraction(unittest.TestCase):
    def test_1_print(self):
        print "Subtracting"
    def test_2_sub(self):
        a=1
        b=3
        c=b-a
        print("Subtraction is %d" % c)

def test_generate_result():
    sys.path.append("..")
    import utils
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Testsubtraction))
    print suite
    print __file__
    utils.run(suite, __file__)        

