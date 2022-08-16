from src.match import Match
from src.index import build_store
from src.board import Board
from src.square import Square

def test_board_for_match():
  game = build_store()
  match = Match(game)
  board = Board(game, match)
  square = Square(game, board)
  assert match.board() == board
  
