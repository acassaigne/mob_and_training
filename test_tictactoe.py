import unittest

class InvalidPlayPositionException(Exception):
    pass

class WrongPlayerException(Exception):
    pass

class Board():
    def __init__(self, size):
        self.size = size
        self.board = [self.generate_row() for i in range(self.size)]
        self.next_player = 'X'

    def generate_row(self):
        return self.size*['.']

    def has_winner(self):
        if not self.size:
            return "Nobody"
        if self.count_character("X") == self.size:
            return "X"
        return "Nobody"

    def _is_out_of_board(self, position):
        return position < 0 or position >= self.size

    def _is_taken_position(self, row, column):
        return not self.board[row][column] == '.'

    def _is_wrong_player(self, player):
        return player != self.next_player

    def _affect_position(self, player, row, column):
        self.board[row][column] = player

    def _switch_player(self):
        self.next_player = 'O' if self.next_player == 'X' else 'X'

    def play(self, player, row, column):
        if self._is_wrong_player(player):
            raise WrongPlayerException
        if self._is_out_of_board(row) or self._is_out_of_board(column):
            raise InvalidPlayPositionException
        if self._is_taken_position(row, column):
            raise InvalidPlayPositionException
        self._affect_position(player, row, column)
        self._switch_player()

    def count_character(self, character):
        counter = 0
        for row in range(self.size):
            for column in range(self.size):
                if self.board[row][column] == character:
                    counter += 1
        return counter



class TestTicTacToe(unittest.TestCase):


    def test_board_size_0_should_have_no_winner(self):
        a_board = Board(0)
        winner = a_board.has_winner()
        self.assertEqual("Nobody", winner)

    def test_board_size_1_should_have_X_winner(self):
        a_board = Board(1) # Arrange
        a_board.play("X", 0, 0) # arrange

        winner = a_board.has_winner() # act

        self.assertEqual("X", winner) # assert

    def test_counter_should_return_1(self):
        a_board = Board(2) # Arrange
        a_board.play("X", 0, 0) # arrange

        number = a_board.count_character('X') # act

        self.assertEqual(1, number) # assert

    def test_board_size_2_should_have_no_winner(self):
        a_board = Board(2) # Arrange
        a_board.play("X", 0, 0) # arrange

        winner = a_board.has_winner() # act

        self.assertEqual("Nobody", winner) # assert

    def test_play_at_same_position_should_raise(self):
        a_board = Board(2)  # Arrange
        a_board.play("X", 0, 0)  # arrange
        with self.assertRaises(InvalidPlayPositionException): # assert
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

    def test_x(self):
        a_board = Board(3)
        a_board.play("X", 0, 0)
        a_board.play("O", 1, 1)
        a_board.play("X", 0, 2)
        a_board.play("O", 0, 1)
        a_board.play("X", 2, 2)

        result = a_board.has_winner()

        self.assertEqual("Nobody", result)

