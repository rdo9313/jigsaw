from match import Match
from index import build_store
from board import Board
from square import Square
from human import Human
from computer import Computer
from player import Player

game = build_store()
match = Match(game)
board = Board(game, match)
# match.play()
