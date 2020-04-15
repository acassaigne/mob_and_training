import unittest

class Row:

    def __init__(self, list_of_values):
        self.values = list_of_values

    def __eq__(self, other):
        return self.values == other.values

    def update(self, position, character):
        if position >= len(self.values):
            raise InvalidUpdateRow
        self.values[position] = character


class InvalidUpdateRow(Exception):
    pass


class TestTicTacToe(unittest.TestCase):

    def test_empty_list_should_not_equal_X(self):
        a_row = Row(['X'])
        a_empty_row = Row(['.'])
        self.assertNotEqual(a_empty_row, a_row)

    def test_empty_should_equal_empty(self):
        a_row = Row(['.'])
        a_empty_row = Row(['.'])
        self.assertEqual(a_empty_row, a_row)

    def test_update_row_with_X_should_equal_created_row(self):
        a_row = Row(['.', '.'])
        a_row.update(1, 'X')
        self.assertEqual(Row(['.', 'X']), a_row)

    def test_x(self):
        a_row = Row(['.'])
        with self.assertRaises(InvalidUpdateRow):
            a_row.update(1, 'X')