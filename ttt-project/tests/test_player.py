from src.player import Player

def test_player_initalized_marker():
  player = Player()
  assert player.marker == "X"

def test_player_initalized_score():
  player = Player()
  assert player.score == 0

def test_player_increment_score():
  player = Player()
  player.increment_score()
  assert player.score == 1
