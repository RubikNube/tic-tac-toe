import unittest
import sys

sys.path.insert(0, "../src")

from board import Board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_board_fields_are_initialized(self):
        self.assertEqual(
            self.board.fields, [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        )

    def test_str_for_initial_board(self):
        self.assertEqual(str(self.board), str([" "] * 9))

    def test_str_for_board_with_one_move(self):
        self.board[1] = "X"
        expected = ["X", " ", " ", " ", " ", " ", " ", " ", " "]
        self.assertEqual(str(self.board), str(expected))

    def test_str_for_board_with_two_moves(self):
        self.board[1] = "X"
        self.board[6] = "O"
        self.assertEqual(
            str(self.board), str(["X", " ", " ", " ", " ", "O", " ", " ", " "])
        )

    def test_repr(self):
        print("repr(self.board):")
        print(repr(self.board))
        expected = """   |   |   
-----------
   |   |   
-----------
   |   |   
"""
        print("expected:")
        print(expected)
        print("expected length:", len(expected))
        print("repr(self.board) length:", len(repr(self.board)))
        self.assertEqual(repr(self.board), expected)

    def test_getitem(self):
        self.assertEqual(self.board[1], " ")

    def test_setitem(self):
        self.board[1] = "X"
        self.assertEqual(self.board[1], "X")

    def test_len(self):
        self.assertEqual(len(self.board), 9)

    def test_contains(self):
        self.assertNotIn("X", self.board)

    def test_hash(self):
        self.assertEqual(hash(self.board), hash(tuple([" "] * 9)))

    def test_copy(self):
        self.board[1] = "X"
        board_copy = self.board.__copy__()
        self.assertEqual(board_copy[1], "X")

    def test_get_empty_cells(self):
        self.assertEqual(self.board.get_empty_cells(), [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_get_empty_cells_count(self):
        self.assertEqual(self.board.get_empty_cells_count(), 9)

    def test_is_full(self):
        self.assertFalse(self.board.is_full())

    def test_is_empty(self):
        self.assertTrue(self.board.is_empty())

    def test_is_valid_move(self):
        self.assertTrue(self.board.is_valid_move(0))

    def test_get_winner(self):
        self.assertIsNone(self.board.get_winner())

    if __name__ == "__main__":
        unittest.main()
