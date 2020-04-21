import unittest


class AliveCell:

    def __eq__(self, other):
        return type(self) == type(other)


class DeadCell:

    def __eq__(self, other):
        return type(self) == type(other)


class Position:

    def __init__(self, row, column):
        self.row = row
        self.column = column

class InvalidPosition(Exception):
    pass

class Grid:

    def __init__(self, number_rows, number_columns):
        self.number_columns = number_columns
        self.number_rows = number_rows
        self.rows = [number_rows * self._generate_dead_row()]

    def _generate_dead_row(self):
        return [DeadCell() for i in range(self.number_columns)]

    def seed(self, position):
        if position.row >= self.number_rows or position.column >= self.number_columns:
            raise InvalidPosition
        self.rows[position.row][position.column] = AliveCell()

    def __eq__(self, other):
        return self.rows == other.rows

    def is_dead(self, position):
        if len(self.rows) == 0:
            return True
        return self.rows[position.row][position.column] != AliveCell()


class TestGameOfLife(unittest.TestCase):

    def test_empty_grid_should_not_equal_grid_with_1_element(self):
        a_grid = Grid(1, 1)
        position = Position(0, 0)
        a_grid.seed(position)
        self.assertNotEqual(a_grid, Grid(1, 1))

    def test_cell_shouldnt_be_dead(self):
        a_grid = Grid(1, 1)
        self.assertTrue(a_grid.is_dead(Position(0, 0)))

    def test_grid_with_a_live_cell_at_0_0_should_not_be_dead(self):
        a_grid = Grid(1, 1)
        position = Position(0, 0)
        a_grid.seed(position)
        self.assertFalse(a_grid.is_dead(position))

    def test_cell_seeded_should_not_be_dead(self):
        a_grid = Grid(1, 2)
        position = Position(0, 1)
        a_grid.seed(position)
        self.assertFalse(a_grid.is_dead(position))

    def test_x(self):
        a_grid = Grid(1, 1)
        position = Position(0, 1)
        with self.assertRaises(InvalidPosition):
            a_grid.seed(position)

