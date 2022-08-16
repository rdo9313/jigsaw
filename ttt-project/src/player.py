class Player:
  def __init__(self, game):
    player_id = len(game["players"]) + 1
    self._id = player_id
    game["players"][player_id] = self

  @property
  def id(self):
    return self._id