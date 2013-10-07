import unittest
import sys
import os
#import utils
    
class TestDivision(unittest.TestCase):
    def test_1_print(self):
        print "Dividing"
    def test_2_divide(self):
        a=1
        b=3
        c=b/a
        print("Division is %d" % c)
        
def test_generate_result():
    sys.path.append("..")
    import utils
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestDivision))
    print suite
    print __file__
    utils.run(suite, __file__)