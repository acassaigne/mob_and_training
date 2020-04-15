import unittest

class Row:

    def __init__(self, length):
        self.values = length*[MarkEmpty()]

    def __eq__(self, other):
        return self.values == other.values

    def update(self, position, character):
        if position >= len(self.values):
            raise InvalidUpdateRow
        self.values[position] = character


class Board:

    def __init__(self, length):
        self.rows = length * [Row(length)]

    def update(self, position, mark):
        self.rows[position.row].update(position.column, mark)

    def __eq__(self, other):
        return self.rows == other.rows


class Position:

    def __init__(self, row, column):
        self.row = row
        self.column = column


class InvalidUpdateRow(Exception):
    pass


class Mark:
    def __eq__(self, other):
        return type(self) == type(other)


class MarkEmpty(Mark):
    pass


class MarkX(Mark):
    pass


class MarkO(Mark):
    pass


class TestTicTacToe(unittest.TestCase):

    def test_update_row_with_X_should_equal_created_row(self):
        a_row = Row(2)
        a_row.update(1, MarkX())
        self.assertNotEqual(Row(2), a_row)

    def test_should_raise_if_out_of_bounds(self):
        a_row = Row(1)
        with self.assertRaises(InvalidUpdateRow):
            a_row.update(1, MarkX())

    def test_x(self):
        a_board = Board(2)
        a_board.update(Position(1,0), MarkX())
        self.assertNotEqual(Board(2), a_board)

    def test_y(self):
        a_board = Board(2)
        self.assertEqual(Board(2), a_board)