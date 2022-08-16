from src.square import Square

def test_square_initalization():
  square1 = Square("X")
  square2 = Square("O")
  assert square1.marker == "X"
  assert square2.marker == "O"

def test_set_marker():
  square1 = Square("X")
  square1.setMarker = "O"
  assert square1.marker == "O"

def test_is_empty():
  square = Square(" ")
  assert square.is_empty() == True