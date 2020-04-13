import unittest

class InvalidPlayPositionException(Exception):
    pass

class Board():
    def __init__(self, size):
        self.size = size
        self.board = size * size * ['.']

    def has_winner(self):
        if not self.size:
            return "Nobody"
        if len([x for x in self.board if x != '.']) == self.size:
            return "X"
        return "Nobody"

    def play(self, player, row, column):
        self.board.append("X")

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

    def test_board_y(self):
        a_board = Board(2)  # Arrange
        a_board.play("X", 0, 0)  # arrange
        with self.assertRaises(InvalidPlayPositionException): # assert
            a_board.play("X", 0, 0)  # act/assert
