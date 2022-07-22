import unittest
from Week1 import positive_sum

class TestPositiveSum(unittest.TestCase):

    # define a function to test basic cases
    def test_basic(self):
        self.assertEquals(positive_sum([1,2,3,4,5]), 15)
        self.assertEquals(positive_sum([1,-2,3,4,5]), 13)
        self.assertEquals(positive_sum([-1,2,3,4,-5]), 9)

    # define a function to test empty case
    def test_empty(self):
        self.assertEquals(positive_sum([]), 0)      
        
    # define a function to test all negative case
    def test_negative(self):
        self.assertEquals(positive_sum([-1,-2,-3,-4,-5]), 0)

if __name__=='__main__':
    unittest.main()