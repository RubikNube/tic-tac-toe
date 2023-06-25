import unittest
import sys

sys.path.insert(0, "../src")

from board import Board


class TestBoard(unittest.TestCase):
    def test_board_fields_are_initialized(self):
        board = Board()
        self.assertEqual(board.fields, [None] * 9)

    def test_str_for_initial_board(self):
        board = Board()
        self.assertEqual(str(board), str([None] * 9))

    def test_str_for_board_with_one_move(self):
        board = Board()
        board[0] = "X"
        self.assertEqual(
            str(board), str(["X", None, None, None, None, None, None, None, None])
        )

    def test_str_for_board_with_two_moves(self):
        board = Board()
        board[0] = "X"
        board[5] = "O"
        self.assertEqual(
            str(board), str(["X", None, None, None, None, "O", None, None, None])
        )

    def test_repr(self):
        board = Board()
        self.assertEqual(
            repr(board), "[None, None, None, None, None, None, None, None, None]"
        )

    def test_getitem(self):
        board = Board()
        self.assertEqual(board[0], None)

    def test_setitem(self):
        board = Board()
        board[0] = "X"
        self.assertEqual(board[0], "X")

    def test_len(self):
        board = Board()
        self.assertEqual(len(board), 9)

    def test_contains(self):
        board = Board()
        self.assertNotIn("X", board)

    def test_hash(self):
        board = Board()
        self.assertEqual(hash(board), hash(tuple([None] * 9)))

    def test_copy(self):
        board = Board()
        board[0] = "X"
        board_copy = board.__copy__()
        self.assertEqual(board_copy[0], "X")

    def test_get_empty_cells(self):
        board = Board()
        self.assertEqual(board.get_empty_cells(), [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_get_empty_cells_count(self):
        board = Board()
        self.assertEqual(board.get_empty_cells_count(), 9)

    def test_is_full(self):
        board = Board()
        self.assertFalse(board.is_full())

    def test_is_empty(self):
        board = Board()
        self.assertTrue(board.is_empty())

    def test_is_valid_move(self):
        board = Board()
        self.assertTrue(board.is_valid_move(0))

    def test_get_winner(self):
        board = Board()
        self.assertIsNone(board.get_winner())

    if __name__ == "__main__":
        unittest.main()
