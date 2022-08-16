class Computer():
  def __init__(self, game, player):
    self._marker = "O"
    self._player = player

  @property
  def marker(self):
    return self._marker

  @property
  def player(self):
    return self._player