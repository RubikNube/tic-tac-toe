class Board:
    def __init__(self):
        self.fields = [None] * 9

    def __str__(self):
        return str(self.fields)

    def __repr__(self):
        return str(self.fields)

    def __getitem__(self, index):
        return self.fields[index]

    def __setitem__(self, index, value):
        self.fields[index] = value

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
        return [i for i, cell in enumerate(self.fields) if cell is None]

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
            if self.fields[i] == self.fields[i + 3] == self.fields[i + 6] is not None:
                return self.fields[i]
            if self.fields[i * 3] == self.fields[i * 3 + 1] == self.fields[i * 3 + 2] is not None:
                return self.fields[i * 3]
        if self.fields[0] == self.fields[4] == self.fields[8] is not None:
            return self.fields[0]
        if self.fields[2] == self.fields[4] == self.fields[6] is not None:
            return self.fields[2]
        return None

    def is_game_over(self):
        return self.is_full() or self.get_winner() is not None