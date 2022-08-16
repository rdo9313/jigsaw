class Square:
    def __init__(self, game, board, marker=" "):
        self._marker = marker
        square_id = len(game["squares"]) + 1
        self._id = square_id
        game["squares"][square_id] = self
        self._board = board

    @property
    def marker(self):
        return self._marker

    @property
    def id(self):
        return self._id

    @property
    def board(self):
        return self._board

    @marker.setter
    def set_marker(self, marker):
        self._marker = marker

    def is_empty(self):
        return self.marker == " "
