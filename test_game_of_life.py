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

    def generate_corners(self, max_position):
        upper_left_corner = Position(max(self.row - 1, 0), max(self.column - 1, 0))
        lower_right_corner = Position(min(max_position.row, self.row + 1), min(max_position.column, self.column + 1))
        return upper_left_corner, lower_right_corner

    def add_position_to(self, list_positions, position):
        if self.row == position.row and self.column == position.column:
            return list_positions
        list_positions.append(position)
        return list_positions

    def generate_horizontal_positions_on_fixed_row(self, row, maximum_position):
        result = []
        upper_left_corner, lower_right_corner = self.generate_corners(maximum_position)
        for column in range(upper_left_corner.column, lower_right_corner.column + 1):
            result = self.add_position_to(result, Position(row, column))
        return result

    def generate_positions_around(self, maximum_position):
        result = []
        upper_left_corner, lower_right_corner = self.generate_corners(maximum_position)
        for row in range(upper_left_corner.row, lower_right_corner.row + 1):
            result += self.generate_horizontal_positions_on_fixed_row(row, maximum_position)
        return result

    def __eq__(self, other):
        return self.row == other.row and self.column == other.column 


class InvalidPosition(Exception):
    pass


class Grid:

    def __init__(self, number_rows, number_columns):
        self.number_columns = number_columns
        self.number_rows = number_rows
        self.rows = [self._generate_dead_row() for row in range(self.number_rows)]

    def _generate_dead_row(self):
        return [DeadCell() for i in range(self.number_columns)]

    def seed(self, position):
        self.raise_if_out_of_bounds(position)
        self.rows[position.row][position.column] = AliveCell()

    def __eq__(self, other):
        return self.rows == other.rows

    def is_dead(self, position):
        if len(self.rows) == 0:
            return True
        return self.rows[position.row][position.column] != AliveCell()

    def generate_neighbour_horizontal_index(self, position):
        horizontal_index = []
        if position.column < self.number_columns - 1:
            horizontal_index.append(position.column + 1)
        if position.column > 0:
            horizontal_index.append(position.column - 1)
        return horizontal_index

    def generate_neighbour_vertical_index(self, position):
        vertical_index = []
        if position.row < self.number_rows - 1:
            vertical_index.append(position.row + 1)
        if position.row > 0:
            vertical_index.append(position.row - 1)
        return vertical_index

    def count_alive_cells_around_horizontal(self, position):
        horizontal_index = self.generate_neighbour_horizontal_index(position)
        result = [self.rows[position.row][column] == AliveCell() for column in horizontal_index]
        return sum(result)

    def count_alive_cells_around_vertical(self, position):
        vertical_index = self.generate_neighbour_vertical_index(position)
        result = [self.rows[row][position.column] == AliveCell() for row in vertical_index]
        return sum(result)

    def count_alive_cells_around_in_diagonals(self, position):
        horizontal_index = self.generate_neighbour_horizontal_index(position)
        result = 0
        for column in horizontal_index:
            result += self.count_alive_cells_around_vertical(Position(position.row, column))
        return result

    def raise_if_out_of_bounds(self, position):
        if position.row >= self.number_rows or position.row < 0 or position.column >= self.number_columns\
                or position.column < 0:
            raise InvalidPosition

    def count_alive_cells_around(self, position):
        self.raise_if_out_of_bounds(position)
        return self.count_alive_cells_around_horizontal(position) + self.count_alive_cells_around_vertical(position) \
            + self.count_alive_cells_around_in_diagonals(position)


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
        position = Position(-1, 0)
        with self.assertRaises(InvalidPosition):
            a_grid.count_alive_cells_around(position)

    def test_count_alive_cell_around_cell_with_alive_cell_on_the_north_should_return_1(self):
        a_grid = Grid(2, 1)
        a_grid.seed(Position(0, 0))
        self.assertEqual(1, a_grid.count_alive_cells_around(Position(1, 0)))

    def test_rows_should_be_generated_as_lists_of_lists(self):
        a_grid = Grid(2, 2)
        self.assertEqual([[DeadCell(), DeadCell()],[DeadCell(), DeadCell()]], a_grid.rows)

    def test_should_count_alive_cell_in_diagonal(self):
        a_grid = Grid(2, 2)
        a_grid.seed(Position(row=0, column=0))
        self.assertEqual(1, a_grid.count_alive_cells_around(Position(row=1, column=1)))

    def test_seeded_grid_should_be_well_seeded(self):
        a_grid = Grid(2, 2)
        a_grid.seed(Position(row=0, column=1))
        self.assertEqual([[DeadCell(), AliveCell()], [DeadCell(), DeadCell()]], a_grid.rows)

    def test_positions_around_0_0_with_0_0_boundaries_should_return_empty_list(self):
        p = Position(0, 0)
        result = p.generate_positions_around(Position(0, 0))
        self.assertEqual([], result)

    def test_positions_around_0_0_with_0_1_boundaries_should_return_position_0_1(self):
        p = Position(0, 0)
        result = p.generate_positions_around(Position(0, 1))
        self.assertEqual([Position(0, 1)], result)

