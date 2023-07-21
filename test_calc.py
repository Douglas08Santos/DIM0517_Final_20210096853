from Calc import add, sub
import unittest

class TestCalc(unittest.TestCase):
    def test_calc(self):
        print("Running tests...")
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(sub(4, 3), 1)
        self.assertEqual(sub(3, 4), -1)

if __name__=='__main__':
	unittest.main()