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
    def test1_empty(self):
        empty_string = ""
        self.assertFalse(contrived_func(empty_string),
                         msg=''.format(contrived_func(empty_string)))


if __name__ == '__main__':
    unittest.main(verbosity=2)
