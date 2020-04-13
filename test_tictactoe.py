import unittest

class InvalidPlayPositionException(Exception):
    pass

class WrongPlayerException(Exception):
    pass

class Board():
    def __init__(self, size):
        self.size = size
        self.board = size * [ size * ['.']]
        self.next_player = 'X'

    def has_winner(self):
        if not self.size:
            return "Nobody"
        if len([x for x in self.board if x != '.']) == self.size:
            return "X"
        return "Nobody"

    def play(self, player, row, column):
        if player != self.next_player:
            raise WrongPlayerException
        if row >= self.size or column >= self.size:
            raise InvalidPlayPositionException
        if self.board[row][column] != '.':
            raise InvalidPlayPositionException
        self.board[row][column] = player

class TestTicTacToe(unittest.TestCase):

    @unittest.skip("a")
    def test_board_size_0_should_have_no_winner(self):
        a_board = Board(0)
        winner = a_board.has_winner()
        self.assertEqual("Nobody", winner)

    @unittest.skip("a")
    def test_board_size_1_should_have_X_winner(self):
        a_board = Board(1) # Arrange
        a_board.play("X", 0, 0) # arrange

        winner = a_board.has_winner() # act

        self.assertEqual("X", winner) # assert

    @unittest.skip("a")
    def test_board_size_2_should_have_no_winner(self):
        a_board = Board(2) # Arrange
        a_board.play("X", 0, 0) # arrange

        winner = a_board.has_winner() # act

        self.assertEqual("Nobody", winner) # assert

    def test_play_at_same_position_should_raise(self):
        a_board = Board(2)  # Arrange
        a_board.play("X", 0, 0)  # arrange
        with self.assertRaises(InvalidPlayPositionException): # assert
            a_board.play("X", 0, 0)  # act/assert

    def test_playing_on_empty_board_should_raise(self):
        a_board = Board(0)  # Arrange
        with self.assertRaises(InvalidPlayPositionException): # assert
            a_board.play("X", 0, 0)  # act/assert

    def test_playing_out_of_board_should_raise(self):
        a_board = Board(1)
        with self.assertRaises(InvalidPlayPositionException):
            a_board.play("X", 1, 0)

    def test_should_fail_if_O_starts(self):
        a_board = Board(1)
        with self.assertRaises(WrongPlayerException):
            a_board.play("O", 0, 0)