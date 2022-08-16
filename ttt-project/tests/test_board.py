from src.console import *


def reset_board():
    for i in range(1, 10):
        board.update_square(i, " ")


def test_initial_board():
    assert board.match == match


def test_is_full():
    for i in range(1, 10):
        board.update_square(i, "X")
    assert board.is_full() == True


def test_is_not_full():
    reset_board()
    assert board.is_full() == False


def test_computer_win():
    board.update_square(1, "O")
    board.update_square(5, "O")
    board.update_square(9, "O")
    assert board.winner() == "Computer"


def test_human_win():
    board.update_square(3, "X")
    board.update_square(5, "X")
    board.update_square(7, "X")
    assert board.winner() == "Human"


def test_winner_for_tie():
    reset_board()

    assert board.winner() == "tie"


def test_winner_for_neither():
    reset_board()
    for i in range(1, 5):
        board.update_square(i, "X") if i % 2 == 0 else board.update_square(i, "O")
    assert board.winner() == "N/A"


# def test_board_reset():
#     board = Board()
