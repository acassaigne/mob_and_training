import unittest
from tictactoe_other import MarkO, MarkX, MarkEmpty, PlayerX, PlayerO, Draw, Nobody, Position, PositionAlreadyTaken, \
    InvalidPosition

class SetOfMarks:

    def __init__(self, length):
        self.values = [MarkEmpty() for i in range(0, length)]

    def __eq__(self, other):
        return self.values == other.values

    def put_mark(self, position, mark):
        if self.values[position] != MarkEmpty():
            raise PositionAlreadyTaken
        self.values[position] = mark

    def is_full_of_same_player_mark(self):
        if self.values[0] == MarkEmpty():
            return False
        return all([mark == self.values[0] for mark in self.values])

    def is_full_of_player_marks(self):
        return not any([MarkEmpty() == element for element in self.values])


class SetOfSetOfMarks:

    def __init__(self, length):
        self.set_of_marks = [SetOfMarks(length) for i in range(length)]

    def has_set_of_mark_full_of_same_player_mark(self):
        list_of_flags = [set_of_mark.is_full_of_same_player_mark() for set_of_mark in self.set_of_marks]
        return any(list_of_flags)

    def is_full_of_player_marks(self):
        return all([set_of_mark.is_full_of_player_marks() for set_of_mark in self.set_of_marks])


    def __eq__(self, other):
        return self.set_of_marks == other.set_of_marks

class Rows(SetOfSetOfMarks):

    def put_mark(self, position, mark):
        self.set_of_marks[position.row].put_mark(position.column, mark)

class Board:

    def __init__(self, board_size):
        self.board_size = board_size
        self.rows = Rows(board_size)
        self.columns = [SetOfMarks(self.board_size) for i in range(self.board_size)]
        self.positive_diagonal = SetOfMarks(self.board_size)
        self.negative_diagonal = SetOfMarks(self.board_size)

    def put_mark_in_board(self, position, mark):
        if self.is_out_of_board(position):
            raise InvalidPosition
        self.rows.put_mark(position, mark)
        self.columns[position.column].put_mark(position.row, mark)
        self.put_mark_in_diagonals(mark, position)

    def put_mark_in_diagonals(self, mark, position):
        if position.row == position.column:
            self.positive_diagonal.put_mark(position.row, mark)
        if position.row == (self.board_size - 1) - position.column:
            self.negative_diagonal.put_mark(position.row, mark)

    def is_out_of_board(self, position):
        return position.row < 0 or position.row >= self.board_size \
               or position.column < 0 or position.column >= self.board_size

    def has_full_row_2(self):
        return self.rows.has_set_of_mark_full_of_same_player_mark()

    def has_full_column(self):
        list_of_flags = [column.is_full_of_same_player_mark() for column in self.columns]
        return any(list_of_flags)

    def has_diagonal_full(self):
        return self._is_positive_diagonal_full() or self._is_negative_diagonal_full()

    def _is_positive_diagonal_full(self):
        return self.positive_diagonal.is_full_of_same_player_mark()

    def _is_negative_diagonal_full(self):
        return self.negative_diagonal.is_full_of_same_player_mark()

    def _is_full(self):
        return self.rows.is_full_of_player_marks()

    def __eq__(self, other):
        return self.rows == other.rows

class Game:

    def __init__(self, board_size = 3):
        self.board_size = board_size
        self.board = Board(self.board_size)
        self.current_player = PlayerX()

    def play(self, position):
        self.board.put_mark_in_board(position, self.current_player)
        self.switch_player()

    def switch_player(self):
        self.current_player = self._other_player()

    def _other_player(self):
        if self.current_player == PlayerO():
            return PlayerX()
        return PlayerO()

    def who_is_winner(self):
        if self.board.has_full_row_2() or self.board.has_full_column() or self.board.has_diagonal_full():
            return self._other_player()
        if self.board._is_full():
            return Draw()
        return Nobody()

    def get_current_player(self):
        return self.current_player


class TestTicTacToe(unittest.TestCase):

    def test_update_row_with_X_should_not_be_equal_to_created_row(self):
        a_set = SetOfMarks(2)
        a_set.put_mark(1, MarkX())
        self.assertNotEqual(SetOfMarks(2), a_set)


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
        self.assertEqual(PlayerX(), a_game.who_is_winner())

    def test_current_player_should_be_x_at_the_stat_of_the_game(self):
        a_game = Game(board_size=2)
        self.assertEqual(PlayerX(), a_game.get_current_player())

    def test_second_player_should_be_O(self):
        a_game = Game(board_size=2)
        a_game.play(Position(0, 0))
        self.assertEqual(PlayerO(), a_game.get_current_player())

    def test_playerO_and_playerX_cant_play_in_same_position(self):
        a_game = Game(board_size=2)
        initial_position = Position(0, 0)
        a_game.play(initial_position)
        with self.assertRaises(PositionAlreadyTaken):
            a_game.play(initial_position)

    def test_O_should_win_if_fills_row_number_1(self):
        a_game = Game(board_size=3)
        a_game.play(Position(0, 0))
        a_game.play(Position(1, 0))
        a_game.play(Position(0, 1))
        a_game.play(Position(1, 1))
        a_game.play(Position(2, 2))
        a_game.play(Position(1, 2))
        self.assertEqual(PlayerO(), a_game.who_is_winner())

    def test_X_should_win_if_fills_row_number_0(self):
        a_game = Game(board_size=3)
        a_game.play(Position(0, 0))
        a_game.play(Position(1, 0))
        a_game.play(Position(0, 1))
        a_game.play(Position(1, 1))
        a_game.play(Position(0, 2))
        self.assertEqual(PlayerX(), a_game.who_is_winner())

    def test_X_should_win_if_fills_column_number_0(self):
        a_game = Game(board_size=3)
        a_game.play(Position(0, 0))
        a_game.play(Position(0, 1))
        a_game.play(Position(1, 0))
        a_game.play(Position(1, 1))
        a_game.play(Position(2, 0))
        self.assertEqual(PlayerX(), a_game.who_is_winner())

    def test_nobody_should_be_return_when_no_satisfied_condition(self):
        a_game = Game(board_size=3)
        a_game.play(Position(0, 0))
        a_game.play(Position(0, 1))
        a_game.play(Position(1, 0))
        a_game.play(Position(1, 1))
        self.assertEqual(Nobody(), a_game.who_is_winner())

    def test_playerX_should_win_with_positive_diagonal(self):
        a_game = Game(board_size=3)
        a_game.play(Position(0, 0))
        a_game.play(Position(0, 1))
        a_game.play(Position(1, 1))
        a_game.play(Position(1, 2))
        a_game.play(Position(2, 2))
        self.assertEqual(PlayerX(), a_game.who_is_winner())

    def test_playerX_should_win_with_negative_diagonal(self):
        a_game = Game(board_size=3)
        a_game.play(Position(2, 0))
        a_game.play(Position(0, 1))
        a_game.play(Position(1, 1))
        a_game.play(Position(1, 2))
        a_game.play(Position(0, 2))
        self.assertEqual(PlayerX(), a_game.who_is_winner())

    def test_for_draw_game_should_return_draw_result(self):
        a_game = Game(board_size=3)
        a_game.play(Position(0, 0))
        a_game.play(Position(0, 1))
        a_game.play(Position(0, 2))
        a_game.play(Position(1, 0))
        a_game.play(Position(1, 1))
        a_game.play(Position(2, 0))
        a_game.play(Position(1, 2))
        a_game.play(Position(2, 2))
        a_game.play(Position(2, 1))
        self.assertEqual(Draw(), a_game.who_is_winner())