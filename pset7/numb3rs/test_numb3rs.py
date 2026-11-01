from numb3rs import validate


def test_valide_ip():
  assert validate("192.168.1.1") == True
  assert validate("255.255.255.255") == True
  assert validate("127.0.0.1") == True


def test_invalid_ip():
  assert validate("275.168.1.1") == False
  assert validate("192.168.001.1") == False
  assert validate("cat") == False
  assert validate("1.2.3") == False
  assert validate("1.2.3.4.5") == False