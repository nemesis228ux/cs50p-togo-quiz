from um import count

def test_valid():
  assert count("Hello, um") == 1
  assert count("Hello, um, UM") == 2
  assert count("Hello, um, mummy") == 1

def test_invalid():
  assert count("not a substring") == 0
  assert count("hummmm !") == 0