class Board:
    def __init__(self):
        self.fields = [" "] * 9

    def __str__(self):
        return str(self.fields)

    def __repr__(self):
        return (
            f" {self[7]} | {self[8]} | {self[9]} \n"
            f"-----------\n"
            f" {self[4]} | {self[5]} | {self[6]} \n"
            f"-----------\n"
            f" {self[1]} | {self[2]} | {self[3]} \n"
        )

    # used to access the board with board[1] instead of board.fields[0]
    def __getitem__(self, index):
        return self.fields[index - 1]

    # used to set the board with board[1] = "X" instead of board.fields[0] = "X"
    def __setitem__(self, index, value):
        self.fields[index - 1] = value

    def __len__(self):
        return len(self.fields)

    def __contains__(self, item):
        return item in self.fields

    def __eq__(self, other):
        return self.fields == other.fields

    def __ne__(self, other):
        return self.fields != other.fields

    def __hash__(self):
        return hash(tuple(self.fields))

    def __copy__(self):
        new_board = Board()
        new_board.fields = self.fields[:]
        return new_board

    def get_empty_cells(self):
        return [i + 1 for i, cell in enumerate(self.fields) if cell == " "]

    def get_empty_cells_count(self):
        return len(self.get_empty_cells())

    def is_full(self):
        return self.get_empty_cells_count() == 0

    def is_empty(self):
        return self.get_empty_cells_count() == 9

    def is_valid_move(self, move):
        return move in self.get_empty_cells()

    def get_winner(self):
        for i in range(3):
            if self.fields[i] == self.fields[i + 3] == self.fields[i + 6] != " ":
                return self.fields[i]
            if (
                self.fields[i * 3]
                == self.fields[i * 3 + 1]
                == self.fields[i * 3 + 2]
                != " "
            ):
                return self.fields[i * 3]
        if self.fields[0] == self.fields[4] == self.fields[8] != " ":
            return self.fields[0]
        if self.fields[2] == self.fields[4] == self.fields[6] != " ":
            return self.fields[2]
        return None

    def is_game_over(self):
        return self.is_full() or self.get_winner() != " "
