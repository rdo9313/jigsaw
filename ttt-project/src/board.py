import os
from square import Square


class Board:
    def __init__(self, game, match):
        self._match = match
        board_id = len(game["boards"]) + 1
        self._id = board_id
        game["boards"][board_id] = self
        self.game = game
        self.initialize_squares()

    @property
    def match(self):
        return self._match

    @property
    def id(self):
        return self._id

    def possible_winning_rows(self):
        return [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9],
            [1, 5, 9],
            [3, 5, 7],
        ]

    def initialize_squares(self):
        for i in range(9):
            Square(self.game, self)

    def squares(self):
        return [
            square
            for square in self.game["squares"].values()
            if square.board.id == self.id
        ]

    def display(self):
        markers = [square.marker for square in self.squares()]
        print("")
        print("     |     |")
        print(f"  {markers[0]}  |  {markers[1]}  |  {markers[2]}")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {markers[3]}  |  {markers[4]}  |  {markers[5]}")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {markers[6]}  |  {markers[7]}  |  {markers[8]}")
        print("     |     |")
        print("")

    def display_with_clear(self):
        clear = lambda: os.system("clear")
        clear()
        print("")
        self.display()

    def is_full(self):
        return len(self.unused_squares()) == 0

    def find_square(self, square_id):
        return [square for square in self.squares() if square.id == square_id][0]

    def unused_squares(self):
        return [square for square in self.squares() if square.marker == " "]

    def update_square(self, square_id, marker):
        square = self.find_square(square_id)
        square.set_marker = marker

    def winner(self):
        for row in self.possible_winning_rows():
            squares = [square for square in self.squares() if square.id in row]
            if [square.marker for square in squares].count("X") == 3:
                return "Human"
            elif [square.marker for square in squares].count("O") == 3:
                return "Computer"

        return "Tie" if self.is_full() else "N/A"
