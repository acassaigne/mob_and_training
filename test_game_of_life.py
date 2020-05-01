import copy
import unittest

from game_of_life_grid import GridFactory, CellsRow, Grid
from game_of_life_position import Position, NeighbourPositionsGenerator, SetNeighbours, InvalidPosition


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
        neighbours_generator = NeighbourPositionsGenerator(p)
        neighbours = neighbours_generator.create(p)
        self.assertEqual(neighbours, SetNeighbours())

    def test_positions_around_0_0_with_0_1_boundaries_should_return_position_0_1(self):
        neighbours_generator = NeighbourPositionsGenerator(Position(0, 1))
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
        neighbours_generator = NeighbourPositionsGenerator(max_position=Position(1, 1))
        result = neighbours_generator.create(central_position=Position(0, 0))
        set_neighbours = SetNeighbours()
        set_neighbours.append(Position(0, 1))
        set_neighbours.append(Position(1, 0))
        set_neighbours.append(Position(1, 1))
        self.assertEqual(set_neighbours, result)

