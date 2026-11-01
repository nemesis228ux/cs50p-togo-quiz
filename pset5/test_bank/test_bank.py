from bank import value

def test_hello():
  assert value("Hello") == 0
  assert value("HELLO") == 0
  assert value("HelLo!") == 0


def test_h():
  assert value("How much") == 20
  assert value("hi") == 20
  assert value("Hi David Melan, how are you?") == 20


def test_others():
  assert value("Good morning") == 100
  assert value("Thanks") == 100
  assert value("come here") == 100