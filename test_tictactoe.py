import unittest


class InvalidPlayPositionException(Exception):
    pass


class WrongPlayerException(Exception):
    pass


class Board:
    def __init__(self, size):
        self.size = size
        self.board = [self.generate_row() for i in range(self.size)]
        self.next_player = 'X'

    def generate_row(self):
        return self.size * ['.']

    def has_winner(self):
        if not self.size:
            return "Nobody"
        if max(self.player_has_full_column(), self.player_has_full_row(), self.player_has_full_diagonal()):
            return self.other_player()
        return "Nobody"

    def player_has_full_row(self):
        player = self.other_player()
        for i in range(self.size):
            if self.board[i] == self.size * [player]:
                return True
        return False

    def player_has_full_diagonal(self):
        player = self.other_player()
        count_positive_diag = 0
        count_negative_diag = 0
        for i in range(self.size):
            if self.board[i][i] == player:
                count_positive_diag += 1
            if self.board[i][(self.size - 1) - i] == player:
                count_negative_diag += 1
        return max(count_positive_diag, count_negative_diag) == self.size

    def player_has_full_column(self):
        for column in range(self.size):
            if self.check_count_per_column(column):
                return True
        return False

    def check_count_per_column(self, column_number):
        player = self.other_player()
        count = 0
        for row in self.board:
            if row[column_number] == player:
                count += 1
        return count == self.size


    def _is_out_of_board(self, position):
        return position < 0 or position >= self.size

    def _is_taken_position(self, row, column):
        return not self.board[row][column] == '.'

    def _is_wrong_player(self, player):
        return player != self.next_player

    def _affect_position(self, player, row, column):
        self.board[row][column] = player

    def other_player(self):
        return 'O' if self.next_player == 'X' else 'X'

    def _switch_player(self):
        self.next_player = self.other_player()

    def play(self, player, row, column):
        if self._is_wrong_player(player):
            raise WrongPlayerException
        if self._is_out_of_board(row) or self._is_out_of_board(column):
            raise InvalidPlayPositionException
        if self._is_taken_position(row, column):
            raise InvalidPlayPositionException
        self._affect_position(player, row, column)
        self._switch_player()



class TestTicTacToe(unittest.TestCase):

    def test_board_size_0_should_have_no_winner(self):
        a_board = Board(0)
        winner = a_board.has_winner()
        self.assertEqual("Nobody", winner)

    def test_board_size_1_should_have_X_winner(self):
        a_board = Board(1)  # Arrange
        a_board.play("X", 0, 0)  # arrange

        winner = a_board.has_winner()  # act

        self.assertEqual("X", winner)  # assert


    def test_board_size_2_should_have_no_winner(self):
        a_board = Board(2)  # Arrange
        a_board.play("X", 0, 0)  # arrange

        winner = a_board.has_winner()  # act

        self.assertEqual("Nobody", winner)  # assert

    def test_play_at_same_position_should_raise(self):
        a_board = Board(2)  # Arrange
        a_board.play("X", 0, 0)  # arrange
        with self.assertRaises(InvalidPlayPositionException):  # assert
            a_board.play("O", 0, 0)  # act/assert

    def test_playing_on_empty_board_should_raise(self):
        a_board = Board(0)
        with self.assertRaises(InvalidPlayPositionException):
            a_board.play("X", 0, 0)

    def test_playing_out_of_board_should_raise(self):
        a_board = Board(1)
        with self.assertRaises(InvalidPlayPositionException):
            a_board.play("X", 1, 0)

    def test_should_raise_if_player_O_starts(self):
        a_board = Board(1)
        with self.assertRaises(WrongPlayerException):
            a_board.play("O", 0, 0)

    def test_should_raise_when_X_play_twice(self):
        a_board = Board(2)
        a_board.play("X", 0, 0)
        with self.assertRaises(WrongPlayerException):
            a_board.play("X", 1, 0)

    def test_should_raise_if_playing_in_negative_position(self):
        a_board = Board(1)
        with self.assertRaises(InvalidPlayPositionException):
            a_board.play("X", -1, 0)

    def test_O_should_win_if_column_1_full(self):
        a_board = Board(3)
        a_board.play("X", 0, 0)
        a_board.play("O", 1, 1)
        a_board.play("X", 0, 2)
        a_board.play("O", 0, 1)
        a_board.play("X", 2, 2)
        a_board.play("O", 2, 1)

        result = a_board.has_winner()

        self.assertEqual("O", result)

    def test_X_should_win_if_column_1_full(self):
        a_board = Board(3)
        a_board.play("X", 0, 1)
        a_board.play("O", 0, 0)
        a_board.play("X", 1, 1)
        a_board.play("O", 1, 0)
        a_board.play("X", 2, 1)

        result = a_board.has_winner()

        self.assertEqual("X", result)

    def test_X_should_win_if_column_0_full(self):
        a_board = Board(3)
        a_board.play("X", 0, 0)
        a_board.play("O", 0, 1)
        a_board.play("X", 1, 0)
        a_board.play("O", 1, 1)
        a_board.play("X", 2, 0)

        result = a_board.has_winner()

        self.assertEqual("X", result)

    def test_X_should_win_if_row_0_full(self):
        a_board = Board(3)
        a_board.play("X", 0, 0)
        a_board.play("O", 1, 1)
        a_board.play("X", 0, 1)
        a_board.play("O", 1, 2)
        a_board.play("X", 0, 2)

        result = a_board.has_winner()

    def test_X_should_win_if_row_1_full(self):
        a_board = Board(3)
        a_board.play("X", 1, 0)
        a_board.play("O", 0, 1)
        a_board.play("X", 1, 1)
        a_board.play("O", 0, 2)
        a_board.play("X", 1, 2)

        result = a_board.has_winner()

        self.assertEqual("X", result)

    def test_X_should_win_if_positive_diagonal_full(self):
        a_board = Board(3)
        a_board.play("X", 0, 0)
        a_board.play("O", 0, 1)
        a_board.play("X", 1, 1)
        a_board.play("O", 0, 2)
        a_board.play("X", 2, 2)

        result = a_board.has_winner()

        self.assertEqual("X", result)

    def test_X_should_win_if_negative_diagonal_full(self):
        a_board = Board(3)
        a_board.play("X", 0, 2)
        a_board.play("O", 0, 1)
        a_board.play("X", 1, 1)
        a_board.play("O", 1, 2)
        a_board.play("X", 2, 0)

        result = a_board.has_winner()

        self.assertEqual("X", result)