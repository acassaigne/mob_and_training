import unittest

class Row:

    def __init__(self, list):
        self.values = list

    def __eq__(self, other):
        return self.values == other.values


class TestTicTacToe(unittest.TestCase):

    def test_empty_list_should_not_equal_X(self):
        a_row = Row(['X'])
        a_empty_row = Row(['.'])
        self.assertNotEqual(a_empty_row, a_row)

    def test_empty_should_equal_empty(self):
        a_row = Row(['.'])
        a_empty_row = Row(['.'])
        self.assertEqual(a_empty_row, a_row)

    def test_x(self):
        a_row = Row(['.','.'])
        a_empty_row = Row(['.','.'])
        self.assertEqual(a_empty_row, a_row)