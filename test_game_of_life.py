import copy
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

    def __eq__(self, other):
        return self.row == other.row and self.column == other.column 

    def __str__(self):
        return f"position row={self.row} column={self.column}"


class NeighboursGenerator:

    def __init__(self, max_position):
        self.maximum_position = max_position
        self.neighbours = None
        self.upper_left_corner = None
        self.lower_right_corner = None
        self.central_position = None

    def _initialize_from_central_position(self, central_position):
        self.central_position = central_position
        self.neighbours = SetNeighbours()
        self.generate_corners()

    def create(self, central_position):
        self._initialize_from_central_position(central_position)
        for row in range(self.upper_left_corner.row, self.lower_right_corner.row + 1):
            self.generate_horizontal_positions_on_fixed_row(row)
        return self.neighbours

    def generate_corners(self):
        self.upper_left_corner = Position(max(self.central_position.row - 1, 0), max(self.central_position.column - 1, 0))
        self.lower_right_corner = Position(min(self.maximum_position.row, self.central_position.row + 1),
                                           min(self.maximum_position.column, self.central_position.column + 1))

    def neighbours_accumulator(self, neighbour_position):
        if self.central_position != neighbour_position:
            self.neighbours.append(neighbour_position)

    def generate_horizontal_positions_on_fixed_row(self, row):
        for column in range(self.upper_left_corner.column, self.lower_right_corner.column + 1):
            self.neighbours_accumulator(Position(row, column))


class SetNeighbours:

    def __init__(self):
        self.positions = []

    def append(self, position):
        self.positions.append(position)

    def __eq__(self, other):
        return self.sorted() == other.sorted()

    def sorted(self):
        return sorted(self.positions, key=lambda position: str(position))

    def __iter__(self):
        for position in self.positions:
            yield position


class InvalidPosition(Exception):
    pass


class GridFactory:

    def __init__(self):
        self.input_string = None
        self.list_of_rows = None
        self.grid = None

    def extract_dimensions(self, input_string):
        self.input_string = input_string
        self.list_of_rows = input_string.split("\n")
        self.grid = Grid(len(self.list_of_rows), len(self.list_of_rows[0]))

    def create(self, input_string):
        self.extract_dimensions(input_string)
        row_number = 0
        for row_string in self.list_of_rows:
            self.seed_row(row_number, row_string)
            row_number += 1
        return self.grid

    def seed_row(self, row_number, row_string):
        column_number = 0
        for cell_string in row_string:
            if cell_string == '1':
                self.grid.seed(Position(row_number, column_number))
            column_number += 1


class CellsRow:

    def __init__(self, number_columns):
        self.number_columns = number_columns
        self.cells = self._generate_dead_row()

    def __eq__(self, other):
        return self.cells == other.cells

    def __str__(self):
        result = ""
        for cell in self.cells:
            result += "1" if cell == AliveCell() else "0"
        return result

    def seed(self, cell_index):
        self.cells[cell_index] = AliveCell()

    def kill(self, cell_index):
        self.cells[cell_index] = DeadCell()

    def is_alive(self, cell_index):
        return self.cells[cell_index] == AliveCell()

    def _generate_dead_row(self):
        return [DeadCell() for i in range(self.number_columns)]


class Grid:

    def __init__(self, number_rows, number_columns):
        self.number_columns = number_columns
        self.number_rows = number_rows
        self.rows = [CellsRow(number_columns) for row in range(self.number_rows)]
        self.max_position = Position(number_rows - 1, number_columns - 1)

    def __str__(self):
        result = ""
        for row in self.rows:
            result += str(row) + "\n"
        return result

    def _generate_dead_row(self):
        return [DeadCell() for i in range(self.number_columns)]

    def seed(self, position):
        self.raise_if_out_of_bounds(position)
        self.rows[position.row].seed(position.column)

    def kill(self, position):
        self.raise_if_out_of_bounds(position)
        self.rows[position.row].kill(position.column)

    def __eq__(self, other):
        return self.rows == other.rows

    def raise_if_out_of_bounds(self, position):
        if position.row >= self.number_rows or position.row < 0 or position.column >= self.number_columns\
                or position.column < 0:
            raise InvalidPosition

    def count_alive_cells_around(self, position):
        self.raise_if_out_of_bounds(position)
        neighbours_generator = NeighboursGenerator(self.max_position)
        neighbours = neighbours_generator.create(position)
        result = 0
        for neighbour in neighbours:
            if self.rows[neighbour.row].is_alive(neighbour.column):
                result += 1
        return result

    def is_alive(self, position):
        return self.rows[position.row].is_alive(position.column)


class GameOfLife:

    def __init__(self, grid):
        self.grid = grid
        self.new_grid = None

    def tick(self):
        self.new_grid = copy.deepcopy(self.grid)
        for index_row in range(self.grid.number_rows):
            self.tick_on_row(index_row)
        self.grid = self.new_grid

    def tick_on_row(self, index_row):
        for index_column in range(self.grid.number_columns):
            position = Position(row=index_row, column=index_column)
            count_alive = self.grid.count_alive_cells_around(position)
            self.birth_cell_at(count_alive, position)
            self.death_cell_at(count_alive, position)

    def death_cell_at(self, count_alive, position):
        if count_alive < 2 or count_alive > 3:
            self.new_grid.kill(position)

    def birth_cell_at(self, count_alive, position):
        if count_alive == 3:
            self.new_grid.seed(position)


class TestGameOfLife(unittest.TestCase):

    def initialize_grid_factory(self):
        self.factory = GridFactory()

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
        a_dead_row = CellsRow(2)
        self.assertEqual([a_dead_row, a_dead_row], a_grid.rows)

    def test_should_count_alive_cell_in_diagonal(self):
        a_grid = Grid(2, 2)
        a_grid.seed(Position(row=0, column=0))
        self.assertEqual(1, a_grid.count_alive_cells_around(Position(row=1, column=1)))

    def test_seeded_grid_should_be_well_seeded(self):
        a_grid = Grid(2, 2)
        a_row = CellsRow(2)
        a_row.seed(cell_index=1)
        a_dead_row = CellsRow(2)

        a_grid.seed(Position(row=0, column=1))

        self.assertEqual([a_row, a_dead_row], a_grid.rows)

    def test_positions_around_0_0_with_0_0_boundaries_should_return_empty_list(self):
        p = Position(0, 0)
        neighbours_generator = NeighboursGenerator(p)
        neighbours = neighbours_generator.create(p)
        self.assertEqual(neighbours, SetNeighbours())

    def test_positions_around_0_0_with_0_1_boundaries_should_return_position_0_1(self):
        neighbours_generator = NeighboursGenerator(Position(0, 1))
        neighbours = neighbours_generator.create(Position(0, 0))
        expected = SetNeighbours()
        expected.append(Position(0, 1))
        self.assertEqual(expected, neighbours)

    def test_str_of_position_3_3_should_return_good_name(self):
        p = Position(3, 3)
        self.assertEqual("position row=3 column=3", str(p))

    def test_create_new_game_with_1_1_grid_and_a_tick_should_return_1_1_grid_with_dead_cell(self):
        a_game = GameOfLife(Grid(1, 1))
        a_game.tick()
        self.assertEqual(Grid(1, 1), a_game.grid)

    def test_alone_live_cell_in_game_should_die_for_grid_1_1(self):
        factory = GridFactory()
        a_grid = factory.create("1")
        a_full_dead_grid = factory.create("0")
        a_game = GameOfLife(a_grid)
        a_game.tick()
        self.assertEqual(a_full_dead_grid, a_game.grid)

    def test_alone_live_cell_in_game_should_die_for_grid_1_2(self):
        factory = GridFactory()
        a_grid = factory.create("01")
        a_full_dead_grid = factory.create("00")
        a_game = GameOfLife(a_grid)
        a_game.tick()
        self.assertEqual(a_full_dead_grid, a_game.grid)


    def test_string_to_grid_should_return_1_1_grid_with_1_dead_cell(self):
        a_grid = Grid(1, 1)
        self.initialize_grid_factory()
        self.assertEqual(a_grid, self.factory.create('0'))

    def test_string_to_grid_with_1_string_should_return_1_1_grid_with_1_alive_cell(self):
        a_grid_expected = Grid(1, 1)
        a_grid_expected.seed(Position(0, 0))
        self.initialize_grid_factory()
        self.assertEqual(a_grid_expected, self.factory.create('1'))

    def test_string_to_grid_with_00_string_should_return_1_2_grid_with_2_dead_cells(self):
        a_grid = Grid(1, 2)
        self.initialize_grid_factory()
        self.assertEqual(a_grid, self.factory.create('00'))

    def test_string_to_grid_with_01_string_should_return_1_2_grid_with_1_dead_cell_and_1_alive_cell(self):
        a_grid = Grid(1, 2)
        a_grid.seed(Position(0, 1))
        self.initialize_grid_factory()
        self.assertEqual(a_grid, self.factory.create('01'))

    def test_string_to_grid_with_00_string_should_return_2_1_grid_with_two_dead_cells(self):
        a_grid = Grid(2, 1)
        self.initialize_grid_factory()
        self.assertEqual(a_grid, self.factory.create('0\n' +
                                                     '0'))

    def test_string_to_grid_with_two_rows_1_newline_0_string_should_return_2_1_grid_with_one_alive_at_position_0_0_and_one_dead(self):
        a_grid = Grid(2, 1)
        a_grid.seed(Position(row=0, column=0))
        self.initialize_grid_factory()
        self.assertEqual(a_grid, self.factory.create('1\n' +
                                                     '0'))

    def test_facory_created_grid_should_be_equal_to_seeded_grid(self):
        self.initialize_grid_factory()
        a_grid_2 = self.factory.create("11\n" +
                                       "10")
        a_grid = Grid(2, 2)
        a_grid.seed(Position(0, 0))
        a_grid.seed(Position(0, 1))
        a_grid.seed(Position(1, 0))
        expected = str(a_grid)
        self.assertEqual(expected, str(a_grid_2))

    def test_dead_cell_in_position_0_1_in_2_2_grid_with_3_alive_neighbours_should_be_alive_after_tick(self):
        self.initialize_grid_factory()
        a_grid = self.factory.create("10\n" +
                                     "11")
        a_game = GameOfLife(a_grid)
        a_game.tick()
        self.assertTrue(a_game.grid.is_alive(Position(0, 1)))

    def test_dead_cell_in_position_1_1_in_2_2_grid_with_3_alive_neighbours_should_be_alive_after_tick(self):
        self.initialize_grid_factory()
        a_grid = self.factory.create("11\n" +
                                     "10")
        a_game = GameOfLife(a_grid)
        a_game.tick()
        self.assertTrue(a_game.grid.is_alive(Position(1, 1)))

    def test_dead_cell_in_position_0_0_in_2_2_grid_with_3_alive_neighbours_should_be_alive_after_tick(self):
        self.initialize_grid_factory()
        a_grid = self.factory.create("01\n" +
                                     "11")
        expected_grid = self.factory.create("11\n" + \
                                        "11")
        a_game = GameOfLife(a_grid)
        a_game.tick()

        self.assertEqual(expected_grid, a_game.grid)

    def test_alive_cell_between_more_than_3_live_cell_should_die(self):
        self.initialize_grid_factory()
        a_grid = self.factory.create("111\n" +
                                     "111")
        expected_grid = self.factory.create("101\n" + \
                                            "101")
        a_game = GameOfLife(a_grid)
        a_game.tick()

        self.assertEqual(str(expected_grid), str(a_game.grid))

    def test_neighbours_generator_with_central_position_0_0_should_return_three_neighbours_for_max_position_1_1(self):
        neighbours_generator = NeighboursGenerator(max_position=Position(1,1))
        result = neighbours_generator.create(central_position=Position(0,0))
        set_neighbours = SetNeighbours()
        set_neighbours.append(Position(0, 1))
        set_neighbours.append(Position(1, 0))
        set_neighbours.append(Position(1, 1))
        self.assertEqual(set_neighbours, result)

