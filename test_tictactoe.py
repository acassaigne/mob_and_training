import unittest

class TestRomanNumber(unittest.TestCase):

    def test_x(self):
        a_board = board(2)
        winner = board.has_winner()
        self.assertIsNone(winner)
