import unittest

class Row:

    def __init__(self, length):
        self.values = length*[MarkEmpty()]

    def __eq__(self, other):
        return self.values == other.values

    def put_mark_in_row(self, position, character):
        if  position >= len(self.values) or position < 0:
            raise InvalidUpdateRow
        self.values[position] = character


class Board:

    def __init__(self, length):
        self.length = length
        self.rows = self.length * [Row(self.length)]

    def put_mark_in_board(self, position, mark):
        self.rows[position.row].put_mark_in_row(position.column, mark)

    def __eq__(self, other):
        return self.rows == other.rows


class Position:

    def __init__(self, row, column):
        self.row = row
        self.column = column


class InvalidUpdateRow(Exception):
    pass

class InvalidUpdateBoard(Exception):
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

    def test_update_row_with_X_should_not_be_equal_to_created_row(self):
        a_row = Row(2)
        a_row.put_mark_in_row(1, MarkX())
        self.assertNotEqual(Row(2), a_row)

    def test_should_raise_if_out_of_bounds(self):
        a_row = Row(1)
        with self.assertRaises(InvalidUpdateRow):
            a_row.put_mark_in_row(1, MarkX())

    def test_update_board_with_X_should_not_be_equal_to_created_board(self):
        a_board = Board(2)
        a_board.put_mark_in_board(Position(1, 0), MarkX())
        self.assertNotEqual(Board(2), a_board)

    def test_negative_position_in_row_should_raise(self):
        a_row = Row(1)
        with self.assertRaises(InvalidUpdateRow):
            a_row.put_mark_in_row(-1, MarkX())

    def test_x(self):
        a_row = Board(2)
        with self.assertRaises(InvalidUpdateRow):
            a_row.put_mark_in_board(Position(-1, 0), MarkX())