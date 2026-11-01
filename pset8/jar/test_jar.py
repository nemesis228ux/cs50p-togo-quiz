import pytest

from jar import Jar


def test_init():
    with pytest.raises(ValueError):
      Jar(-5)

    assert Jar().capacity == 12


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    with pytest.raises(ValueError):
        Jar().deposit(-9) 
    with pytest.raises(ValueError):
        Jar().deposit(45) 
    with pytest.raises(ValueError):
        Jar().deposit(0) 


def test_withdraw():
    with pytest.raises(ValueError):
        Jar().withdraw(-9) 
    with pytest.raises(ValueError):
        Jar().withdraw(13) 
    with pytest.raises(ValueError):
        Jar().withdraw(0) 