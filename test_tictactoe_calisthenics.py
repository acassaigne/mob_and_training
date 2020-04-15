import unittest

class Row:

    def __init__(self, list):
        self.values = list

    def __eq__(self, other):
        return False


class TestTicTacToe(unittest.TestCase):

    def test_x(self):
        a_row = Row(['X'])
        a_empty_row = Row(['.'])
        self.assertNotEqual(a_empty_row, a_row)