import unittest
import sys
import os
#import utils

class TestMultiplication(unittest.TestCase):
    def test_1_print(self):
        print "Multiplying"
    def test_2_multi(self):
        a=1
        b=3
        c=a*b
        print("Multiplication is %d" % c)
      
def test_generate_result():
    sys.path.append("..")
    import utils
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestMultiplication))
    print suite
    print __file__
    utils.run(suite, __file__)
