# Name: Sean Perez
# Date: 4/16/22
# CS362 - HW2


import unittest
from contrived_func import contrived_func


class TestCase(unittest.TestCase):
    """Unittest to find 6 bugs in the credit_card_validator func"""

    # Length related tests

    # Verifies if empty string returns False
    # Picked using Category Partition Testing
    def test1_125(self):
        less_than_150 = 125
        self.assertTrue(contrived_func(less_than_150),
                        msg=''.format(contrived_func(less_than_150)))

    def test2_75(self):
        less_than_100 = 75
        self.assertFalse(contrived_func(less_than_100),
                         msg=''.format(contrived_func(less_than_100)))

    def test3_F(self):
        greater_than_150 = 362
        self.assertFalse(contrived_func(greater_than_150),
                         msg=''.format(contrived_func(greater_than_150)))

    def test4_6(self):
        val_is_6 = 6
        self.assertFalse(contrived_func(val_is_6),
                         msg=''.format(contrived_func(val_is_6)))

    def test5_8(self):
        val_is_8 = 8
        self.assertTrue(contrived_func(val_is_8),
                        msg=''.format(contrived_func(val_is_8)))

    def test6_80(self):
        val_is_80 = 80
        self.assertTrue(contrived_func(val_is_80),
                        msg=''.format(contrived_func(val_is_80)))

    def test7_50(self):
        val_is_50 = 50
        self.assertTrue(contrived_func(val_is_50),
                        msg=''.format(contrived_func(val_is_50)))


if __name__ == '__main__':
    unittest.main(verbosity=2)
