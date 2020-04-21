import unittest


class Cell:
    pass


class Position:

    def __init__(self, row, column):
        self.row = row
        self.column = column

class Grid:

    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.rows = []
        self.columns = []

    def seed(self, position):
        self.rows.append(Cell())

    def __eq__(self, other):
        return self.rows == other.rows

class TestGameOfLife(unittest.TestCase):

    def test_x(self):
        a_grid = Grid(1, 1)
        position = Position(0, 0)
        a_grid.seed(position)
        self.assertNotEqual(a_grid, Grid(1, 1))
