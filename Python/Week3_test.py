# import packages
import unittest
from Week3 import number

# define a test class that inherits unittest.TestCase class
class TestNumber(unittest.TestCase):

    # define a function to test basic cases
    def test_basic(self):
        self.assertEquals(number([[10,0],[3,5],[5,8]]),5)
        self.assertEquals(number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]),17)
        self.assertEquals(number([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]),21)

if __name__=='__main__':
    unittest.main()