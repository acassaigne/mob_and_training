import unittest

class Row:

    def __init__(self, length):
        self.values = length*[MarkEmpty()]

    def __eq__(self, other):
        return self.values == other.values

    def put_mark_in_row(self, position, character):
        if self.values[position] != MarkEmpty():
            raise PositionAlreadyTaken
        self.values[position] = character


class Board:

    def __init__(self, length):
        self.length = length
        self.rows = self.length * [Row(self.length)]

    def put_mark_in_board(self, position, mark):
        if self.is_out_of_board(position):
            raise InvalidPosition
        self.rows[position.row].put_mark_in_row(position.column, mark)

    def is_out_of_board(self, position):
        return position.row < 0 or position.row >= self.length \
               or position.column < 0 or position.column >= self.length

    def __eq__(self, other):
        return self.rows == other.rows


class Position:

    def __init__(self, row, column):
        self.row = row
        self.column = column

class PositionAlreadyTaken(Exception):
    pass

class InvalidPosition(Exception):
    pass

class Mark:
    def __eq__(self, other):
        return type(self) == type(other)


class MarkEmpty(Mark):
    pass


class MarkX(Mark):
    pass


class MarkO(Mark):
    pass


class Player:
    def __eq__(self, other):
        return type(self) == type(other)


class PlayerO(Player):
    pass


class PlayerX(Player):
    pass


class Game:

    def __init__(self, board_size = 3):
        self.board_size = board_size
        self.board = Board(self.board_size)
        self.current_player = PlayerX()

    def play(self, position):
        self.switch_player()

    def switch_player(self):
        if self.current_player == PlayerO():
            self.current_player = PlayerX()
        self.current_player = PlayerO()

    def has_winner(self):
        return PlayerX()

    def get_current_player(self):
        return self.current_player


class TestTicTacToe(unittest.TestCase):

    def test_update_row_with_X_should_not_be_equal_to_created_row(self):
        a_row = Row(2)
        a_row.put_mark_in_row(1, MarkX())
        self.assertNotEqual(Row(2), a_row)


    def test_update_board_with_X_should_not_be_equal_to_created_board(self):
        a_board = Board(2)
        a_board.put_mark_in_board(Position(1, 0), MarkX())
        self.assertNotEqual(Board(2), a_board)

    def test_negative_column_number_should_raise_error(self):
        a_row = Board(1)
        with self.assertRaises(InvalidPosition):
            a_row.put_mark_in_board(Position(0, -1), MarkX())

    def test_negative_row_number_should_raise_error(self):
        a_row = Board(2)
        with self.assertRaises(InvalidPosition):
            a_row.put_mark_in_board(Position(-1, 0), MarkX())

    def test_already_taken_position_should_raise(self):
        a_row = Board(2)
        a_row.put_mark_in_board(Position(1, 0), MarkX())
        with self.assertRaises(PositionAlreadyTaken):
            a_row.put_mark_in_board(Position(1, 0), MarkO())

    def test_game_with_size_board_to_one_should_has_player_x_as_winner(self):
        a_game = Game(board_size=1)
        a_game.play(Position(0, 0))
        self.assertEqual(PlayerX(), a_game.has_winner())

    def test_current_player_should_be_x_at_the_stat_of_the_game(self):
        a_game = Game(board_size=2)
        self.assertEqual(PlayerX(), a_game.get_current_player())

    def test_second_player_should_be_O(self):
        a_game = Game(board_size=2)
        a_game.play(Position(0, 0))
        self.assertEqual(PlayerO(), a_game.get_current_player())

    def test_x(self):
        a_game = Game(board_size=2)
        a_game.play(Position(0, 0))
        self.assertEqual(PlayerO(), a_game.get_current_player())
