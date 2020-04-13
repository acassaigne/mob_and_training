import unittest

class Board():
    def __init__(self, size):
        self.size = size

    def has_winner(self):
        return "Nobody"

    def play(self, player, row, column):
        pass

class TestTicTacToe(unittest.TestCase):

    def test_board_size_0_should_have_no_winner(self):
        a_board = Board(0)
        winner = a_board.has_winner()
        self.assertEqual("Nobody", winner)

    def test_board_size_1_should_have_no_winner(self):
        a_board = Board(1)
        a_board.play("X", 0, 0)
        winner = a_board.has_winner()
        self.assertEqual("X", winner)
