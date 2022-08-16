import os


class Match:
    def __init__(self, game, first_player="X"):
        match_id = len(game["matches"]) + 1
        self.id = match_id
        game["matches"][match_id] = self
        self.first_player = first_player
        self.game = game

    def play(self):
        self.display_welcome_message()
        self.play_match()
        self.display_match_results()
        self.display_goodbye_message()

    def display_welcome_message(self):
        clear = lambda: os.system("clear")
        clear()
        print("Welcome to Tic Tac Toe!")
        print("")

    def board(self):
        return [
            board for board in self.game["boards"].values() if board.match.id == self.id
        ][0]

    def play_match(self):
        current_player = self.first_player
        self.board().display()

        while True:
            self.player_moves(current_player)

            self.board().display_with_clear()
            if self.game_over():
                break
            current_player = self.toggle_player(current_player)

    def player_moves(self, player):
        if player == "X":
            self.human_moves()
        else:
            self.computer_moves()

    def game_over(self):
        return self.board().is_full() or self.board().winner() != "N/A"

    def toggle_player(self, player):
        return "X" if player == "O" else "O"

    def human_moves(self):
        choices = [str(square.id) for square in self.board().unused_squares()]
        while True:
            print(f'Choose a square: {" ".join(choices)}')
            choice = input()
            if choice in choices:
                break
            else:
                self.board().display_with_clear()
                print("Input a valid number.")

        self.board().update_square(int(choice), "X")

    def computer_moves(self):
        choice = self.choose_center_square()

        if not choice:
            choice = (
                self.find_winning_move()
                or self.find_defensive_move()
                or self.find_random_square()
            )

        self.board().update_square(choice, "O")

    def choose_center_square(self):
        square = self.board().find_square(5)
        return 5 if square.is_empty() else None

    def find_winning_move(self):
        winning_rows = self.board().possible_winning_rows()
        for row in winning_rows:
            squares = [self.board().find_square(id) for id in row]
            markers = [square.marker for square in squares]
            if markers.count("O") == 2 and markers.count("X") == 0:
                return [square.id for square in squares if square.marker == " "][0]

        return None

    def find_defensive_move(self):
        winning_rows = self.board().possible_winning_rows()
        for row in winning_rows:
            squares = [self.board().find_square(id) for id in row]
            markers = [square.marker for square in squares]
            if markers.count("X") == 2 and markers.count("O") == 0:
                return [square.id for square in squares if square.marker == " "][0]

        return None

    def find_random_square(self):
        choices = self.board().unused_squares()
        return choices[0].id

    def display_match_results(self):
        winner = self.board().winner()
        if winner == "Human":
            print("Player wins!")
        elif winner == "Computer":
            print("Computer wins!")
        else:
            print("It's a tie!")

    def display_goodbye_message(self):
        print("Thanks for playing Tic Tac Toe! Goodbye!")
