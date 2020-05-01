class Position:

    def __init__(self, row, column):
        self.row = row
        self.column = column

    def __eq__(self, other):
        return self.row == other.row and self.column == other.column

    def __str__(self):
        return f"position row={self.row} column={self.column}"


class NeighbourPositionsGenerator:

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