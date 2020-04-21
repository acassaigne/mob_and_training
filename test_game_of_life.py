import unittest


class AliveCell:
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
        self.rows = [[AliveCell()]]

    def __eq__(self, other):
        return self.rows == other.rows

    def is_dead(self, position):
        return True

class TestGameOfLife(unittest.TestCase):

    def test_empty_grid_should_not_equal_grid_with_1_element(self):
        a_grid = Grid(1, 1)
        position = Position(0, 0)
        a_grid.seed(position)
        self.assertNotEqual(a_grid, Grid(1, 1))

    def test_cell_shouldnt_be_dead(self):
        a_grid = Grid(1, 1)
        self.assertTrue(a_grid.is_dead(Position(0, 0)))

    def test_x(self):
        a_grid = Grid(1, 1)
        position = Position(0, 0)
        a_grid.seed(position)
        self.assertFalse(a_grid.is_dead(position))

