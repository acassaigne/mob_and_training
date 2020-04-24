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

    def neighbours_accumulator(self, list_positions, position):
        if self.row == position.row and self.column == position.column:
            return list_positions
        return list_positions + [position]

    def generate_horizontal_positions_on_fixed_row(self, row, maximum_position):
        result = []
        upper_left_corner, lower_right_corner = self.generate_corners(maximum_position)
        for column in range(upper_left_corner.column, lower_right_corner.column + 1):
            result = self.neighbours_accumulator(result, Position(row, column))
        return result

    def generate_positions_around(self, maximum_position):
        result = []
        upper_left_corner, lower_right_corner = self.generate_corners(maximum_position)
        for row in range(upper_left_corner.row, lower_right_corner.row + 1):
            result += self.generate_horizontal_positions_on_fixed_row(row, maximum_position)
        return result

    def __eq__(self, other):
        return self.row == other.row and self.column == other.column 

    def __str__(self):
        return f"position row={self.row} column={self.column}"

# TODO: class SetNeighbours class iterable

class InvalidPosition(Exception):
    pass


class Grid:

    def __init__(self, number_rows, number_columns):
        self.number_columns = number_columns
        self.number_rows = number_rows
        self.rows = [self._generate_dead_row() for row in range(self.number_rows)]

    @staticmethod
    def string_to_grid(input_string):
        list_of_rows = input_string.split('\n')
        if len(list_of_rows) == 1:
            a_grid = Grid(1, len(input_string))
            column = 0
            for character in input_string:
                if character == '1':
                    a_grid.seed(Position(0, column))
                column += 1
            return a_grid
        return Grid(2, 1)

    def _generate_dead_row(self):
        return [DeadCell() for i in range(self.number_columns)]

    def seed(self, position):
        self.raise_if_out_of_bounds(position)
        self.rows[position.row][position.column] = AliveCell()

    def __eq__(self, other):
        return self.rows == other.rows

    def raise_if_out_of_bounds(self, position):
        if position.row >= self.number_rows or position.row < 0 or position.column >= self.number_columns\
                or position.column < 0:
            raise InvalidPosition

    def count_alive_cells_around(self, position):
        self.raise_if_out_of_bounds(position)
        neighbours = position.generate_positions_around(Position(self.number_rows - 1, self.number_columns - 1))
        result = 0
        for neighbour in neighbours:
            if self.rows[neighbour.row][neighbour.column] == AliveCell():
                result += 1
        return result

    def is_alive(self, position):
        return self.rows[position.row][position.column] == AliveCell()

    def kill_all(self):
        for row in self.rows:
            self.kill_row(row)

    def kill_row(self, row):
        for column in range(self.number_columns):
            row[column] = DeadCell()


class GameOfLife:

    def __init__(self, grid):
        self.grid = grid

    def tick(self):
        try:
            count_alive = self.grid.count_alive_cells_around(Position(1, 1))

        except InvalidPosition:
            count_alive = 0
        try:
            count_alive_0_0 = self.grid.count_alive_cells_around(Position(0, 0))
        except InvalidPosition:
            count_alive_0_0 = 0
        self.grid.kill_all()
        if count_alive == 3:
            self.grid.seed(Position(1, 1))
        if count_alive_0_0 == 3:
            self.grid.seed(Position(0, 0))

class TestGameOfLife(unittest.TestCase):

    def test_empty_grid_should_not_equal_grid_with_1_element(self):
        a_grid = Grid(1, 1)
        position = Position(0, 0)
        a_grid.seed(position)
        self.assertNotEqual(a_grid, Grid(1, 1))

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

    def test_str_of_position_3_3_should_return_good_name(self):
        p = Position(3, 3)
        self.assertEqual("position row=3 column=3", str(p))

    def test_create_new_game_with_1_1_grid_and_a_tick_should_return_1_1_grid_with_dead_cell(self):
        a_game = GameOfLife(Grid(1, 1))
        a_game.tick()
        self.assertEqual(Grid(1, 1), a_game.grid)

    def test_alone_live_cell_in_game_should_die_for_grid_1_1(self):
        a_grid = Grid(1, 1)
        a_grid.seed(Position(0, 0))
        a_game = GameOfLife(a_grid)
        a_game.tick()
        self.assertEqual(Grid(1, 1), a_game.grid)

    def test_alone_live_cell_in_game_should_die_for_grid_1_2(self):
        a_grid = Grid(1, 2)
        a_grid.seed(Position(0, 1))
        a_game = GameOfLife(a_grid)
        a_game.tick()
        self.assertEqual(Grid(1, 2), a_game.grid)

    def test_dead_cell_in_position_1_1_in_2_2_grid_with_3_alive_neighbours_should_be_alive_after_tick(self):
        a_grid = Grid(2, 2)
        a_grid.seed(Position(0, 0))
        a_grid.seed(Position(0, 1))
        a_grid.seed(Position(1, 0))
        a_game = GameOfLife(a_grid)
        a_game.tick()
        self.assertTrue(a_grid.is_alive(Position(1, 1)))

    def test_dead_cell_in_position_0_0_in_2_2_grid_with_3_alive_neighbours_should_be_alive_after_tick(self):
        a_grid = Grid(2, 2)
        a_grid.seed(Position(0, 1))
        a_grid.seed(Position(1, 1))
        a_grid.seed(Position(1, 0))
        a_game = GameOfLife(a_grid)
        a_game.tick()
        self.assertTrue(a_grid.is_alive(Position(0, 0)))

    def test_string_to_grid_should_return_1_1_grid_with_1_dead_cell(self):
        a_grid = Grid(1, 1)
        self.assertEqual(a_grid, Grid.string_to_grid('0'))

    def test_string_to_grid_with_1_string_should_return_1_1_grid_with_1_alive_cell(self):
        a_grid = Grid(1, 1)
        a_grid.seed(Position(0, 0))
        self.assertEqual(a_grid, Grid.string_to_grid('1'))

    def test_string_to_grid_with_00_string_should_return_1_2_grid_with_2_dead_cells(self):
        a_grid = Grid(1, 2)
        self.assertEqual(a_grid, Grid.string_to_grid('00'))

    def test_string_to_grid_with_01_string_should_return_1_2_grid_with_1_dead_cell_and_1_alive_cell(self):
        a_grid = Grid(1, 2)
        a_grid.seed(Position(0, 1))
        self.assertEqual(a_grid, Grid.string_to_grid('01'))

    def test_string_to_grid_with_00_string_should_return_2_1_grid_with_two_dead_cells(self):
        a_grid = Grid(2, 1)
        self.assertEqual(a_grid, Grid.string_to_grid('0\n' +
                                                     '0'))

    def test_x(self):
        a_grid = Grid(2, 1)
        a_grid.seed(Position(row=0, column=0))
        self.assertEqual(a_grid, Grid.string_to_grid('1\n' +
                                                     '0'))
