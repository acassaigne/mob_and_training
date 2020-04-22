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
        if position.row >= self.number_rows or position.row < 0 or position.column >= self.number_columns or position.column < 0:
            raise InvalidPosition
        self.rows[position.row][position.column] = AliveCell()

    def __eq__(self, other):
        return self.rows == other.rows

    def is_dead(self, position):
        if len(self.rows) == 0:
            return True
        return self.rows[position.row][position.column] != AliveCell()

    def count_alive_cells_around(self, position):
        if position.row >= self.number_rows or position.row < 0 or position.column >= self.number_columns or position.column < 0:
            raise InvalidPosition
        horizontal_index = []
        if position.column < self.number_columns - 1:
            horizontal_index.append(position.column + 1)
        if position.column > 0:
            horizontal_index.append(position.column - 1)
        result = [self.rows[position.row][column] == AliveCell() for column in horizontal_index]
        vertical_index = []
        if position.row < self.number_rows - 1:
            vertical_index.append(position.row + 1)
        if position.row > 0:
            vertical_index.append(position.row - 1)
        result += [self.rows[row][position.column] == AliveCell() for row in vertical_index]
        return sum(result)


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

    def test_seeding_positive_out_of_board_should_raise_error(self):
        a_grid = Grid(1, 1)
        position = Position(0, 1)
        with self.assertRaises(InvalidPosition):
            a_grid.seed(position)

    def test_seeding_negative_out_of_board_should_raise_error(self):
        a_grid = Grid(1, 1)
        position = Position(-1, 0)
        with self.assertRaises(InvalidPosition):
            a_grid.seed(position)

    def test_unique_alive_cell_should_have_no_living_neighbour(self):
        a_grid = Grid(1, 2)
        position = Position(0, 0)
        a_grid.seed(position)
        self.assertEqual(0, a_grid.count_alive_cells_around(position))

    def test_count_alive_cell_around_cell_with_alive_cell_on_the_east_should_return_1(self):
        a_grid = Grid(1, 2)
        a_grid.seed(Position(0, 1))
        self.assertEqual(1, a_grid.count_alive_cells_around(Position(0, 0)))

    def test_count_alive_cell_around_cell_with_alive_cell_on_the_west_should_return_1(self):
        a_grid = Grid(1, 2)
        a_grid.seed(Position(0, 0))
        self.assertEqual(1, a_grid.count_alive_cells_around(Position(0, 1)))

    def test_negative_index_position_should_raise(self):
        a_grid = Grid(1, 2)
        position = Position(-1,0)
        with self.assertRaises(InvalidPosition):
            a_grid.count_alive_cells_around(position)

    def test_x(self):
        a_grid = Grid(2, 1)
        a_grid.seed(Position(0, 0))
        self.assertEqual(1, a_grid.count_alive_cells_around(Position(1, 0)))
