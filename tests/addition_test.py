import unittest
from src.addition import summation

# setup a class to test the summation function
class TestSummation(unittest.TestCase):
    def test_correct_two_pos(self):
        # assert true means the statement enclosed should be true
        self.assertTrue(summation(1, 1) == 2)

    def test_incorrect_two_pos(self):
        self.assertFalse(summation(1, 2) == 2)

    def test_correct_one_pos_one_neg(self):
        self.assertTrue(summation(1, -2) == -1)

    def test_incorrect_one_pos_one_neg(self):
        self.assertFalse(summation(5, -3) == 5)
    
    def test_correct_decimal(self):
        self.assertTrue(summation(0.5, 1.5) == 2)