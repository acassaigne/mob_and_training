from game_of_life_cells import AliveCell, DeadCell
from game_of_life_position import Position, InvalidPosition, NeighbourPositionsGenerator


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
        neighbours_generator = NeighbourPositionsGenerator(self.max_position)
        neighbours = neighbours_generator.create(position)
        return len(self._list_alive_cells(neighbours))

    def _list_alive_cells(self, neighbours):
        return [neighbour for neighbour in neighbours if self.rows[neighbour.row].is_alive(neighbour.column)]

    def is_alive(self, position):
        return self.rows[position.row].is_alive(position.column)