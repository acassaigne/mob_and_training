import unittest

class Board():
    def __init__(self, size):
        self.size = size
        self.board = []

    def has_winner(self):
        if not self.size:
            return "Nobody"
        if len(self.board) == self.size:
            return "X"
        return "Nobody"

    def play(self, player, row, column):
        self.board.append("X")

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

    def test_board_size_2_should_have_no_winner(self):
        a_board = Board(2) # Arrange
        a_board.play("X", 0, 0) # arrange

        winner = a_board.has_winner() # act

        self.assertEqual("Nobody", winner) # assert
