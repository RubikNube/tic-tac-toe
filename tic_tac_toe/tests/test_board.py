import unittest
import sys

# Add the tic_tac_toe/src directory to the path so that we can import the board module
sys.path.insert(0, "../src")
from board import Board  # noqa: E402


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_dummy_false(self):
        self.assertFalse(True)

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

    def test_repr_for_empty_board(self):
        expected = (
            "   |   |   \n"
            "-----------\n"
            "   |   |   \n"
            "-----------\n"
            "   |   |   \n"
        )

        self.assertEqual(repr(self.board), expected)

    def test_repr_for_full_board(self):
        for i in range(1, 10):
            if i % 2 == 0:
                self.board[i] = "X"
            else:
                self.board[i] = "O"

        expected = (
            " O | X | O \n"
            "-----------\n"
            " X | O | X \n"
            "-----------\n"
            " O | X | O \n"
        )

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

    def test_get_empty_cells_for_empty_board(self):
        self.assertEqual(self.board.get_empty_cells(), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_get_empty_cells_count(self):
        self.assertEqual(self.board.get_empty_cells_count(), 9)

    def test_is_full_for_empty_board(self):
        self.assertFalse(self.board.is_full())

    def test_is_full_for_full_board(self):
        self.board.fields = ["X"] * 9
        self.assertTrue(self.board.is_full())

    def test_is_empty_for_empty_board(self):
        self.assertTrue(self.board.is_empty())

    def test_is_empty_for_full_board(self):
        self.board.fields = ["X"] * 9
        self.assertFalse(self.board.is_empty())

    def test_is_valid_move_for_coordinate_0_is_false(self):
        self.assertFalse(self.board.is_valid_move(0))

    def test_is_valid_move_for_coordinate_1_to_9_is_true(self):
        for i in range(1, 10):
            self.assertTrue(self.board.is_valid_move(i))

    def test_is_valid_move_for_coordinate_10_is_false(self):
        self.assertFalse(self.board.is_valid_move(10))

    def test_get_winner_for_empty_board_is_none(self):
        self.assertIsNone(self.board.get_winner())

    def test_get_winner_for_full_board_with_no_winner_is_none(self):
        self.board.fields = ["X", "O", "X", "X", "O", "O", "O", "X", "X"]

        self.assertIsNone(self.board.get_winner())

    def test_get_winner_for_horizontal_win_is_x(self):
        self.board[1] = self.board[2] = self.board[3] = "X"
        self.assertEqual(self.board.get_winner(), "X")

    def test_get_winner_for_horizontal_win_is_o(self):
        self.board[1] = self.board[2] = self.board[3] = "O"
        self.assertEqual(self.board.get_winner(), "O")

    def test_get_winner_for_vertical_win_is_x(self):
        self.board[1] = self.board[4] = self.board[7] = "X"
        self.assertEqual(self.board.get_winner(), "X")

    def test_get_winner_for_diagonal_win_is_x(self):
        self.board[1] = self.board[5] = self.board[9] = "X"
        self.assertEqual(self.board.get_winner(), "X")

    if __name__ == "__main__":
        unittest.main()
